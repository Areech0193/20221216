# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
tur = turtle.Turtle()
screen=turtle.Screen()
screen.setup(800,600)
tur.penup()
tur.goto(-300,200)
tur.pendown()
tur.fillcolor('#BB5500')
tur.begin_fill()
for i in range(4):
    tur.forward(100)
    tur.right(90)
tur.end_fill()
turtle.done()
turtle.exitonclick()