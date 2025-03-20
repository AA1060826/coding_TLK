#-----------------------------------------------------------------------------
# Name: randon number guessing game
# Purpose: to create a number guessing game
#
# Author: Adithya A
# Created:  March/20/2025
# Updated:  March/20/2025
#-----------------------------------------------------------------------------

import random
number = random.randint(1, 10)
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    print("Wrong!")

if guess == number:
    print("You got it!")
    exit()






