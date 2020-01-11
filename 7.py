import turtle
import math
import random
win=turtle.Screen()
win.bgcolor("#FFFFFF")
win.colormode(255)
pen0=turtle.Turtle()
pen0.pensize(3)
pen0.speed(0)
pen0.color("#000000")
def draw_arc(b,r):
    c=2*math.pi*r
    n=int(c/180)+1
    l=c/(60*n)
    for i in range(n):
        b.fd(l)
        b.lt(60/n)


def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(120)
    draw_arc(b,r)
    b.rt(15)

for i in range(-550,551,150):
    for j in range(-320,321,120):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        pen0.penup()
        pen0.goto(i,j)
        pen0.pendown()
        pen0.begin_fill()
        pen0.fillcolor((red, green, blue))
        for n in range(8):
             draw_petal(pen0,500)
        pen0.end_fill()
turtle.done()