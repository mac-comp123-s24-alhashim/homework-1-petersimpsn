"""
This code will create 25 random squares around the screen of 4 various colors.

@author: Peter J. Simpson (psimpson@macalester.edu)
"""

import random
import turtle

scr = turtle.Screen()
scr.bgcolor("light gray")
turtle.speed(0)
turt = turtle.Turtle()

colorList = ["red", "green", "blue", "yellow"]

for i in range(25):
    turtleColor = random.choice(colorList)
    turtle.color(turtleColor)
    turtle.penup()
    turtle.goto(random.randrange(-250,250),random.randrange(-250, 250))
    turtle.pendown()

    turtle.begin_fill()
    for i in range(4):
        turtle.forward(25)
        turtle.left(90)
    turtle.end_fill()


scr.exitonclick()
