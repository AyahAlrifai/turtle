import turtle
import random
win=turtle.Screen()
win.bgcolor("black")
win.colormode(255)
pen0=turtle.Turtle()
pen0.pensize(3)
colors=["#aa7788","#88cc44","#4657ff","#842390"]

for s in range(0,361,5):
    pen0.color(colors[s%4])
    pen0.forward(s)
    pen0.left(90)
