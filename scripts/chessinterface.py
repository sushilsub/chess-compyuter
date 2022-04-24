# Chess Interface

import PySimpleGUI as Sg
import welcome
import pyautogui
import display
import fen2bmn
import bmn2fen
import newposition
import rules
import checks
import stockfishmove

# Welcome Screen - Welcome Color is 1 if not playing against Stockfish
mode, level, welcome_color = welcome.page()

# Determine Size of Image using Display Monitor Size
screen_width, screen_height = pyautogui.size()
window_size = int(min([screen_height, screen_width]) * 0.6)
size = (window_size, window_size)

# Initial Position, Board Size and User Perspective Color
user_color = welcome_color
FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
BMN = fen2bmn.fen2bmn(FEN)

# Define Window Layout
layout = [
    [Sg.Text('FEN: ', size=(4, 1), font='"Open Sans" 11', pad=((0, 0), (0, 15))), Sg.InputText(FEN, disabled_readonly_background_color='#738498', text_color='white', size=(10, 1), expand_x=True, font='"Open Sans" 11', pad=((0, 0), (0, 15)), disabled=True, key='-FEN-')],
    [Sg.Text('White to Play', size=(12, 1), font='"Open Sans" 14 bold', pad=((0, 0), (0, 15)), key='-PLAY-'), Sg.Push(), Sg.Button('Flip Board', size=(9, 1), font='"Open Sans" 12', pad=((0, 0), (0, 15)), key='-FLIP-')],
    [Sg.Image('board.png', pad=((0, 0), (0, 10)), key='-BOARD-')],
    [Sg.Text('Enter Square for Piece to Move:', size=(26, 1), font='"Open Sans" 14', key='-INSTRUCTION-'), Sg.InputText(size=(3, 1), pad=((0, 10), (0, 0)), font='"Open Sans" 14', key='-INPUT-'), Sg.Button('Enter', font='"Open Sans" 12', key='-ENTER-')],
    [Sg.Text('', size=(30, 1), font='"Open Sans" 14 bold', text_color='salmon', key='-VALID-')]
]

# Display Board with Initial Position and Possible King in Check
play_color = 1
img_board = display.position(BMN, user_color)
img_board.resize(size).save('board.png')
window = []

BMN_next = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

moves = 500
square = 'a1'
new_square = 'a1'
premove_square = 'a1'
premove_new_square = 'a1'
square_king = 'a1'

for move2x in range(1, (2 * moves)):
    if move2x == 1:
        BMN_cur = BMN
    else:
        BMN_cur = BMN_next

    # For stockfish mode - use engine
    if mode == 'stockfish' and play_color != welcome_color:
        best_move = stockfishmove.stockfishmove(FEN, 1 - welcome_color, level)
        square = best_move[0:2]
        new_square = best_move[2:4]
        BMN_valid = rules.selectedsquare(BMN_cur, square)
        errormove, BMN_next = newposition.newBMN(BMN_cur, BMN_valid, square, new_square)
        if move2x == 1:
            window = Sg.Window("Chess Compyuter (No Castling, No Promotion, No En Passant)", layout, margins=(10, 10), finalize=True)

    # For friend mode - ask user
    elif mode == 'friend' or (mode == 'stockfish' and play_color == welcome_color):
        if move2x == 1:
            window = Sg.Window("Chess Compyuter (No Castling, No Promotion, No En Passant)", layout, margins=(10, 10), finalize=True)
        while True:
            event, values = window.read()
            if event == '-ENTER-':
                square = values['-INPUT-']
                break
            if event == '-FLIP-':
                user_color = 1 - user_color
                img_board = display.position(BMN_cur, user_color)
                if move2x != 1:
                    img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                    img_board = display.kingincheck(img_board, BMN_cur, 1 - play_color, user_color)
                img_board.resize(size).save('board.png')
                window.Element('-BOARD-').update('board.png')
            if event == Sg.WIN_CLOSED:
                print('Thank You for using Chess Compyuter.')
                print('FEN of Last Position: ' + FEN)
                quit()

        # Check if Input is Valid and Piece has Valid Moves
        BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        valid_input_square = 0
        valid_moves = 0
        while valid_input_square == 0 or valid_moves == 0:
            valid_input_square = checks.validsquareselected(BMN_cur, square, play_color)
            if valid_input_square == 0:
                img_board = display.position(BMN_cur, user_color)
                if move2x != 1:
                    img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                    img_board = display.kingincheck(img_board, BMN_cur, 1 - play_color, user_color)
                img_board.resize(size).save('board.png')
                window.Element('-BOARD-').update('board.png')
                window.Element('-VALID-').update('Invalid Square! Select Again.')
                window.Element('-INPUT-').update('')

                while True:
                    event, values = window.read()
                    if event == '-ENTER-':
                        square = values['-INPUT-']
                        break
                    if event == '-FLIP-':
                        user_color = 1 - user_color
                        img_board = display.position(BMN_cur, user_color)
                        if move2x != 1:
                            img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                            img_board = display.kingincheck(img_board, BMN_cur, 1 - play_color, user_color)
                        img_board.resize(size).save('board.png')
                        window.Element('-BOARD-').update('board.png')
                    if event == Sg.WIN_CLOSED:
                        print('Thank You for using Chess Compyuter.')
                        print('FEN of Last Position: ' + FEN)
                        quit()

            if valid_input_square == 1:
                if valid_moves == 0:
                    BMN_valid = rules.selectedsquare(BMN_cur, square)
                    img_board = display.position(BMN_cur, user_color)
                    if move2x != 1:
                        img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                        img_board = display.kingincheck(img_board, BMN_next, 1 - play_color, user_color)
                    img_board = display.valid(img_board, BMN_valid, user_color)
                    img_board.resize(size).save('board.png')
                    window.Element('-BOARD-').update('board.png')
                    valid_moves = checks.novalidmoves(BMN_valid)
                    if valid_moves == 0:
                        window.Element('-VALID-').update('No Valid Moves! Select Again.')
                        window.Element('-INPUT-').update('')

                        while True:
                            event, values = window.read()
                            if event == '-ENTER-':
                                square = values['-INPUT-']
                                break
                            if event == '-FLIP-':
                                user_color = 1 - user_color
                                img_board = display.position(BMN_cur, user_color)
                                if move2x != 1:
                                    img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                                    img_board = display.kingincheck(img_board, BMN_next, 1 - play_color, user_color)
                                img_board = display.valid(img_board, BMN_valid, user_color)
                                img_board.resize(size).save('board.png')
                                window.Element('-BOARD-').update('board.png')
                            if event == Sg.WIN_CLOSED:
                                print('Thank You for using Chess Compyuter.')
                                print('FEN of Last Position: ' + FEN)
                                quit()

        window.Element('-VALID-').update('')

        # Valid Movable Square for Selected Piece
        window.Element('-INSTRUCTION-').update('Enter New Square for Piece:')
        window.Element('-INPUT-').update('')

        while True:
            event, values = window.read()
            if event == '-ENTER-':
                new_square = values['-INPUT-']
                break
            if event == '-FLIP-':
                user_color = 1 - user_color
                img_board = display.position(BMN_cur, user_color)
                if move2x != 1:
                    img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                    img_board = display.kingincheck(img_board, BMN_next, 1 - play_color, user_color)
                img_board = display.valid(img_board, BMN_valid, user_color)
                img_board.resize(size).save('board.png')
                window.Element('-BOARD-').update('board.png')
            if event == Sg.WIN_CLOSED:
                print('Thank You for using Chess Compyuter.')
                print('FEN of Last Position: ' + FEN)
                quit()

        # Check if New Square is an Error
        valid_new_square = 0
        errormove = 1
        while valid_new_square == 0 or errormove == 1:
            valid_new_square = checks.validnewsquaretypo(new_square)
            if valid_new_square == 0:
                window.Element('-VALID-').update('Invalid New Square! Select Again.')
                window.Element('-INPUT-').update('')

                while True:
                    event, values = window.read()
                    if event == '-ENTER-':
                        new_square = values['-INPUT-']
                        break
                    if event == '-FLIP-':
                        user_color = 1 - user_color
                        img_board = display.position(BMN_cur, user_color)
                        if move2x != 1:
                            img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                            img_board = display.kingincheck(img_board, BMN_next, 1 - play_color, user_color)
                        img_board = display.valid(img_board, BMN_valid, user_color)
                        img_board.resize(size).save('board.png')
                        window.Element('-BOARD-').update('board.png')
                    if event == Sg.WIN_CLOSED:
                        print('Thank You for using Chess Compyuter.')
                        print('FEN of Last Position: ' + FEN)
                        quit()

            if valid_new_square == 1:
                errormove, BMN_next = newposition.newBMN(BMN_cur, BMN_valid, square, new_square)
                if errormove == 1:
                    window.Element('-VALID-').update('Invalid New Square! Select Again.')
                    window.Element('-INPUT-').update('')

                    while True:
                        event, values = window.read()
                        if event == '-ENTER-':
                            new_square = values['-INPUT-']
                            break
                        if event == '-FLIP-':
                            user_color = 1 - user_color
                            img_board = display.position(BMN_cur, user_color)
                            if move2x != 1:
                                img_board = display.oldnewsquares(img_board, premove_square, premove_new_square, user_color)
                                img_board = display.kingincheck(img_board, BMN_next, 1 - play_color, user_color)
                            img_board = display.valid(img_board, BMN_valid, user_color)
                            img_board.resize(size).save('board.png')
                            window.Element('-BOARD-').update('board.png')
                        if event == Sg.WIN_CLOSED:
                            print('Thank You for using Chess Compyuter.')
                            print('FEN of Last Position: ' + FEN)
                            quit()

        window.Element('-VALID-').update('')

    # Move Selected Piece
    img_board = display.position(BMN_next, user_color)
    img_board = display.oldnewsquares(img_board, square, new_square, user_color)
    img_board = display.kingincheck(img_board, BMN_next, play_color, user_color)
    img_board.resize(size).save('board.png')
    window.Element('-BOARD-').update('board.png')
    window.Element('-INSTRUCTION-').update('Enter Square for Piece to Move:')
    window.Element('-INPUT-').update('')
    FEN = bmn2fen.bmn2fen(BMN_next)
    window.Element('-FEN-').update(FEN)

    # Detect King Square and CheckMate
    kingcheck = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if (BMN_next[i][j] == 'k' or BMN_next[i][j] == 'K') and (BMN_next[i][j].isupper() != play_color):
                square_king = chr(97 + j) + str(8 - i)
                if checks.squareattacked(BMN_next, square_king, play_color) == 1:
                    kingcheck = 1

    valid_moves_check = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if BMN_next[i][j].isupper() != play_color:
                square_piece = chr(97 + j) + str(8 - i)
                BMN_valid_check = rules.selectedsquare(BMN_next, square_piece)
                if checks.novalidmoves(BMN_valid_check) == 1:
                    valid_moves_check = 1
                    break

    if kingcheck == 1 and valid_moves_check == 0:
        checkmate = 1
        break

    # Next Steps
    if (move2x + 1) % 2 == 1:
        window.Element('-PLAY-').update('White to Play')
        play_color = 1
    elif (move2x + 1) % 2 == 0:
        window.Element('-PLAY-').update('Black to Play')
        play_color = 0
    premove_square = square
    premove_new_square = new_square

# End of Game
window.Element('-INSTRUCTION-').update(visible=False)
window.Element('-INPUT-').update(visible=False)
window.Element('-ENTER-').update(visible=False)
window.Element('-PLAY-').update('Game Over')
if play_color == 0:
    window.Element('-VALID-').update('Checkmate! Black Wins.', text_color='palegreen')
elif play_color == 1:
    window.Element('-VALID-').update('Checkmate! White Wins.', text_color='palegreen')

while True:
    event, values = window.read()
    if event == '-FLIP-':
        user_color = 1 - user_color
        img_board = display.position(BMN_next, user_color)
        img_board = display.oldnewsquares(img_board, square, new_square, user_color)
        img_board = display.kingincheck(img_board, BMN_next, play_color, user_color)
        img_board.resize(size).save('board.png')
        window.Element('-BOARD-').update('board.png')
    if event == Sg.WIN_CLOSED:
        print('Thank You for using Chess Compyuter.')
        print('FEN: ' + FEN)
        quit()
