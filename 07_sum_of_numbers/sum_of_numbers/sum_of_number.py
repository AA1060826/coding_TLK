#-----------------------------------------------------------------------------
# Name:sum of number calculator
# Purpose: to show the summ of 0 to number inputted
#
# Author: Adithya A
# Created:  March/20/2025
# Updated:  March/20/2025
#-----------------------------------------------------------------------------

total = 0
n = int(input("Enter a number: "))
for i in range(1,n+1):
    total += i
    print(total)