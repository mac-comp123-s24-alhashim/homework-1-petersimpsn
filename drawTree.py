"""
This code will draw a pretty tree.

@author: Peter J. Simpson (psimpson@macalester.edu)
"""

import turtle

scr = turtle.Screen()
turt = turtle.Turtle()
turtle.speed(0)
scr.bgcolor("blue")

turtle.color("sienna")
turtle.begin_fill()
turtle.goto((-100,-250))
turtle.forward(200)
turtle.left(90)
turtle.forward(700)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(700)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(90,100)
turtle.left(135)
turtle.forward(200)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()

turtle.up()
turtle.color("green")
turtle.goto(170,170)
turtle.begin_fill()
for i in range(4):
    turtle.forward(30)
    turtle.left(90)
turtle.end_fill()

turtle.up()
turtle.color("green")
turtle.goto(230,230)
turtle.begin_fill()
for i in range(4):
    turtle.forward(30)
    turtle.left(90)
turtle.end_fill()

turtle.up()
turtle.color("red")
turtle.goto(210,160)
turtle.begin_fill()
for i in range(4):
    turtle.forward(30)
    turtle.left(90)
turtle.end_fill()

scr.exitonclick()