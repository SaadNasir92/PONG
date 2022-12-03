from turtle import Turtle

# defining global sizes & limitations
PADDLE_SIZE = 10
PADDLE_INCREMENT = 20
PADDLE_LEN = (PADDLE_SIZE * PADDLE_INCREMENT) - 10
PADDLE_COLOR = 'white'
PADDLE_MOVEMENT = 50
PADDLE_STARTY = (PADDLE_LEN / 2)
PADDLE_STARTX = 590
TOP_BOUNDARY = 495
BOT_BOUNDARY = 485

# defining a paddle class with turtles


class Paddle:
    def __init__(self, side):
        # initializing the paddle creates multiple squares lined up to make a paddle based on the side inputted.
        x = 1
        if side == 'l':
            x = -1
        self.dotted_collection = []
        start_x = PADDLE_STARTX * x
        start_y = PADDLE_STARTY
        # create turtles to make a paddle
        for _ in range(PADDLE_SIZE):
            _ = Turtle()
            _.speed('fastest')
            _.shape('square')
            _.color(PADDLE_COLOR)
            _.penup()
            _.goto(start_x, start_y)
            start_y -= PADDLE_INCREMENT
            self.dotted_collection.append(_)
        # End of initial creation.
        # Attributes
        self.player = side
        self.top = self.dotted_collection[0]
        self.bot = self.dotted_collection[PADDLE_SIZE - 1]
        self.top_half = []
        self.bot_half = []

    # paddle movement
    def up(self):
        if self.top.ycor() < TOP_BOUNDARY:
            for turtle in self.dotted_collection:
                turtle.setheading(90)
                turtle.forward(PADDLE_MOVEMENT)

    def down(self):
        if self.bot.ycor() > -BOT_BOUNDARY:
            for turtle in self.dotted_collection:
                turtle.setheading(270)
                turtle.forward(PADDLE_MOVEMENT)

    def update_paddle(self):
        self.top_half = self.dotted_collection[0:5]
        self.bot_half = self.dotted_collection[5:10]
