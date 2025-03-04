#-----------------------------------------------------------------------------
# Name: Student Grading System
# Purpose: Create a Python program that asks for a student's score
# and then provides a grade based on the score.
#
# Author:Adithya Arikuti
# Created 3-March-2025
# Updated: 3-March-2025
#-----------------------------------------------------------------------------
#step 1 print title
print("====Grade finder====")
print()
print()
#step 2 use variables to take the users input
scr = int(input("What is your score out of 100?: "))
#step 3 use conditionals to create the grading system.
if scr >= 90 and scr <= 100:
    print("grade A")
elif scr >= 80 and scr <= 89:
    print("grade B")
elif scr >= 70 and scr <= 79:
    print("grade C")
elif scr >= 60 and scr <=69:
    print("grade D")
elif scr < 60:
    print("grade F")
else:
    print("Wrong input")


