from turtle import Turtle
import random
from data import ball_data
# defining global sizes & limitations
BALL_SPEED = ball_data['BALL_SPEED']
BALL_COLOR = ball_data['BALL_COLOR']
TOP_BOUND = ball_data['TOP_BOUND']
BOT_BOUND = ball_data['BOT_BOUND']
BALL_INCREMENT = ball_data['BALL_INCREMENT']
START_POSITIONS = ball_data['START_POSITIONS']
PIXEL_DISTANCE_TO_PADDLE = ball_data['PIXEL_DISTANCE_TO_PADDLE']
TOP_SHIFT_ANGLE = ball_data['TOP_SHIFT_ANGLE']
BOT_SHIFT_ANGLE = ball_data['BOT_SHIFT_ANGLE']


class Ball:
    def __init__(self):
        self.creations = []
        ball = Turtle()
        ball.penup()
        ball.shape('circle')
        ball.color(BALL_COLOR)
        ball.setheading(random.choice(START_POSITIONS))
        self.creations.append(ball)
        self.ball = self.creations[0]

    def move(self):
        self.ball.forward(BALL_INCREMENT)

    def right_left_correction(self, direction):
        if self.ball.heading() >= 0:
            new_heading = (180 - self.ball.heading()) + direction

        else:
            new_heading = (-180 + abs(self.ball.heading())) + direction
        self.ball.setheading(new_heading)

    def check_collision(self):
        if self.ball.ycor() >= TOP_BOUND or self.ball.ycor() <= -BOT_BOUND:
            new_heading = self.ball.heading() * -1
            self.ball.setheading(new_heading)

        # else:
        #     for paddle in paddle_top:
        #         if self.ball.distance(paddle) <= PIXEL_DISTANCE_TO_PADDLE:
        #             self.right_left_correction(TOP_SHIFT_ANGLE)
        #
        #     for paddle in paddle_bot:
        #         if self.ball.distance(paddle) <= PIXEL_DISTANCE_TO_PADDLE:
        #             self.right_left_correction(BOT_SHIFT_ANGLE)

# elif self.ball.xcor() >= 600 or self.ball.xcor() <= -600:
        #     if self.ball.heading() >= 0:
        #         new_heading = 180 - self.ball.heading()
        #     else:
        #         new_heading = -180 + abs(self.ball.heading())
