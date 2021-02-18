import turtle
import math
bob = turtle.Turtle()
print(bob)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def triangle(t,r,angle):
        y = r * math.sin(angle * math.pi / 180)

        t.rt(angle)
        t.fd(r)
        t.lt(90+angle)
        t.fd(2*y)
        t.lt(90+angle)
        t.fd(r)
        t.lt(180-angle)


def turtle_pie(t,r,n):
    t.lt(30)
    for i in range(n):
        triangle(t,r,(360/n)/2)
        t.lt(360/n)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,length,n):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t,r):
    arc(t,r,360)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def petal(t,r,angle):

  for i in range(2):
   arc(t,r,angle)
   t.lt(180-angle)



#square(bob,100)

#polygon(bob,100,50)

#circle(bob,50)

#arc(bob,100,180)

def flower(t,r,angle,petals):

 for i in range(petals):
     petal(t,r,angle)
     t.lt(360.0/petals)

def move(t,length):
    t.pu()
    t.fd(length)
    t.pd()
"""move(bob, -100)
flower(bob,60,60,7)

move(bob, 100)
flower(bob,40,80,10)

move(bob, 100)
flower(bob,140,20,20)
bob.hideturtle()

"""
#triangle(bob,50)

turtle_pie(bob,40,12)

turtle.mainloop()