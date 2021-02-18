import turtle
import math
bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,length,n):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def draw_A(t):

    t.lt(75)
    t.fd(100)
    t.rt(145)
    t.fd(100)
    t.pu()
    t.rt(180)
    t.fd(45)
    t.lt(70)
    t.pd()
    t.fd(33)
    t.lt(180)
    t.pu()
    t.fd(80)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.pd()
 #   t.hideturtle()

draw_A(bob)
draw_A(bob)

turtle.mainloop()