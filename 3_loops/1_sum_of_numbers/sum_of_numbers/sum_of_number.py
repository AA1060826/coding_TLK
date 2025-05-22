#-----------------------------------------------------------------------------
# Name:sum of number calculator
# Purpose: to show the summ of 0 to number inputted
#
# Author: Adithya A
# Created:  March/20/2025
# Updated:  March/20/2025
#-----------------------------------------------------------------------------
# assign 0 to initial total value
total = 0
#use a variable to input promt
n = int(input("Enter a number: "))
#use for and in range to print numbers in a desired range
for i in range(1,n+1):
#use "+" symbol to add to the total value
    total += i
#print total value
    print(total)