from turtle import Turtle
from data import scoreboard_data

# GLOBALS from DATA FILE
FIELD_COLOR = scoreboard_data['FIELD_COLOR']
FIELD_OUTLINE_SIZE = scoreboard_data['FIELD_OUTLINE_SIZE']
TOP_LEFT = scoreboard_data['TOP_LEFT']
TOP_RIGHT = scoreboard_data['TOP_RIGHT']
BOT_LEFT = scoreboard_data['BOT_LEFT']
BOT_RIGHT = scoreboard_data['BOT_RIGHT']
BOARD_COLOR = scoreboard_data['BOARD_COLOR']
SCORE_COLOR = scoreboard_data['SCORE_COLOR']
BOARD_ADJUST = scoreboard_data['BOARD_ADJUST']
BOARD_CENTER_TEXT_X = scoreboard_data['BOARD_CENTER_TEXT_X']
BOARD_LEFT_TEXT_X = (TOP_LEFT[0] / 2) - BOARD_ADJUST
BOARD_RIGHT_TEXT_X = (TOP_RIGHT[0] / 2) + BOARD_ADJUST
BOARD_CENTER_TEXT_Y = TOP_LEFT[1] + BOARD_ADJUST
BOARD_FONT = scoreboard_data['BOARD_FONT']
BOARD_FONT_SIZE = scoreboard_data['BOARD_FONT_SIZE']
WINNING_FONT_SIZE = scoreboard_data['WINNING_FONT_SIZE']
BOARD_FONT_TYPE = scoreboard_data['BOARD_FONT_TYPE']
BOARD_ALIGN = scoreboard_data['BOARD_ALIGN']
MAX_SCORE = scoreboard_data['MAX_SCORE']


# FIELD DRAW
class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor(FIELD_COLOR)
        self.pensize(FIELD_OUTLINE_SIZE)
        self.goto(TOP_LEFT)
        self.top_left = self.pos()
        self.pendown()
        self.goto(TOP_RIGHT)
        self.top_right = self.pos()
        self.goto(BOT_RIGHT)
        self.bot_right = self.pos()
        self.goto(BOT_LEFT)
        self.bot_left = self.pos()
        self.goto(self.top_left)


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.write_score()

    def goal_update_left(self):
        self.left_score += 1
        self.clear()
        self.write_score()

    def goal_update_right(self):
        self.right_score += 1
        self.clear()
        self.write_score()

    def check_limit(self):
        if self.left_score == MAX_SCORE or self.right_score == MAX_SCORE:
            return False
        else:
            return True

    def write_score(self):
        self.pencolor(BOARD_COLOR)
        self.goto(BOARD_CENTER_TEXT_X, BOARD_CENTER_TEXT_Y)
        self.write(arg=':', align=BOARD_ALIGN, font=(BOARD_FONT, BOARD_FONT_SIZE, BOARD_FONT_TYPE))
        self.goto(BOARD_RIGHT_TEXT_X, BOARD_CENTER_TEXT_Y)
        self.pencolor(SCORE_COLOR)
        self.write(arg=f'{self.right_score}', align=BOARD_ALIGN, font=(BOARD_FONT, BOARD_FONT_SIZE, BOARD_FONT_TYPE))
        self.goto(BOARD_LEFT_TEXT_X, BOARD_CENTER_TEXT_Y)
        self.write(arg=f'{self.left_score}', align=BOARD_ALIGN, font=(BOARD_FONT, BOARD_FONT_SIZE, BOARD_FONT_TYPE))

    def write_ending(self):
        self.goto(0, 0)
        self.pencolor(SCORE_COLOR)
        if self.left_score == MAX_SCORE:
            self.write(arg=f'Left Player won! {self.left_score} - {self.right_score}',
                       align=BOARD_ALIGN, font=(BOARD_FONT, WINNING_FONT_SIZE, BOARD_FONT_TYPE))
        else:
            self.write(arg=f'Right Player won! {self.right_score} - {self.left_score}',
                       align=BOARD_ALIGN, font=(BOARD_FONT, WINNING_FONT_SIZE, BOARD_FONT_TYPE))
