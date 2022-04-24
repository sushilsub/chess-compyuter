# Various Checks

import rules

# Check if Square is Attacked
def squareattacked(BMN, square, color):
    attacked = 0
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    for i in range(0, 8):
        for j in range(0, 8):
            if BMN[i][j] != ' ' and BMN[i][j].isupper() == color:
                piece_square = chr(97 + j) + str(8 - i)
                BMN_valid_noking_nopawn = rules.selectedsquare_noking_nopawn(BMN, piece_square)
                if BMN_valid_noking_nopawn[square_row][square_column] == '●' or BMN_valid_noking_nopawn[square_row][square_column] == '○':
                    attacked = 1
                BMN_valid_pawn = rules.pawn(BMN, piece_square)
                if BMN_valid_pawn[square_row][square_column] == '✕' or BMN_valid_pawn[square_row][square_column] == '○':
                    attacked = 1

    return attacked


# Check if Square has King Adjacent to it
def adjacentking(BMN, square, color):
    adjacent = 0
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])

    # Check Squares
    i_valid = square_row + 1
    j_valid = square_column + 1
    if (i_valid <= 7) and (j_valid <= 7):
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row
    j_valid = square_column + 1
    if j_valid <= 7:
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row - 1
    j_valid = square_column + 1
    if (i_valid >= 0) and (j_valid <= 7):
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row + 1
    j_valid = square_column
    if i_valid <= 7:
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row - 1
    j_valid = square_column
    if i_valid >= 0:
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row + 1
    j_valid = square_column - 1
    if (i_valid <= 7) and (j_valid >= 0):
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row
    j_valid = square_column - 1
    if j_valid >= 0:
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    i_valid = square_row - 1
    j_valid = square_column - 1
    if (i_valid >= 0) and (j_valid >= 0):
        if (BMN[i_valid][j_valid] == 'k' or BMN[i_valid][j_valid] == 'K') and BMN[i_valid][j_valid].isupper() == color:
            adjacent = 1

    return adjacent


# Check if the Square Selected is Valid
def validsquareselected(BMN, square, play_color):
    valid = 1
    continue_checks = 0
    if len(square) != 2:
        valid = 0
    elif not square[1].isnumeric():
        valid = 0
    elif square[0].isnumeric():
        valid = 0
    else:
        continue_checks = 1

    if continue_checks == 1:
        square_column = ord(square[0]) - 97
        square_row = 8 - int(square[1])
        if BMN[square_row][square_column] == ' ':
            valid = 0
        elif BMN[square_row][square_column].isupper() != play_color:
            valid = 0
        elif square_column > 7 or square_column < 0 or square_row > 7 or square_row < 0:
            valid = 0

    return valid


# Check if the Selected Piece has any Valid Moves
def novalidmoves(BMN_valid):
    valid = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if BMN_valid[i][j] == '●' or BMN_valid[i][j] == '○':
                valid = 1
                continue

    return valid


# Check if the New Square Selected has a Typo
def validnewsquaretypo(square):
    valid = 1
    continue_checks = 0
    if len(square) != 2:
        valid = 0
    elif not square[1].isnumeric():
        valid = 0
    elif square[0].isnumeric():
        valid = 0
    else:
        continue_checks = 1

    if continue_checks == 1:
        square_column = ord(square[0]) - 97
        square_row = 8 - int(square[1])
        if square_column > 7 or square_column < 0 or square_row > 7 or square_row < 0:
            valid = 0

    return valid
