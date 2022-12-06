from turtle import Turtle
from data import paddle_data

# defining global sizes & limitations
PADDLE_SIZE = paddle_data['PADDLE_SIZE']
PADDLE_COLOR = paddle_data['PADDLE_COLOR']

TOP_BOUNDARY = paddle_data['TOP_BOUNDARY']
BOT_BOUNDARY = paddle_data['BOT_BOUNDARY']

PADDLE_STARTX = paddle_data['PADDLE_STARTX']
PADDLE_STARTY = paddle_data['PADDLE_STARTY']
PADDLE_MOVEMENT = paddle_data['PADDLE_MOVEMENT']


# defining a paddle class with turtles
class Paddle:
    def __init__(self, side):
        # Initialize a turtle and give all initial setup, then append to self to be accessible.
        self.obj = []
        x = 1
        if side == 'l':
            x = -1
        pad = Turtle()
        pad.speed('fastest')
        pad.shape('square')
        pad.shapesize(PADDLE_SIZE[0], PADDLE_SIZE[1])
        pad.color(PADDLE_COLOR)
        pad.penup()
        start_x = PADDLE_STARTX * x
        pad.goto(start_x, PADDLE_STARTY)
        self.obj.append(pad)
        self.paddle = self.obj[0]
        # End of initial creation.
        # Attributes
        self.player = side
        self.x = self.paddle.xcor()
        self.y = self.paddle.ycor()

    # paddle movement
    def up(self):
        if (self.y + (PADDLE_SIZE[0] / 2) * 20) + PADDLE_MOVEMENT < TOP_BOUNDARY:
            self.y = self.y + PADDLE_MOVEMENT
            self.paddle.goto(self.x, self.y)

    def down(self):
        if (self.y - (PADDLE_SIZE[0] / 2) * 20) - PADDLE_MOVEMENT > BOT_BOUNDARY:
            self.y = self.y - PADDLE_MOVEMENT
            self.paddle.goto(self.x, self.y)
