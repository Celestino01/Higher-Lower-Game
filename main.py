from art import logo
from art import vs
import game_data
import random

print(logo)

def random_list_selection():
  new_list = game_data.data
  random_select = random.choice(new_list)
  return random_select
  
def name_selection(name):
  return name['name']

def follower_selection(follow):
  return follow['follower_count']

def description_selection(description):
  return description['description']

def country_selection(country):
  return country['country']
   
score = 0

def game():
  keep_game_going = True
  global score
  
  while keep_game_going == True:
    global score
    random_list_a = random_list_selection()
    random_list_b = random_list_selection()
    
    name_a = name_selection(random_list_a)
    name_b = name_selection(random_list_b)
    
    follower_a = follower_selection(random_list_a)
    follower_b = follower_selection(random_list_b)
    
    description_a = description_selection(random_list_a)
    description_b = description_selection(random_list_b)
    
    country_a = country_selection(random_list_a)
    country_b = country_selection(random_list_b)

    if score > 0:
      print(f"You're right! Current score: {score}")
    
    print(f"Compare A: {name_a}, {description_a}. from {country_a}")
    print(vs)
    print(f"Compare B: {name_b}, {description_b}. from {country_b}")
    
    follower_count = input("Who has more followers? Type 'A' or 'B' ")
    
    if follower_count == "A":
      if follower_a > follower_b:
        score += 1
      elif follower_a < follower_b:
        print(f"Sorry, that's wrong. final score {score}")
        keep_game_going = False
      else:
        print("They're equal so keep going")
    elif follower_count == "B":
      if follower_b > follower_a:
        score += 1
      elif follower_b < follower_a:      
        print(f"Sorry, that's wrong. final score {score}")
        keep_game_going = False
      else:
        print("They're equal so keep playing")
game()
