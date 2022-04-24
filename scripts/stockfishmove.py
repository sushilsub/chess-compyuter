from stockfish import Stockfish


def stockfishmove(FEN, play_color, level):
    skill_level = 0
    depth_comp = 0
    max_time = 0
    color_char = 'w'

    match play_color:
        case 0: color_char = 'b'
        case 1: color_char = 'w'

    match level:
        case 1:
            skill_level = -9
            depth_comp = 5
            max_time = 50
        case 2:
            skill_level = -5
            depth_comp = 5
            max_time = 100
        case 3:
            skill_level = -1
            depth_comp = 5
            max_time = 150
        case 4:
            skill_level = 3
            depth_comp = 5
            max_time = 200
        case 5:
            skill_level = 7
            depth_comp = 5
            max_time = 300
        case 6:
            skill_level = 11
            depth_comp = 8
            max_time = 400
        case 7:
            skill_level = 16
            depth_comp = 13
            max_time = 500
        case 8:
            skill_level = 20
            depth_comp = 22
            max_time = 1000

    stockfish = Stockfish(path="..\\stockfish_14.1_win_x64_avx2\\stockfish_14.1_win_x64_avx2.exe", depth=depth_comp, parameters={"Skill Level": skill_level})
    stockfish.get_best_move_time(max_time)
    FEN_full = FEN + ' ' + color_char + ' - - 0 1'
    stockfish.set_fen_position(FEN_full)
    best_move = stockfish.get_best_move()

    return best_move
