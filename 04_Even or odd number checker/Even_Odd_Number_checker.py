#-----------------------------------------------------------------------------
# Name:Even or odd number checker
# Purpose:Create a Python program that asks the user for a number
# and then tells them if the number is even or odd.
#
# Author:      Adithya Arikuti
# Created:     3-March-2025
# Updated:     3-March-2025
#-----------------------------------------------------------------------------
#use variable
Number = int(input("Number: "))
#Use conditionals
if Number % 2 == 0:
    print("Even")
else:
    print("Odd")