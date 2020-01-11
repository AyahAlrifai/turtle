import turtle
import math
win=turtle.Screen()
win.bgcolor("black")
pen0=turtle.Turtle()
pen0.pensize(3)
pen0.speed(80)
pen0.speed(150)
color=["#F760C5","#88DCF0","#CDEB0E","#EE0808","#F2BE84","#0EEB42"]


def draw_arc(b,r):
    c=2*math.pi*r
    n=int(c/180)+1
    l=c/(60*n)
    pen0.penup()
    for i in range(n):
        if i>20:
            pen0.pendown()
        b.fd(l)
        b.lt(60/n)


def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(120)
    draw_arc(b,r)
    b.rt(15)

for j in range(3):
    pen0.lt(30)
    pen0.fillcolor(color[j])
    pen0.color(color[j])
    pen0.begin_fill()
    for i in range(8):
        draw_petal(pen0,2000)
    pen0.end_fill()



turtle.done()