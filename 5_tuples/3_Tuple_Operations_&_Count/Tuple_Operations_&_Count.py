#-----------------------------------------------------------------------------
# Name: Tuple operation and count
# Purpose: to provide a count of the fruit inputted by the user
# and then provides a grade based on the score.
#
# Author:Adithya Arikuti
# Created 7-april-2025
# Updated: 7-april-2025
#-----------------------------------------------------------------------------
# Create a tuple with  repeating  items
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")
#Create a Variable to take users input
fruit_name = input("Enter a fruit name: ")
#Create a variable which desplays count od]f the fruit inputted by the user
Fruit_count = fruit_tuple.count(fruit_name)
#print the fruit count
print("That fruit appears",Fruit_count,"times in the tuple.")