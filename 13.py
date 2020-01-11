import turtle
import random
win=turtle.Screen()
win.bgcolor("black")
win.colormode(255)
pen0=turtle.Turtle()
pen0.pensize(3)


pen0.color((120,200,214))
pen0.fillcolor((120,200,214))
for i in range(50):
    pen0.forward(10+i*5)
    pen0.forward(10 + (i+1) * 5)
    pen0.forward(10 + (i+2) * 5)
    pen0.left(120)
    pen0.left(15)
turtle.done()
