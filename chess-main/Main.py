import chess
# from ChessHelpers import ChessAI
from Interface.gui import play_chess
from ChessHelpers import ChessEngineHelper


CHECKMATE = 1000
STALEMATE = 0

def main():
    board = chess.Board()
    move_generator = ChessEngineHelper.MoveGenerator()
    play_chess(board, black = move_generator.mini_max_move)
if __name__ == '__main__':
    main()
