import chess
from Interface.gui import play_chess
from ChessHelpers import AlphaBetaMove

def main():
    board = chess.Board()
    move_generator = AlphaBetaMove.BestMove()
    play_chess(board, black = move_generator.alpha_beta_move)
    #play_chess(board,white = move_generator.alpha_beta_move)
    #play_chess(board, black = move_generator.alpha_beta_move,white = move_generator.alpha_beta_move)
if __name__ == '__main__':
    main()
