import random
from game_data import data
import art

def assign_values(string):
  """To fetch a random key from the list of celebrities"""
  random_number1 = random.randint(0,len(data))
  if(data[random_number1] != string):
      return data[random_number1]
  else:
    assign_values(string)

print("Welcome to the HIGHER-LOWER game!") 

def play_game():

  print(art.logo)
  score = 0 
  should_game_continue = "True"
  A_num = assign_values("")
  B_num = assign_values(A_num)

  while(should_game_continue):
    print(f"\nCompare A: {A_num['name']}, {A_num['description']} from {A_num['country']}")
    print(art.vs)
    print(f"With B: {B_num['name']}, {B_num['description']} from {B_num['country']}")
    #Asking the input from the user
    ans = input("\n\nWhich one do you think has high followers count (A/B): ")
    if(ans == "A" and (A_num['follower_count'] > B_num['follower_count'])):
      score+=1
      print(f"Your score is {score}")
      print(art.logo)
      A_num = B_num
      B_num = assign_values(A_num)
    elif(ans == "B" and (B_num['follower_count'] > A_num['follower_count'])):
      score+=1
      print(f"Your score is {score}")
      print(art.logo)
      A_num = B_num
      B_num = assign_values(A_num)
    else:
      print(f"Your score is {score}")
      print("Oops, You lost the game!")
      
      should_game_continue = False
  
play_game() #Calling the game

#Repeat the game until the user wants
ch = 'y'
while(ch != 'n'):
  ch = input("\nWant to play another game? (y/n): ")
  if ch == 'y':
    play_game()
  else:
    print("Bye bye come again!")
