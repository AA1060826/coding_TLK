-----------------------------------------------------------------------------
# Name: Set methods
# Purpose: To use basic set methods
#
# Author:Adithya Arikuti
# Created 17-4-2025
# Updated: 17-4-2025
#-----------------------------------------------------------------------------


# Create the set
letters = {'a', 'b', 'c'}

# Add multiple elements using update
letters.update(['d', 'e', 'f'])

# Remove 'b' using discard (won’t cause an error if 'b' is missing)
letters.discard('b')

# Print the updated set
print(letters)
