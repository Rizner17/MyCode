#!/usr/bin/env python3
""" AJRodriguez | Lab 43: Using classes"""
#import all functions from cheat dice
from cheatdice import *
# below are all the swapper and loaded dice classes imported from the cheatdice.py script
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
swapper_score = 0 #starting score is 0, will be incremented upon win
loaded_dice_score = 0 #starting score is 0, will increment
number_of_games = 100000 #total number of games the while loop will run through
game_number = 0 #increments with every game passed
print("Simulation running")
print("==================")
while game_number < number_of_games: #begins the while loop with the condition that the current game number is < total games required
  swapper.roll() #swapper class rolls their dice
  loaded_dice.roll() #laoded dice class rolls their dice

  swapper.cheat() #runs the cheat function from cheatdice.py
  loaded_dice.cheat() #runs the loaded dice function from cheatdice.py

   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1 #if swapper sum is larger, increments their win score by1

  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1 #if loaded dice sum is larger, increments their win score by 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")

