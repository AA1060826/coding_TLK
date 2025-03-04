#-----------------------------------------------------------------------------
# Name:Voting Eligibility checker
# Purpose:Write a Python program that checks if a person is eligible to vote based on their age.
#
# Author:      Adithya Arikuti
# Created:     3-March-2025
# Updated:     3-March-2025
#-----------------------------------------------------------------------------
print("Voting eligibility checker")
print()
print()
#Use variables  to store and ask for input
age = int(input("Enter your age: "))
#Use conditionals to check age
if age >= 18:
    print("You are eligible to vote!!!!!")
else:
    print("You are not eligible to vote...YET!!")