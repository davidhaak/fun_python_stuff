#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:21:57 2019

@author: dhaak
"""

import turtle

def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)