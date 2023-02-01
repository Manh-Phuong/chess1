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
            return self.CHECKMATE

        if board.is_checkmate() and (not white and board.turn == chess.BLACK or
                                     white and board.turn == chess.WHITE):
            return -self.CHECKMATE

        if board.is_stalemate():
            return self.STALEMATE

        return self.calculate_score(board, white)

    def calculate_score(self, board, white):
        chess_board = MakeMatrix().convert_to_matrix(board)
        score = 0
        count_black = 0
        count_white = 0
        for row in chess_board:
            for cell in row:
                color = cell[0]
                piece_type = cell[1]
                if color == "w":
                    count_white += 1
                    score += self.piece_score[piece_type]
                elif color == "b":
                    count_black += 1
                    score -= self.piece_score[piece_type]

        if white is False:
            score = -score
        return score

        

    '''def heuristic_2(self, board, white):
        score = self.heuristic_1(board, white)

        score += self.control_diagonals(board, white) / 5
        score += self.control_center(board, white) / 4
        return score

   
    def control_diagonals(self, board, white):
    
        diagonal_figures = ["b", "q"]

        diagonal_heuristics = 0

        chess_board = MakeMatrix().convert_to_matrix(board)

        black_diagonal = [chess_board[1][1], chess_board[2][2], chess_board[3][3], chess_board[4][4],
                          chess_board[5][5], chess_board[6][6], chess_board[7][7], chess_board[0][0]]

        white_diagonal = [chess_board[0][7], chess_board[1][6], chess_board[2][5], chess_board[3][4],
                          chess_board[4][3], chess_board[5][2], chess_board[6][1], chess_board[7][0]]

        for cell in black_diagonal:
            for figure in diagonal_figures:
                if figure == cell[1]:
                    if (cell[0] == "w" and white) or (cell[0] == "b" and not white):
                        diagonal_heuristics += 3
        for cell in white_diagonal:
            for figure in diagonal_figures:
                if figure == cell[1]:
                    if (cell[0] == "w" and white) or (cell[0] == "b" and not white):
                        diagonal_heuristics += 3

        return diagonal_heuristics'''
  
  
    def heuristic_2(self, board, white):
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
        score = self.calculate_score(board, white)
        
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
        
        return score

    
    def control_center(self, board, white):
        # This procedure will give heuristic points for control of central squares

        # Convert board
        chess_board = MakeMatrix().convert_to_matrix(board)

        # define central squares: e4, e5, d4, d5
        central_squares = [chess_board[4][4], chess_board[4][5], chess_board[5][4], chess_board[5][5]]

        # Define squares can be used to control central squares by pawns
        white_pawn_squares = [chess_board[3][3], chess_board[4][3], chess_board[5][3], chess_board[6][3],
                              chess_board[4][3], chess_board[4][4], chess_board[4][5], chess_board[4][6]]

        black_pawn_squares = [chess_board[3][6], chess_board[4][6], chess_board[5][6], chess_board[6][6],
                              chess_board[3][5], chess_board[4][5], chess_board[5][5], chess_board[5][6]]

        # Define squares can be used to control central squares by knights
        knight_squares = [chess_board[3][2], chess_board[4][2], chess_board[5][2], chess_board[6][2],
                          chess_board[2][3], chess_board[3][3], chess_board[6][3], chess_board[7][3],
                          chess_board[2][4], chess_board[7][4], chess_board[2][5], chess_board[7][5],
                          chess_board[2][6], chess_board[3][6], chess_board[6][6], chess_board[7][6],
                          chess_board[3][7], chess_board[4][7], chess_board[5][7], chess_board[6][7]]

        # Set control center heuristics to 0
        ccHeuristic = 0

        # Give points for each piece in central square (pawn or knight)

        for square in central_squares:
            if square[1] == "p" and square[0] == "b":
                ccHeuristic += 1
            elif square[1] == "n" and square[0] == "b":
                ccHeuristic += 2
            elif square[1] == "b" and square[0] == "b":
                ccHeuristic += 2
            elif square[1] == "r" and square[0] == "b":
                ccHeuristic += 2
            elif square[1] == "q" and square[0] == "b":
                ccHeuristic += 3
            elif square[1] == "k" and square[0] == "b":
                ccHeuristic += 2

        # # Give points for white pawns in controlling positions
        # if white:
        #     for square in white_pawn_squares:
        #         if square == "p":
        #             ccHeuristic += 1

        # # Give points for black pawns in controlling positions
        # if not white:
        #     for square in black_pawn_squares:
        #         if square == "p":
        #             ccHeuristic += 1

        # Give points for knights controlling central squares

        for square in knight_squares:
            if square[1] == "n" and square[0] == "b":
                ccHeuristic += 2

        return ccHeuristic

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
                    if cell.islower(): 
                        board_row.append(("b", cell))
                    else:  
                        board_row.append(("w", cell.lower()))
            self.board_mat.append(board_row)
        return self.board_mat
