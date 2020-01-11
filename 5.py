import turtle
import math
win=turtle.Screen()
win.bgcolor("black")
pen0=turtle.Turtle()
pen0.pensize(3)
pen0.speed(0)
color=["#F760C5","#88DCF0","#CDEB0E","#EE0808","#F2BE84","#0EEB42"]

def draw_arc(b,r,x):
    c=2*math.pi*r
    n=int(c/180)+1
    l=c/(60*n)
    for i in range(n):
        pen0.penup()
        if i>20 and x==0:
            pen0.pendown()
        if i<50 and x==1:
            pen0.pendown()
        print(i,x)
        b.fd(l)
        b.lt(60/n)


def draw_petal(b,r):
    draw_arc(b,r,0)
    b.lt(120)
    draw_arc(b,r,1)
    b.rt(15)

for j in range(3):
    pen0.lt(30)
    for i in range(8):
        pen0.fillcolor(color[j])
        pen0.color(color[j])
        draw_petal(pen0, 2000)

turtle.done()