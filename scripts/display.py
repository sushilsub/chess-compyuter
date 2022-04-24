# Display Options for Chess Board

from PIL import Image

# Display Position given BMN
import checks


def position(BMN, user_color):

    width_board = 800
    height_board = 800
    width_square = int(width_board/8)
    height_square = int(height_board/8)

    # Create White Board
    img_board = Image.new(mode="RGB", size=(width_board, height_board), color=(255, 255, 255))

    # Load and Resize Pieces
    bB = Image.open('../pieces_png/bB.png')
    bB = bB.resize((100, 100))
    bK = Image.open('../pieces_png/bK.png')
    bK = bK.resize((100, 100))
    bN = Image.open('../pieces_png/bN.png')
    bN = bN.resize((100, 100))
    bP = Image.open('../pieces_png/bP.png')
    bP = bP.resize((100, 100))
    bQ = Image.open('../pieces_png/bQ.png')
    bQ = bQ.resize((100, 100))
    bR = Image.open('../pieces_png/bR.png')
    bR = bR.resize((100, 100))

    wB = Image.open('../pieces_png/wB.png')
    wB = wB.resize((100, 100))
    wK = Image.open('../pieces_png/wK.png')
    wK = wK.resize((100, 100))
    wN = Image.open('../pieces_png/wN.png')
    wN = wN.resize((100, 100))
    wP = Image.open('../pieces_png/wP.png')
    wP = wP.resize((100, 100))
    wQ = Image.open('../pieces_png/wQ.png')
    wQ = wQ.resize((100, 100))
    wR = Image.open('../pieces_png/wR.png')
    wR = wR.resize((100, 100))

    # Paste Position on Board
    compyuter_color = 1 - user_color
    for i in range(0, 8):
        i_user = (user_color * i) + (compyuter_color * (7 - i))
        for j in range(0, 8):
            j_user = (user_color * j) + (compyuter_color * (7 - j))
            # Define White Square
            img_square = Image.new(mode="RGB", size=(width_square, height_square), color=(255, 255, 255))

            # Determine Square Color
            if (i_user + j_user) % 2 == 1:
                img_square = Image.new(mode="RGB", size=(width_square, height_square), color=(119, 63, 26))
            if (i_user + j_user) % 2 == 0:
                img_square = Image.new(mode="RGB", size=(width_square, height_square), color=(238, 211, 164))

            # Add Black Pieces from BMN
            if BMN[i][j] == 'p':
                img_board.paste(img_square, (j_user*100, i_user*100))
                img_board.paste(bP, (j_user*100, i_user*100), bP.convert('RGBA'))
            if BMN[i][j] == 'n':
                img_board.paste(img_square, (j_user*100, i_user*100))
                img_board.paste(bN, (j_user*100, i_user*100), bN.convert('RGBA'))
            if BMN[i][j] == 'b':
                img_board.paste(img_square, (j_user*100, i_user*100))
                img_board.paste(bB, (j_user*100, i_user*100), bB.convert('RGBA'))
            if BMN[i][j] == 'r':
                img_board.paste(img_square, (j_user*100, i_user*100))
                img_board.paste(bR, (j_user*100, i_user*100), bR.convert('RGBA'))
            if BMN[i][j] == 'q':
                img_board.paste(img_square, (j_user*100, i_user*100))
                img_board.paste(bQ, (j_user*100, i_user*100), bQ.convert('RGBA'))
            if BMN[i][j] == 'k':
                img_board.paste(img_square, (j_user*100, i_user*100))
                img_board.paste(bK, (j_user*100, i_user*100), bK.convert('RGBA'))

            # Add White Pieces from BMN
            if BMN[i][j] == 'P':
                img_board.paste(img_square, (j_user * 100, i_user * 100))
                img_board.paste(wP, (j_user * 100, i_user * 100), wP.convert('RGBA'))
            if BMN[i][j] == 'N':
                img_board.paste(img_square, (j_user * 100, i_user * 100))
                img_board.paste(wN, (j_user * 100, i_user * 100), wN.convert('RGBA'))
            if BMN[i][j] == 'B':
                img_board.paste(img_square, (j_user * 100, i_user * 100))
                img_board.paste(wB, (j_user * 100, i_user * 100), wB.convert('RGBA'))
            if BMN[i][j] == 'R':
                img_board.paste(img_square, (j_user * 100, i_user * 100))
                img_board.paste(wR, (j_user * 100, i_user * 100), wR.convert('RGBA'))
            if BMN[i][j] == 'Q':
                img_board.paste(img_square, (j_user * 100, i_user * 100))
                img_board.paste(wQ, (j_user * 100, i_user * 100), wQ.convert('RGBA'))
            if BMN[i][j] == 'K':
                img_board.paste(img_square, (j_user * 100, i_user * 100))
                img_board.paste(wK, (j_user * 100, i_user * 100), wK.convert('RGBA'))

            # Add Vacant Squares from BMN
            if BMN[i][j] == ' ':
                img_board.paste(img_square, (j_user * 100, i_user * 100))

    # Load and Add Square Coordinate Indicators
    b1 = Image.open('../numbers_png/b1.png')
    b1.thumbnail((18, 18))
    b2 = Image.open('../numbers_png/b2.png')
    b2.thumbnail((18, 18))
    b3 = Image.open('../numbers_png/b3.png')
    b3.thumbnail((18, 18))
    b4 = Image.open('../numbers_png/b4.png')
    b4.thumbnail((18, 18))
    b5 = Image.open('../numbers_png/b5.png')
    b5.thumbnail((18, 18))
    b6 = Image.open('../numbers_png/b6.png')
    b6.thumbnail((18, 18))
    b7 = Image.open('../numbers_png/b7.png')
    b7.thumbnail((18, 18))
    b8 = Image.open('../numbers_png/b8.png')
    b8.thumbnail((18, 18))
    ba = Image.open('../numbers_png/ba.png')
    ba.thumbnail((18, 18))
    bb = Image.open('../numbers_png/bb.png')
    bb.thumbnail((18, 18))
    bc = Image.open('../numbers_png/bc.png')
    bc.thumbnail((18, 18))
    bd = Image.open('../numbers_png/bd.png')
    bd.thumbnail((18, 18))
    be = Image.open('../numbers_png/be.png')
    be.thumbnail((18, 18))
    bf = Image.open('../numbers_png/bf.png')
    bf.thumbnail((18, 18))
    bg = Image.open('../numbers_png/bg.png')
    bg.thumbnail((18, 18))
    bh = Image.open('../numbers_png/bh.png')
    bh.thumbnail((18, 18))
    w1 = Image.open('../numbers_png/w1.png')
    w1.thumbnail((18, 18))
    w2 = Image.open('../numbers_png/w2.png')
    w2.thumbnail((18, 18))
    w3 = Image.open('../numbers_png/w3.png')
    w3.thumbnail((18, 18))
    w4 = Image.open('../numbers_png/w4.png')
    w4.thumbnail((18, 18))
    w5 = Image.open('../numbers_png/w5.png')
    w5.thumbnail((18, 18))
    w6 = Image.open('../numbers_png/w6.png')
    w6.thumbnail((18, 18))
    w7 = Image.open('../numbers_png/w7.png')
    w7.thumbnail((18, 18))
    w8 = Image.open('../numbers_png/w8.png')
    w8.thumbnail((18, 18))
    wa = Image.open('../numbers_png/wa.png')
    wa.thumbnail((18, 18))
    wb = Image.open('../numbers_png/wb.png')
    wb.thumbnail((18, 18))
    wc = Image.open('../numbers_png/wc.png')
    wc.thumbnail((18, 18))
    wd = Image.open('../numbers_png/wd.png')
    wd.thumbnail((18, 18))
    we = Image.open('../numbers_png/we.png')
    we.thumbnail((18, 18))
    wf = Image.open('../numbers_png/wf.png')
    wf.thumbnail((18, 18))
    wg = Image.open('../numbers_png/wg.png')
    wg.thumbnail((18, 18))
    wh = Image.open('../numbers_png/wh.png')
    wh.thumbnail((18, 18))

    if user_color == 0:
        img_board.paste(bh, (0 + 2, 800 - 20), bh.convert('RGBA'))
        img_board.paste(bg, (100 + 2, 800 - 20), bg.convert('RGBA'))
        img_board.paste(bf, (200 + 2, 800 - 20), bf.convert('RGBA'))
        img_board.paste(be, (300 + 2, 800 - 20), be.convert('RGBA'))
        img_board.paste(bd, (400 + 2, 800 - 20), bd.convert('RGBA'))
        img_board.paste(bc, (500 + 2, 800 - 20), bc.convert('RGBA'))
        img_board.paste(bb, (600 + 2, 800 - 20), bb.convert('RGBA'))
        img_board.paste(ba, (700 + 2, 800 - 20), ba.convert('RGBA'))
        img_board.paste(b1, (800 - 12, 0 + 2), b1.convert('RGBA'))
        img_board.paste(b2, (800 - 12, 100 + 2), b2.convert('RGBA'))
        img_board.paste(b3, (800 - 12, 200 + 2), b3.convert('RGBA'))
        img_board.paste(b4, (800 - 12, 300 + 2), b4.convert('RGBA'))
        img_board.paste(b5, (800 - 12, 400 + 2), b5.convert('RGBA'))
        img_board.paste(b6, (800 - 12, 500 + 2), b6.convert('RGBA'))
        img_board.paste(b7, (800 - 12, 600 + 2), b7.convert('RGBA'))
        img_board.paste(b8, (800 - 12, 700 + 2), b8.convert('RGBA'))
    if user_color == 1:
        img_board.paste(wa, (0 + 2, 800 - 20), wa.convert('RGBA'))
        img_board.paste(wb, (100 + 2, 800 - 20), wb.convert('RGBA'))
        img_board.paste(wc, (200 + 2, 800 - 20), wc.convert('RGBA'))
        img_board.paste(wd, (300 + 2, 800 - 20), wd.convert('RGBA'))
        img_board.paste(we, (400 + 2, 800 - 20), we.convert('RGBA'))
        img_board.paste(wf, (500 + 2, 800 - 20), wf.convert('RGBA'))
        img_board.paste(wg, (600 + 2, 800 - 20), wg.convert('RGBA'))
        img_board.paste(wh, (700 + 2, 800 - 20), wh.convert('RGBA'))
        img_board.paste(w8, (800 - 12, 0 + 2), w8.convert('RGBA'))
        img_board.paste(w7, (800 - 12, 100 + 2), w7.convert('RGBA'))
        img_board.paste(w6, (800 - 12, 200 + 2), w6.convert('RGBA'))
        img_board.paste(w5, (800 - 12, 300 + 2), w5.convert('RGBA'))
        img_board.paste(w4, (800 - 12, 400 + 2), w4.convert('RGBA'))
        img_board.paste(w3, (800 - 12, 500 + 2), w3.convert('RGBA'))
        img_board.paste(w2, (800 - 12, 600 + 2), w2.convert('RGBA'))
        img_board.paste(w1, (800 - 12, 700 + 2), w1.convert('RGBA'))

    return img_board


# Display Board with Valid Squares for Select Piece given BMN_valid
def valid(img_board, BMN_valid, user_color):
    # Load and Resize Move and Capture Symbols
    move = Image.open('../display_png/move.png')
    move = move.resize((100, 100))
    capture = Image.open('../display_png/capture.png')
    capture = capture.resize((100, 100))
    select = Image.open('../display_png/select.png')
    select = select.resize((100, 100))

    compyuter_color = 1 - user_color
    for i in range(0, 8):
        i_user = (user_color * i) + (compyuter_color * (7 - i))
        for j in range(0, 8):
            j_user = (user_color * j) + (compyuter_color * (7 - j))

            # Add Move and Capture Symbols; Add Highlight
            if BMN_valid[i][j] == '●':
                img_board.paste(move, (j_user * 100, i_user * 100), move.convert('RGBA'))
            if BMN_valid[i][j] == '○':
                img_board.paste(capture, (j_user * 100, i_user * 100), capture.convert('RGBA'))
            if BMN_valid[i][j] == '■':
                img_board.paste(select, (j_user * 100, i_user * 100), select.convert('RGBA'))

    return img_board


# Display Board with Old and New Squares Marked
def oldnewsquares(img_board, square, new_square, user_color):
    # Load and Resize Move and Capture Symbols
    oldnew = Image.open('../display_png/oldnew.png')
    oldnew = oldnew.resize((100, 100))

    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    new_square_column = ord(new_square[0]) - 97
    new_square_row = 8 - int(new_square[1])

    compyuter_color = 1 - user_color

    # Add Highlight to Old Square
    i_user = (user_color * square_row) + (compyuter_color * (7 - square_row))
    j_user = (user_color * square_column) + (compyuter_color * (7 - square_column))
    img_board.paste(oldnew, (j_user * 100, i_user * 100), oldnew.convert('RGBA'))

    # Add Highlight to Old Square
    i_user = (user_color * new_square_row) + (compyuter_color * (7 - new_square_row))
    j_user = (user_color * new_square_column) + (compyuter_color * (7 - new_square_column))
    img_board.paste(oldnew, (j_user * 100, i_user * 100), oldnew.convert('RGBA'))

    return img_board


# Display King Square as Check if Attacked
def kingincheck(img_board, BMN, play_color, user_color):
    # Load and Resize Move and Capture Symbols
    check = Image.open('../display_png/check.png')
    check = check.resize((100, 100))

    kingcheck = 0
    i_king = 0
    j_king = 0
    compyuter_color = 1 - user_color
    for i in range(0, 8):
        for j in range(0, 8):
            if (BMN[i][j] == 'k' or BMN[i][j] == 'K') and (BMN[i][j].isupper() != play_color):
                i_king = i
                j_king = j
                square_king = chr(97 + j_king) + str(8 - i_king)
                if checks.squareattacked(BMN, square_king, play_color) == 1:
                    kingcheck = 1

    if kingcheck == 1:
        i_user = (user_color * i_king) + (compyuter_color * (7 - i_king))
        j_user = (user_color * j_king) + (compyuter_color * (7 - j_king))
        img_board.paste(check, (j_user * 100, i_user * 100), check.convert('RGBA'))

    return img_board

