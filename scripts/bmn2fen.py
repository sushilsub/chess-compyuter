# BMN to FEN Conversion

def bmn2fen(BMN):
    FEN = ''
    for i in range(0, 8):
        count = 0
        for j in range(0, 8):
            if BMN[i][j] == ' ':
                count = count + 1
            elif not BMN[i][j].isnumeric():
                if count == 0:
                    FEN = FEN + BMN[i][j]
                else:
                    FEN = FEN + str(count) + BMN[i][j]
                    count = 0
        if count != 0:
            FEN = FEN + str(count)
        if i != 7:
            FEN = FEN + '/'

    return FEN
