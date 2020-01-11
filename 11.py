import turtle
import random
win=turtle.Screen()
win.bgcolor("black")
win.colormode(255)
pen0=turtle.Turtle()
pen0.pensize(3)
colors=["#86AC43","#AA9843","#0087FF","#CC0066","#742BCC","#00FF00","#0000FF","#FF5664"]

for i in range(1,9):
    pen0.color(colors[i-1])
    pen0.fillcolor(colors[i - 1])
    for j in range(12):
        pen0.begin_fill()
        pen0.left(30)
        pen0.circle(200-i*20)
        pen0.end_fill()
turtle.done()