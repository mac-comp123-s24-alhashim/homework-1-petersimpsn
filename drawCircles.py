"""
The program draws 6 circles of different colors around each other.

@author: Peter J. Simpson (psimpson@macalester.edu)
"""


import turtle
import math

scr = turtle.Screen()
turt = turtle.Turtle() #The code references "Turtel", when it should be "Turtle"

scr.bgcolor("seashell")

tColors = ["light salmon", "light sky blue", "pale green", "light coral", "pale turquoise", "plum"]

turt.width(5)
numRings = 6

for i in range(numRings):
    turt.color(tColors[i]) #The tColors[0] should be tColors[i-1] so it changes with each iteration of the for loop
    radius = 40 * (i + 1)

    
    turt.up()
    turt.forward(radius)
    turt.down()
    
    turt.left(90)
    turt.circle(radius) #"turt.circle(i)" makes the radius 1-6, instead of the radius 40*(1-6)
    turt.right(90) #The turtle was turning 60 instead of 90, making all of the rings off-center
    
    turt.up() # the turt.up command was missing the "()" at the end
    turt.backward(radius)
    turt.down()

scr.exitonclick()
