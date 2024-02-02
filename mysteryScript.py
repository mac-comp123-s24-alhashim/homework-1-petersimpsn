"""
The goal of the code is to print the name of the user that they input letter by letter, with a space in between.
This is followed by an exclamation point.

@author: Peter J. Simpson (psimpson@macalester.edu)
"""

# This line is asking for used input of their name, which is central to the point of the code.
# This allows the rest of the code to operate, as it prints out this answer.
name = input("What is your name? ")

#This print statement sets up the printing of the user's name line by line
print("Hooray for")
#This for loop prints out the user's name line by line with a space in between each letter
for c in name:
    #This prints each letter from the user's name
    print(c)
    #This prints a space between each letter of the user's name
    print()
#At the end of the user's name an exclamation point is printed
print("!")
