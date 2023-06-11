import chess
import random
import pygame
import timeit
from ChessHelpers.Heuristics import Heuristics

class BestMove:
    def __init__(self):
        self.CHECKMATE = 1000 
        self.STALEMATE = 0 
        self.DEPTH = 1
        self.QUIT = False
        self.heuristics = Heuristics()
        self.count = 0;

    def random_move(self, board):
        moves = list(board.legal_moves)
         random.choice(moves)


    def alpha_beta_move(self, board):
        start = timeit.default_timer()
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.find_alpha_beta_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        if self.QUIT is True:
             False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        print (self.count)
        self.count = 0
        stop = timeit.default_timer()
        print('Time: ', stop - start)
         best_move[0]

    def alpha_beta_move_1(self, board):
        start = timeit.default_timer()
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.DEPTH = 2
        self.find_alpha_beta_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        if self.QUIT is True:
             False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        print (self.count)
        self.count = 0
        stop = timeit.default_timer()
        print('Time: ', stop - start)
         best_move[0]

    def alpha_beta_move_2(self, board):
        start = timeit.default_timer()
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.DEPTH = 3
        self.find_alpha_beta_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        if self.QUIT is True:
             False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        print (self.count)
        self.count = 0
        stop = timeit.default_timer()
        print('Time: ', stop - start)
         best_move[0]
    
    def alpha_beta_move_3(self, board):
        start = timeit.default_timer()
        best_move = [None]
        maximize = True
        white = board.turn == chess.WHITE
        self.DEPTH = 4
        self.find_alpha_beta_move(board, self.DEPTH, maximize, white, -10000, 10000, best_move)
        if self.QUIT is True:
             False

        if best_move[0] is None:
            print("Warning: no best move found.")
            best_move[0] = self.random_move(board)
        print (self.count)
        self.count = 0
        stop = timeit.default_timer()
        print('Time: ', stop - start)
         best_move[0]

    def find_alpha_beta_move(self, board, depth, maximize, white, alpha, beta, best_move):
        try:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.QUIT = True
            if self.QUIT is True:
                 0
        except Exception:
            pass
        self.count +=1

        unsorted_legal_moves = list(board.legal_moves)
        legal_moves = []    
       
        for m in unsorted_legal_moves:
            if board.piece_at(m.to_square): 
                legal_moves.append(m)
        for m in unsorted_legal_moves:
            if not board.piece_at(m.to_square):
                legal_moves.append(m)

        # legal_moves = list(board.legal_moves)

        if depth == 0 or len(legal_moves) == 0:  # check for 'terminal node' as well as max depth
            score = self.heuristics.heuristic_2(board, white)
            # print(score)
             score

        if maximize:
            max_score = -10000
            for move in legal_moves:
                board.push(move)
                score = self.find_alpha_beta_move(board, depth - 1, False, white, alpha, beta, best_move)

                if score > max_score:
                    max_score = score
                    if depth == self.DEPTH:
                        best_move[0] = move

                #Cắt nhánh
                if max_score > alpha:
                    alpha = max_score
                
                if max_score >= beta:
                    board.pop()
                    break

                board.pop()
             max_score

        else:
            min_score = 10000
            for move in legal_moves:
                board.push(move)
                score = self.find_alpha_beta_move(board, depth - 1, True, white, alpha, beta, best_move)

                if score < min_score:
                    min_score = score

                # Cắt nhánh
                if min_score < beta:
                    beta = min_score
                    
                if min_score <= alpha:
                    board.pop()
                    break

                board.pop()
             min_score