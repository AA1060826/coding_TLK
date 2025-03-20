#-----------------------------------------------------------------------------
# Name: Countdown
# Purpose: To create a countdown which can stop wit the correct input
# Author: Adithya A
# Created:  March/20/2025
# Updated:  March/20/2025
#-----------------------------------------------------------------------------
#asighn count a number u want to start from
Count = 10
#start a while loop
while Count > 0:
#use a variable to get user input
    No = input("")
#use conditionals
    if No != "":
#use break command to stop program
        break
    print(Count)
    Count -= 1
#use if to print msg at the end of the countdown
    if Count == 0:
        print("Blastoff!")



