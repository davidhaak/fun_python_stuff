#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:38:27 2019

@author: dhaak
"""

from turtle import *
from shapes import *

speed(0)

window = turtle.Screen()
window.bgcolor("white")

# Background for snowman
draw_circle(turtle, "#69D9FF", 0, -200, 220)

draw_circle(turtle, "white", 0, -180, 90)  # bottom
draw_circle(turtle, "white", 0, -60, 70)  # middle
draw_circle(turtle, "white", 0, 50, 50)  # top

# Buttons
y = -150
for i in range(5):
    draw_circle(turtle, 'black', 0, y, 7)
    y = y + 45

# eyes
    draw_circle(turtle, 'black', -15, 110, 7)
    draw_circle(turtle, 'black', 15, 110, 7)

# mouth
draw_circle(turtle, "red", 0, 80, 12)
draw_circle(turtle, "white", 0, 85, 12)

# Left arm
left(45)
draw_rectangle(turtle, "brown", 50, 25, 50, 5)
left(0)
draw_rectangle(turtle, "brown", 75, 50, 20, 3)
left(90)
draw_rectangle(turtle, "brown", 75, 50, 20, 3)

# Right arm

left(-45)
draw_rectangle(turtle, "brown", -90, 60, 50, 5)
left(0)
draw_rectangle(turtle, "brown", -100, 50, 20, 3)
left(90)
draw_rectangle(turtle, "brown", -75, 50, 20, 3)

# Message
penup()
color('red')
goto(-200, 250)
write("Happy Nerdy Holidays", font=("Comic", 40, "bold"))

# Lower message
penup()
color('red')
goto(-180, -250)
write("From the Haak Lab", font=("Comic", 40, "bold"))

hideturtle()
turtle.done()
