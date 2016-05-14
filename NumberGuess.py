"""In this project, we'll build a program that rolls a pair of dice and asks the user to guess a number. Based on the user's guess, the program should determine a winner."""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input ("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value you can get is " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "Invalid value"
  else:
    print "Rolling..."
    sleep (2)
    print "The value of your first roll is %d" % (first_roll)
    print "The value of your second roll is %d" % (second_roll)
    sleep (1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep (1)
    if user_guess > total_roll:
      print "Congratulation, you have won this game!"
    else:
      print "Sorry, you lost. But no worries, it happens to the best of us."

roll_dice(6)