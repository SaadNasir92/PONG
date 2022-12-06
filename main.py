from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Field, Board
from data import screen_data
# Screen attribute globals.
SCREEN_WIDTH = screen_data['SCREEN_WIDTH']
SCREEN_HEIGHT = screen_data['SCREEN_HEIGHT']
SCREEN_BGCOLOR = screen_data['SCREEN_BGCOLOR']
SCREEN_TITLE = screen_data['SCREEN_TITLE']

# Creation and setup of screen & field & scoreboard
win = Screen()
win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
win.bgcolor(SCREEN_BGCOLOR)
win.title(SCREEN_TITLE)
win.tracer(0)
field = Field()
board = Board()

# paddle & ball creation
p1 = Paddle('l')
p2 = Paddle('r')
ball = Ball()

win.update()

# player inputs
win.listen()

win.onkey(p1.up, "w")
win.onkey(p1.down, "s")

win.onkey(p2.up, "Up")
win.onkey(p2.down, "Down")

# game set to on and start the loop
game_on = board.check_limit()

while game_on:
    # refresh positions
    win.update()
    time.sleep(.02)

    # ball movement
    ball.move()

    # collision with top and bottom
    ball.vertical_collision()

    # collision with left or right paddles
    ball.pad_collision(p1.y, p2.y)
    win.update()
    # collision with right or left goal
    if ball.hit_goal():
        if ball.ball.xcor() < 0:
            board.goal_update_right()
        else:
            board.goal_update_left()

        # reset ball to middle
        ball.reset_ball()
        # update screen for ball to show middle
        win.update()
        # check to see if score limit reached otherwise restart loop
        game_on = board.check_limit()

# score limit reached, hide turtle and write final score and update.
ball.ball.hideturtle()
board.write_ending()
win.update()

win.exitonclick()
