from turtle import Screen
from paddle import Paddle
import time
# Screen attribute globals.
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000
SCREEN_BGCOLOR = 'black'
SCREEN_TITLE = 'Pang Pong'

# Creation and setup of screen
win = Screen()
win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
win.bgcolor(SCREEN_BGCOLOR)
win.title(SCREEN_TITLE)
win.tracer(0)

# paddle creation
p1 = Paddle('l')
p2 = Paddle('r')
win.update()

# player inputs
win.listen()

win.onkey(p1.up, "w")
win.onkey(p1.down, "s")

win.onkey(p2.up, "Up")
win.onkey(p2.down, "Down")

# game set to on and start the loop
game_on = True
while game_on:
    win.update()

win.exitonclick()
