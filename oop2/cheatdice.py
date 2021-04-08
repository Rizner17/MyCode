#!/usr/bin/env python3
""" AJRodriguez | LLab43b: Cheatdice script"""
#import random integer from the random library
from random import randint

#Creating a class called Player
class Player:
  def __init__(self):# initializing 
    self.dice = []#self.dice has an empty list until the for loop

  def roll(self):#defines roll function with the for loop below
    self.dice = [] # clears current dice
    for i in range(3):#for loop with a range of 3, 3 rolls per player
      self.dice.append(randint(1,6))#appends the self.dice list with a random # between 1-6

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1

