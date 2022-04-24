# Moving Pieces and Generating New Position

def newBMN(BMN, BMN_valid, square, new_square):

    BMN_next = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    error = 0
    square_column = ord(square[0]) - 97
    square_row = 8 - int(square[1])
    new_square_column = ord(new_square[0]) - 97
    new_square_row = 8 - int(new_square[1])
    for i in range(0, 8):
        for j in range(0, 8):
            BMN_next[i][j] = BMN[i][j]
            if i == new_square_row and j == new_square_column and (BMN_valid[i][j] == '●' or BMN_valid[i][j] == '○'):
                BMN_next[i][j] = BMN[square_row][square_column]
            elif i == new_square_row and j == new_square_column and (BMN_valid[i][j] != '●' or BMN_valid[i][j] != '○'):
                error = 1

    if error == 0:
        BMN_next[square_row][square_column] = ' '

    return error, BMN_next
