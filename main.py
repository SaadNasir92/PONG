from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Field
from data import screen_data
# Screen attribute globals.
SCREEN_WIDTH = screen_data['SCREEN_WIDTH']
SCREEN_HEIGHT = screen_data['SCREEN_HEIGHT']
SCREEN_BGCOLOR = screen_data['SCREEN_BGCOLOR']
SCREEN_TITLE = screen_data['SCREEN_TITLE']

# Creation and setup of screen & field
win = Screen()
win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
win.bgcolor(SCREEN_BGCOLOR)
win.title(SCREEN_TITLE)
win.tracer(0)
field = Field()
# paddle & ball creation
# p1 = Paddle('l')
# p2 = Paddle('r')
ball = Ball()
win.update()

# player inputs
# win.listen()
#
# win.onkey(p1.up, "w")
# win.onkey(p1.down, "s")
#
# win.onkey(p2.up, "Up")
# win.onkey(p2.down, "Down")

# game set to on and start the loop
game_on = True
while game_on:
    win.update()
    time.sleep(.05)
    ball.move()
    # p1.update_paddle()
    # p2.update_paddle()
    # p1top = p1.top_half
    # p1bot = p1.bot_half
    # p2top = p1.top_half
    # p2bot = p1.bot_half
    # ball.check_collision(p2top, p2bot)
    # ball.check_collision(p1top, p1bot)


win.exitonclick()
