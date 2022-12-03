from turtle import Turtle, Screen
import random
from data import scoreboard_data
w = Screen()
# RIGHT OR LEFT:
#  180 - angle  for positive angle
# -180 + abs(angle) for negative angle

a = Turtle()
a.shape('square')
a.penup()
a.goto(0, 100)
a.shapesize(8, 1)
print(a.pos())

b = Turtle()
b.shape('circle')
b.penup()
b.goto(-100, 0)


w.exitonclick()