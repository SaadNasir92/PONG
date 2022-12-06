screen_data = {
    'SCREEN_WIDTH': 1500,
    'SCREEN_HEIGHT': 800,
    'SCREEN_BGCOLOR': 'black',
    'SCREEN_TITLE': 'Pang Pong',
    'VERT_SPACE_CUT': 125,
    'HOR_SPACE_CUT': 200,
    'PADDLE_FROM_SIDE_DISTANCE': 30
}

scoreboard_data = {
    'FIELD_COLOR': 'yellow',
    'FIELD_OUTLINE_SIZE': 5,
    'TOP_LEFT': (-screen_data['SCREEN_WIDTH']/2 + screen_data['HOR_SPACE_CUT'],
                 screen_data['SCREEN_HEIGHT']/2 - screen_data['VERT_SPACE_CUT']),

    'TOP_RIGHT': (screen_data['SCREEN_WIDTH']/2 - screen_data['HOR_SPACE_CUT'],
                  screen_data['SCREEN_HEIGHT']/2 - screen_data['VERT_SPACE_CUT']),

    'BOT_LEFT': (-screen_data['SCREEN_WIDTH']/2 + screen_data['HOR_SPACE_CUT'],
                 -screen_data['SCREEN_HEIGHT']/4 - screen_data['VERT_SPACE_CUT']),

    'BOT_RIGHT': (screen_data['SCREEN_WIDTH']/2 - screen_data['HOR_SPACE_CUT'],
                  -screen_data['SCREEN_HEIGHT']/4 - screen_data['VERT_SPACE_CUT']),
    'BOARD_COLOR': 'white',
    'SCORE_COLOR': 'red',
    'BOARD_ADJUST': 40,
    'BOARD_CENTER_TEXT_X': 0,
    'BOARD_FONT': 'Arial',
    'BOARD_FONT_SIZE': 36,
    'WINNING_FONT_SIZE': 24,
    'BOARD_FONT_TYPE': 'bold',
    'BOARD_ALIGN': 'center',
    'MAX_SCORE': 7
}

paddle_data = {
    'PADDLE_SIZE': (8, 1),
    'PADDLE_COLOR': 'white',
    'TOP_BOUNDARY': scoreboard_data['TOP_RIGHT'][1],
    'BOT_BOUNDARY': scoreboard_data['BOT_RIGHT'][1],
    'PADDLE_STARTX': scoreboard_data['TOP_RIGHT'][0] - screen_data['PADDLE_FROM_SIDE_DISTANCE'],
    'PADDLE_STARTY': 0,
    'PADDLE_MOVEMENT': 45
}

ball_data = {
    'BALL_SPEED': 10,
    'BALL_COLOR': 'red',
    'TOP_BOUNDARY': scoreboard_data['TOP_RIGHT'][1],
    'BOT_BOUNDARY': scoreboard_data['BOT_RIGHT'][1],
    'RIGHT_BOUND_X': scoreboard_data['TOP_RIGHT'][0],
    'LEFT_BOUND_X': scoreboard_data['TOP_LEFT'][0],
    'START_POSITIONS': [40, 130, 220, 310],
    'LEFT_BOT_CORNER_ANGLE': 225,
    'LEFT_TOP_CORNER_ANGLE': 135,
    'RIGHT_BOT_CORNER_ANGLE': 315,
    'RIGHT_TOP_CORNER_ANGLE': 45,
    'SUCCESS_SPEED_UP': 0.25
}