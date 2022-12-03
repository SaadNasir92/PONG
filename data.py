screen_data = {
    'SCREEN_WIDTH': 1500,
    'SCREEN_HEIGHT': 800,
    'SCREEN_BGCOLOR': 'black',
    'SCREEN_TITLE': 'Pang Pong',
    'VERT_SPACE_CUT': 125,
    'HOR_SPACE_CUT': 200,
}

ball_data = {
    'BALL_SPEED': 30,
    'BALL_COLOR': 'red',
    'TOP_BOUND': 495,
    'BOT_BOUND': 485,
    'BALL_INCREMENT': 10,
    'START_POSITIONS': [0, 45, 135, 225, 315],
    'PIXEL_DISTANCE_TO_PADDLE': 50,
    'TOP_SHIFT_ANGLE': 22,
    'BOT_SHIFT_ANGLE': 22
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
                  -screen_data['SCREEN_HEIGHT']/4 - screen_data['VERT_SPACE_CUT'])
}
