# FEN to BMN Conversion

def fen2bmn(FEN):
    # FEN to Board Matrix Notation (BMN) Conversion
    BMN = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    FEN_len = len(FEN)
    i = 0
    j = 0
    for m in range(0, FEN_len):
        if FEN[m] == '/':
            i = i + 1
            j = 0
        elif FEN[m] == '1' or FEN[m] == '2' or FEN[m] == '3' or FEN[m] == '4' or FEN[m] == '5' or FEN[m] == '6' or FEN[m] == '7' or FEN[m] == '8':
            for k in range(j, int(FEN[m]) + j):
                BMN[i][k] = ' '
            j = j + int(FEN[m])
        else:
            BMN[i][j] = FEN[m]
            j = j + 1

    return BMN
