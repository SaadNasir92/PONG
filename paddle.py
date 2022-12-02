from turtle import Turtle

# defining global sizes
PADDLE_SIZE = 10
PADDLE_COLOR = 'white'
PADDLE_THICKNESS = 0
PADDLE_MOVEMENT = 100
PADDLE_STARTY = 100
PADDLE_STARTX = 590
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
        for ball in range(PADDLE_SIZE):
            ball = Turtle()
            ball.speed('fastest')
            ball.shape('square')
            ball.color(PADDLE_COLOR)
            ball.penup()
            ball.goto(start_x, start_y)
            start_y -= 20
            self.dotted_collection.append(ball)
        # End of initial creation.
        # Attributes
        self.player = side
        self.top = self.dotted_collection[0]
        self.bot = self.dotted_collection[PADDLE_SIZE - 1]

    # paddle movement
    def up(self):
        if self.top.ycor() < 470:
            for turtle in self.dotted_collection:
                turtle.setheading(90)
                turtle.forward(PADDLE_MOVEMENT)

    def down(self):
        if self.bot.ycor() > -470:
            for turtle in self.dotted_collection:
                turtle.setheading(270)
                turtle.forward(PADDLE_MOVEMENT)

