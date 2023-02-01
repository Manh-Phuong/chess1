import chess
import random
import pygame
from ChessHelpers.ChessHeuristics import Heuristics

class MoveGenerator:
    def __init__(self):
        self.CHECKMATE = 1000 
        self.STALEMATE = 0 
        self.DEPTH = 1
        self.QUIT = False
        self.heuristics = Heuristics()

    def random_move(self, board):
        moves = list(board.legal_moves)
        return random.choice(moves)


    def mini_max_move(self, board):
        best_move = [None]
    
        maximize = True
        white = board.turn == chess.WHITE
        # print(white)
        self.find_mini_max_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        print(self.DEPTH)
        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        return best_move[0]

    def mini_max_move_1(self, board):
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.DEPTH = 2
        self.find_mini_max_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        print(self.DEPTH)
        if self.QUIT is True:
            return False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        return best_move[0]
    
    def mini_max_move_2(self, board):
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.DEPTH = 3
        self.find_mini_max_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        print(self.DEPTH)
        if self.QUIT is True:
            return False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        return best_move[0]
    
    def mini_max_move_3(self, board):
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.DEPTH = 4
        self.find_mini_max_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        print(self.DEPTH)
        if self.QUIT is True:
            return False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        return best_move[0]

    def find_mini_max_move(self, board, depth, maximize, white, alpha, beta, best_move):
        try:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.QUIT = True
            if self.QUIT is True:
                return 0
        except Exception:
            pass

        legal_moves = list(board.legal_moves)

        if depth == 0 or len(legal_moves) == 0:  # check for 'terminal node' as well as max depth
            score = self.heuristics.heuristic_2(board, white)
            # print(score)
            return score

        if maximize:
            max_score = -10000
            for move in legal_moves:
                board.push(move)
                score = self.find_mini_max_move(board, depth - 1, False, white, alpha, beta, best_move)

                if score > max_score:
                    max_score = score
                    if depth == self.DEPTH:
                        best_move[0] = move

                # pruning
                # update "minimum guaranteed score"
                if max_score > alpha:
                    alpha = max_score
                # pruning
                # skip if move is better than best move opponent will allow
                if max_score >= beta:
                    board.pop()
                    break

                board.pop()
            return max_score

        else:
            min_score = 10000
            for move in legal_moves:
                board.push(move)
                score = self.find_mini_max_move(board, depth - 1, True, white, alpha, beta, best_move)

                if score < min_score:
                    min_score = score

                # pruning: update beta value
                if min_score < beta:
                    beta = min_score

                # pruning
                # skip if worse than the worst score we can be forced to accept
                if min_score <= alpha:
                    board.pop()
                    break

                board.pop()
            return min_score