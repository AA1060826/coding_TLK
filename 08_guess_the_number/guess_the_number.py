#-----------------------------------------------------------------------------
# Name: randon number guessing game
# Purpose: to create a number guessing game
#
# Author: Adithya A
# Created:  March/20/2025
# Updated:  March/20/2025
#-----------------------------------------------------------------------------
#use import to assign value to random
import random
#use variable to make it choose a random number each time
number = random.randint(1, 10)
#assign 0 to initial value of guess
guess = 0
#start a while loop
while guess != number:
#assign guess a int value
    guess = int(input("Guess a number between 1 and 10: "))
#if guess is not equal to number then print "wrong!"
if guess != number:
    print("Wrong!")
#if guess = number print "you got it"
if guess == number:
    print("You got it!")







