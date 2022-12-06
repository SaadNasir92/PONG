from turtle import Turtle
import random
from data import ball_data, paddle_data
# defining global sizes & limitations
BALL_SPEED = ball_data['BALL_SPEED']
BALL_COLOR = ball_data['BALL_COLOR']
TOP_BOUND = ball_data['TOP_BOUNDARY']
BOT_BOUND = ball_data['BOT_BOUNDARY']
RIGHT_BOUND_X = ball_data['RIGHT_BOUND_X']
LEFT_BOUND_X = ball_data['LEFT_BOUND_X']
START_POSITIONS = ball_data['START_POSITIONS']
LEFT_BOT_CORNER_ANGLE = 225
LEFT_TOP_CORNER_ANGLE = 135
RIGHT_BOT_CORNER_ANGLE = 315
RIGHT_TOP_CORNER_ANGLE = 45
PADDLE_SIZE = paddle_data['PADDLE_SIZE']
PADDLE_LOCATION_X = paddle_data['PADDLE_STARTX']
SUCCESS_SPEED_UP = 0.25


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
        self.speed = BALL_SPEED

    def move(self):
        self.ball.forward(self.speed)

    def right_left_correction(self, shift):
        new_heading = 180 - self.ball.heading()
        if shift != 0:
            self.ball.setheading(shift)
        else:
            self.ball.setheading(new_heading)

    def vertical_collision(self):
        if self.ball.ycor() >= TOP_BOUND - BALL_SPEED or self.ball.ycor() <= BOT_BOUND + BALL_SPEED:
            new_heading = self.ball.heading() * -1
            self.ball.setheading(new_heading)

    def pad_collision(self, pad_yl, pad_yr):
        if self.ball.xcor() >= PADDLE_LOCATION_X - BALL_SPEED:
            if (pad_yr - (PADDLE_SIZE[0] / 2) * 20) < self.ball.ycor() < (pad_yr + (PADDLE_SIZE[0] / 2) * 20):
                self.right_left_correction(self.pad_tilt_adjustment(pad_yr))
                self.ball.forward(3 * self.speed)
                self.speed += SUCCESS_SPEED_UP

        elif self.ball.xcor() <= -PADDLE_LOCATION_X + BALL_SPEED:
            if (pad_yl - (PADDLE_SIZE[0] / 2) * 20) < self.ball.ycor() < (pad_yl + (PADDLE_SIZE[0] / 2) * 20):
                self.right_left_correction(self.pad_tilt_adjustment(pad_yl))
                self.ball.forward(1.5 * self.speed)
                self.speed += SUCCESS_SPEED_UP

    def pad_tilt_adjustment(self, pad_y):
        if self.ball.xcor() < 0:
            if (pad_y - (PADDLE_SIZE[0] / 2) * 18) >= self.ball.ycor() >= (pad_y - (PADDLE_SIZE[0] / 2) * 20):
                return LEFT_BOT_CORNER_ANGLE
            elif (pad_y + (PADDLE_SIZE[0] / 2) * 18) <= self.ball.ycor() <= (pad_y + (PADDLE_SIZE[0] / 2) * 20):
                return LEFT_TOP_CORNER_ANGLE
            else:
                return 0
        else:
            if (pad_y - (PADDLE_SIZE[0] / 2) * 18) >= self.ball.ycor() >= (pad_y - (PADDLE_SIZE[0] / 2) * 20):
                return RIGHT_BOT_CORNER_ANGLE
            elif (pad_y + (PADDLE_SIZE[0] / 2) * 18) <= self.ball.ycor() <= (pad_y + (PADDLE_SIZE[0] / 2) * 20):
                return RIGHT_TOP_CORNER_ANGLE
            else:
                return 0

    def hit_goal(self):
        if self.ball.xcor() >= RIGHT_BOUND_X:
            return True
        elif self.ball.xcor() <= LEFT_BOUND_X:
            return True
        else:
            return False

    def reset_ball(self):
        self.speed = BALL_SPEED
        self.ball.hideturtle()
        self.ball.goto(0, 0)
        self.ball.showturtle()
        self.ball.setheading(random.choice(START_POSITIONS))
