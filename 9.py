import turtle
import random
win=turtle.Screen()
win.bgcolor("black")
win.colormode(255)
pen0=turtle.Turtle()
pen0.pensize(3)


for i in range(24):
    pen0.left(15)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    pen0.color((red,green,blue))
    for j in range(4):
        pen0.forward(200)
        pen0.left(90)

turtle.done()
