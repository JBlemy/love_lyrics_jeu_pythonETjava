""" Projet coeur Briser"""
import turtle

s = turtle.Screen().bgcolor("white")
t = turtle.Turtle()
t.speed(5)
t.width(12)

def curve():
    """Nombre de tour."""
    for _ in range(200):
        t.right(1)
        t.forward(1)

def heart():
    """ Forme coeur"""
    t.color("red", "red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.pencolor("white")
t.penup()
t.goto(0,170)
t.pendown()

for broken in range(3):
    t.speed(3)
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(45)

turtle.done()
