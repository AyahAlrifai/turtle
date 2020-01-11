import turtle
import random
import math
win=turtle.Screen()
win.bgcolor("black")
win.colormode(255)
pen0=turtle.Turtle()
pen0.pensize(3)
pen0.color("#DD8100")
pen0.fillcolor("#DD8100")
pen0.begin_fill()
for x in range(24):
    pen0.circle(150)
    pen0.left(15)
pen0.end_fill()

turtle.done()