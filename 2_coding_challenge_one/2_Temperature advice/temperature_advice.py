#-----------------------------------------------------------------------------
# Name:Temperature Advice
# Purpose: Create a Python program that suggests an activity based on the day of the week.
#
# Author:Adithya Arikuti
# Created:3-March-2025
# Updated:3-March-2025
#--------------------------------------------------------------------------
#title
print(" Temperature Advice ")
print()
print()
#Ask for users inout via a variable
Temp = int(input("What is the temperature today?: "))
#Use conditionals to give advice based of the users input
if Temp <= 10:
    print("Its a cold day!!! wear a jacket and warm up")
elif Temp <= 25 and Temp >10:
    print("Its a nice warm day, wear short sleeves")
elif Temp >25 and Temp <100:
    print("Its a hot day, stay cool")
elif Temp >= 100:
    print("HOW ARE YOU ALIVE!!!???")
else:
    print("Are you sure? check again.")


