# Welcome Page for Chess Compyuter

import PySimpleGUI as Sg
import webbrowser
import random


def page():

    url = 'https://github.com/sushilsub/chess-compyuter'
    layout = [
        [Sg.Text('Welcome to Chess Com', font='"Open Sans" 20', pad=((0, 0), (0, 0))), Sg.Text('py', font='"Open Sans" 20 bold', text_color='black', pad=((0, 0), (0, 0))), Sg.Text('uter', font='"Open Sans" 20', pad=((0, 0), (0, 0)))],
        [Sg.Text('A Chess Engine in Python (Version 1.0)', font='"Open Sans" 10', pad=((0, 0), (0, 0)))],
        [Sg.Text(url, tooltip=url, font='"Open Sans" 10 underline', enable_events=True, pad=((0, 0), (0, 30)), key='-DOC-')],
        [Sg.Button('Play With Stockfish', size=(18, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=False, key='-STOCKFISH-'),
         Sg.Text('OR', size=(3, 1), font='"Open Sans" 14', text_color='white', pad=((10, 10), (0, 15)), key='-OR-'),
         Sg.Button('Play With Friend', size=(18, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=False, key='-FRIEND-')
         ],
        [Sg.Text('Choose Stockfish Level:', font='"Open Sans" 14', pad=((0, 0), (0, 15)), text_color='#465362', key='-LEVEL-')],
        [Sg.Button('1', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-1-'),
         Sg.Button('2', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-2-'),
         Sg.Button('3', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-3-'),
         Sg.Button('4', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-4-'),
         Sg.Button('5', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-5-'),
         Sg.Button('6', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-6-'),
         Sg.Button('7', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-7-'),
         Sg.Button('8', size=(3, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), disabled=True, key='-8-')
         ],
        [Sg.Text('Choose Color:', font='"Open Sans" 14', pad=((0, 0), (0, 15)), text_color='#465362', key='-COLOR-')],
        [Sg.Button('Black', size=(8, 1), font='"Open Sans" 12', pad=((0, 0), (0, 10)), disabled=True, key='-BLACK-'),
         Sg.Button('White', size=(8, 1), font='"Open Sans" 12', pad=((0, 0), (0, 10)), disabled=True, key='-WHITE-'),
         Sg.Button('Random', size=(8, 1), font='"Open Sans" 12', pad=((0, 0), (0, 10)), disabled=True, key='-RANDOM-')
         ]
    ]

    window = Sg.Window("Chess Compyuter (No Castling, No Promotion, No En Passant)", layout, margins=(10, 10))
    mode = 'friend'
    level = 0
    color = 1
    while True:
        event, values = window.read()

        # Open URL to Documentation if Clicked
        if event == '-DOC-':
            webbrowser.open(url)

        # Select Friend Mode
        if event == '-FRIEND-':
            mode = 'friend'
            break

        # Select Stockfish Mode
        if event == '-STOCKFISH-':
            mode = 'stockfish'
            window.Element('-STOCKFISH-').update(disabled=True)
            window.Element('-FRIEND-').update(disabled=True)
            window.Element('-OR-').update(text_color='#465362')
            window.Element('-LEVEL-').update(text_color='white')
            for i in range(1, 9):
                window.Element('-' + str(i) + '-').update(disabled=False)
            continue

        # Select Level of Stockfish
        for i in range(1, 9):
            if event == ('-' + str(i) + '-'):
                level = i
                for j in range(1, 9):
                    window.Element('-' + str(j) + '-').update(disabled=True)
                window.Element('-LEVEL-').update(text_color='#465362')
                window.Element('-COLOR-').update(text_color='white')
                window.Element('-BLACK-').update(disabled=False)
                window.Element('-WHITE-').update(disabled=False)
                window.Element('-RANDOM-').update(disabled=False)
            continue

        # Select Color to Play Against Stockfish
        if event == '-BLACK-':
            color = 0
            break
        if event == '-WHITE-':
            color = 1
            break
        if event == '-RANDOM-':
            color = random.choice([0, 1])
            break

        # Manual Close Window
        elif event == Sg.WIN_CLOSED:
            print('Thank You for using Chess Compyuter.')
            quit()

    window.close()
    return mode, level, color
