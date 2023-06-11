import chess
global best_move


class Heuristics:
    def __init__(self):
        self.CHECKMATE = 1000
        self.STALEMATE = 0
        self.piece_score = {"k": 0, "q": 8.8, "r": 5.1, "b": 3.33, "n": 3.2, "p": 1}

    def heuristic_1(self, board, white):
        if board.is_checkmate() and (white and board.turn == chess.BLACK or
                                     not white and board.turn == chess.WHITE):
             self.CHECKMATE

        if board.is_checkmate() and (not white and board.turn == chess.BLACK or
                                     white and board.turn == chess.WHITE):
             -self.CHECKMATE

        if board.is_stalemate():
             self.STALEMATE

         self.calculate_score(board, white)

    def calculate_score(self, board, white):
        chess_board = MakeMatrix().convert_to_matrix(board)
        score = 0
        for row in chess_board:
            for cell in row:
                color = cell[0]
                piece_type = cell[1]
                if color == "w":
                    score += self.piece_score[piece_type]
                elif color == "b":
                    score -= self.piece_score[piece_type]

        if white is False:
            score = -score
         score

        
    def heuristic_2(self, board, white):

        score = self.heuristic_1(board, white) + self.advance_score(board, white)

         score

    
    def advance_score(self, board, white):
        
        knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                         [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                         [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                         [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                         [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                         [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                         [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                         [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

        bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

        rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

        queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

        pawn_scores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

        piece_position_scores = {("w","n"): knight_scores,
                         ("b","n"): knight_scores[::-1],
                         ("w","b"): bishop_scores,
                         ("b","b"): bishop_scores[::-1],
                         ("w","q"): queen_scores,
                         ("b","q"): queen_scores[::-1],
                         ("w","r"): rook_scores,
                         ("b","r"): rook_scores[::-1],
                         ("w","p"): pawn_scores,
                         ("b","p"): pawn_scores[::-1]}

        chess_board = MakeMatrix().convert_to_matrix(board)
        score = 0
        
        for row in range(0,8):
            for col in range(0,8):
                piece = chess_board[row][col]
                if piece != '--' and piece[1] != 'k':
                    if piece[0] == 'w':
                        score += piece_position_scores[piece][row][col]
                    elif piece[0] == 'b':
                        score -= piece_position_scores[piece][row][col]                
        
        if white is False:
            score = -score
         score

                    

class MakeMatrix:

    def __init__(self):
        self.board_mat = []

    def convert_to_matrix(self, board):
        board_str = board.epd()
        rows = board_str.split(" ", 1)[0].split("/")
        for row in rows:
            board_row = []
            for cell in row:
                if cell.isdigit():
                    for i in range(0, int(cell)):
                        board_row.append('--')
                else:
                    if cell.islower():  # black
                        board_row.append(("b", cell))
                    else:  # white
                        board_row.append(("w", cell.lower()))
            self.board_mat.append(board_row)
         self.board_mat
