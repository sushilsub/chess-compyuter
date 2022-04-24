# Rules for Piece Movement

import checks
import newposition


# Piece (Toplevel)
def selectedsquare(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    # Check for Piece from BMN
    if piece == 'k' or piece == 'K':
        BMN_valid_nocheck = king(BMN, square)
    elif piece == 'p' or piece == 'P':
        BMN_valid_nocheck = pawn(BMN, square)
    else:
        BMN_valid_nocheck = selectedsquare_noking_nopawn(BMN, square)

    # Detect Square of the King
    square_king = 'a1'
    for i in range(0, 8):
        for j in range(0, 8):
            if (BMN[i][j] == 'k' and piece.isupper() == 0) or (BMN[i][j] == 'K' and piece.isupper() == 1):
                i_king = i
                j_king = j
                square_king = chr(97 + j_king) + str(8 - i_king)

    # If King in Check after move see which move by selected piece not possible
    BMN_valid = BMN_valid_nocheck

    for i in range(0, 8):
        for j in range(0, 8):
            if BMN_valid_nocheck[i][j] == '●' or BMN_valid_nocheck[i][j] == '○':
                new_square = chr(97 + j) + str(8 - i)
                error_temp, BMN_temp = newposition.newBMN(BMN, BMN_valid_nocheck, square, new_square)
                if piece == 'k' or piece == 'K':
                    kingcheckagain = checks.squareattacked(BMN_temp, new_square, piece.islower())
                else:
                    kingcheckagain = checks.squareattacked(BMN_temp, square_king, piece.islower())
                if kingcheckagain == 1:
                    BMN_valid[i][j] = ' '

    return BMN_valid


# Piece (Toplevel no King no Pawn)
def selectedsquare_noking_nopawn(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check for Piece from BMN
    if piece == 'n' or piece == 'N':
        BMN_valid = knight(BMN, square)
    if piece == 'b' or piece == 'B':
        BMN_valid = bishop(BMN, square)
    if piece == 'r' or piece == 'R':
        BMN_valid = rook(BMN, square)
    if piece == 'q' or piece == 'Q':
        BMN_valid = queen(BMN, square)

    return BMN_valid


# Bishop
def bishop(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check South-East Diagonals
    i_valid = square_row + 1
    j_valid = square_column + 1
    while (i_valid <= 7) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        i_valid = i_valid + 1
        j_valid = j_valid + 1

    # Check North-West Diagonals
    i_valid = square_row - 1
    j_valid = square_column - 1
    while (i_valid >= 0) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        i_valid = i_valid - 1
        j_valid = j_valid - 1

    # Check South-West Diagonals
    i_valid = square_row + 1
    j_valid = square_column - 1
    while (i_valid <= 7) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        i_valid = i_valid + 1
        j_valid = j_valid - 1

    # Check North-East Diagonals
    i_valid = square_row - 1
    j_valid = square_column + 1
    while (i_valid >= 0) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        i_valid = i_valid - 1
        j_valid = j_valid + 1

    # Mark Square with Piece
    BMN_valid[square_row][square_column] = '■'

    return BMN_valid


# Knight
def knight(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check Squares
    i_valid = square_row + 2
    j_valid = square_column + 1
    if (i_valid <= 7) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 2
    j_valid = square_column + 1
    if (i_valid >= 0) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row + 1
    j_valid = square_column + 2
    if (i_valid <= 7) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 1
    j_valid = square_column + 2
    if (i_valid >= 0) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row + 2
    j_valid = square_column - 1
    if (i_valid <= 7) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 2
    j_valid = square_column - 1
    if (i_valid >= 0) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row + 1
    j_valid = square_column - 2
    if (i_valid <= 7) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 1
    j_valid = square_column - 2
    if (i_valid >= 0) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'

    # Mark Square with Piece
    BMN_valid[square_row][square_column] = '■'

    return BMN_valid


# Rook
def rook(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check South on Column
    i_valid = square_row + 1
    j_valid = square_column
    while i_valid <= 7:
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        i_valid = i_valid + 1

    # Check North on Column
    i_valid = square_row - 1
    j_valid = square_column
    while i_valid >= 0:
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        i_valid = i_valid - 1

    # Check West on Row
    i_valid = square_row
    j_valid = square_column + 1
    while j_valid <= 7:
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        j_valid = j_valid + 1

    # Check East on Column
    i_valid = square_row
    j_valid = square_column - 1
    while j_valid >= 0:
        if BMN[i_valid][j_valid] == ' ':
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
            BMN_valid[i_valid][j_valid] = '○'
            break
        if BMN[i_valid][j_valid] != ' ':
            break
        j_valid = j_valid - 1

    # Mark Square with Piece
    BMN_valid[square_row][square_column] = '■'

    return BMN_valid


# Queen
def queen(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check Bishop Rules
    if piece == 'q':
        BMN[square_row][square_column] = 'b'
    elif piece == 'Q':
        BMN[square_row][square_column] = 'B'
    BMN_valid_bishop = bishop(BMN, square)

    # Check Rook Rules
    if piece == 'q':
        BMN[square_row][square_column] = 'r'
    elif piece == 'Q':
        BMN[square_row][square_column] = 'R'
    BMN_valid_rook = rook(BMN, square)

    # Combine Rules
    if piece == 'q':
        BMN[square_row][square_column] = 'q'
    elif piece == 'Q':
        BMN[square_row][square_column] = 'Q'
    for i in range(0, 8):
        for j in range(0, 8):
            if BMN_valid_bishop[i][j] == '●' or BMN_valid_rook[i][j] == '●':
                BMN_valid[i][j] = '●'
            if BMN_valid_bishop[i][j] == '○' or BMN_valid_rook[i][j] == '○':
                BMN_valid[i][j] = '○'

    # Mark Square with Piece
    BMN_valid[square_row][square_column] = '■'

    return BMN_valid


# Pawn
def pawn(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check Squares for Black Pawns
    if piece == 'p':
        i_valid = square_row + 1
        j_valid = square_column
        if i_valid <= 7:
            if BMN[i_valid][j_valid] == ' ':
                BMN_valid[i_valid][j_valid] = '●'

        i_valid = square_row + 1
        j_valid = square_column + 1
        if (i_valid <= 7) and (j_valid <= 7):
            if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
                BMN_valid[i_valid][j_valid] = '○'
            else:
                BMN_valid[i_valid][j_valid] = '✕'

        i_valid = square_row + 1
        j_valid = square_column - 1
        if (i_valid <= 7) and (j_valid >= 0):
            if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
                BMN_valid[i_valid][j_valid] = '○'
            else:
                BMN_valid[i_valid][j_valid] = '✕'

        if square_row == 1:
            i_valid = square_row + 2
            j_valid = square_column
            if BMN[i_valid][j_valid] == ' ' and BMN[i_valid - 1][j_valid] == ' ':
                BMN_valid[i_valid][j_valid] = '●'

    # Check Squares for White Pawns
    if piece == 'P':
        i_valid = square_row - 1
        j_valid = square_column
        if i_valid >= 0:
            if BMN[i_valid][j_valid] == ' ':
                BMN_valid[i_valid][j_valid] = '●'

        i_valid = square_row - 1
        j_valid = square_column + 1
        if (i_valid >= 0) and (j_valid <= 7):
            if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
                BMN_valid[i_valid][j_valid] = '○'
            else:
                BMN_valid[i_valid][j_valid] = '✕'

        i_valid = square_row - 1
        j_valid = square_column - 1
        if (i_valid >= 0) and (j_valid >= 0):
            if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper():
                BMN_valid[i_valid][j_valid] = '○'
            else:
                BMN_valid[i_valid][j_valid] = '✕'

        if square_row == 6:
            i_valid = square_row - 2
            j_valid = square_column
            if BMN[i_valid][j_valid] == ' ' and BMN[i_valid + 1][j_valid] == ' ':
                BMN_valid[i_valid][j_valid] = '●'

    # Mark Square with Piece
    BMN_valid[square_row][square_column] = '■'

    return BMN_valid


# King
def king(BMN, square):
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    piece = BMN[square_row][square_column]

    BMN_valid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check Squares
    i_valid = square_row + 1
    j_valid = square_column + 1
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if (i_valid <= 7) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row
    j_valid = square_column + 1
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if j_valid <= 7:
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 1
    j_valid = square_column + 1
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if (i_valid >= 0) and (j_valid <= 7):
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row + 1
    j_valid = square_column
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if i_valid <= 7:
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 1
    j_valid = square_column
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if i_valid >= 0:
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row + 1
    j_valid = square_column - 1
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if (i_valid <= 7) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row
    j_valid = square_column - 1
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if j_valid >= 0:
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    i_valid = square_row - 1
    j_valid = square_column - 1
    move_square = chr(97 + j_valid) + str(8 - i_valid)
    if (i_valid >= 0) and (j_valid >= 0):
        if BMN[i_valid][j_valid] == ' ' and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '●'
        if BMN[i_valid][j_valid] != ' ' and piece.isupper() != BMN[i_valid][j_valid].isupper() and checks.squareattacked(BMN, move_square, piece.islower()) == 0 and checks.adjacentking(BMN, move_square, piece.islower()) == 0:
            BMN_valid[i_valid][j_valid] = '○'

    # Mark Square with Piece
    BMN_valid[square_row][square_column] = '■'

    return BMN_valid
