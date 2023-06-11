import sys
import os
import pygame
import chess
from Interface.button import Button
from ChessHelpers import AlphaBetaMove

TILE_SIZE = 64
BORDER = 10
INFO_HEIGHT = 100
BOARD_POS = (BORDER, BORDER)
COLOR_DARK = "#6fa3d5"
COLOR_LIGHT = "#edf2fa"
COLOR_BG = (22, 21, 18)
COLOR_DRAW_LINE = (22, 21, 18)
COLOR_DRAW_SELECT = (220, 10, 0, 50)
COLOR_DRAW_DRAG = (0, 220, 0, 50)
ENABLE_ILLEGAL_MOVES = False  
IMAGE_PATH = "chess-main/Assets/images/"

BG = pygame.image.load("chess-main/Assets/Background.png")
def get_font(size):
     pygame.font.Font("chess-main/Assets/font.ttf", size)     


def create_board_surface():
    board_surface = pygame.Surface((TILE_SIZE*8, TILE_SIZE*8))
    dark = False
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(board_surface, pygame.Color(COLOR_DARK if dark else COLOR_LIGHT), rect)
            dark = not dark
        dark = not dark
     board_surface


def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(BOARD_POS)
    x, y = [int(v // TILE_SIZE) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0:
             board[y][x], x, y
    except IndexError:
        pass
     None, None, None


def create_board_from_fen(fen):
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)
    col = 0
    row = 0
    for f in fen:
        if f == '/':
            col = col + 1
            row = 0
        elif f in ('1', '2', '3', '4', '5', '6', '7', '8'):
            row = row + int(f)
        elif f in ('K', 'k', 'Q', 'q', 'R', 'r', 'N', 'n', 'B', 'b', 'P', 'p'):
            board[int(col)][row] = get_piece(f)  
            row = row + 1
     board


def get_piece(f):
    if f == 'K':
         'white', 'king'
    elif f == 'k':
         'black', 'king'
    elif f == 'Q':
         'white', 'queen'
    elif f == 'q':
         'black', 'queen'
    elif f == 'R':
         'white', 'rook'
    elif f == 'r':
         'black', 'rook'
    elif f == 'N':
         'white', 'knight'
    elif f == 'n':
         'black', 'knight'
    elif f == 'B':
         'white', 'bishop'
    elif f == 'b':
         'black', 'bishop'
    elif f == 'P':
         'white', 'pawn'
    elif f == 'p':
         'black', 'pawn'


def draw_pieces(screen, board, font, selected_piece):
    sx, sy = None, None
    if selected_piece:
        piece, sx, sy = selected_piece

    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece:
                selected = x == sx and y == sy
                color, piece_type = piece
                s1 = pygame.image.load(resource_path(IMAGE_PATH + color + "/" + piece_type + ".png")).convert_alpha()
                s2 = pygame.image.load(resource_path(IMAGE_PATH + color + "/" + piece_type + ".png")).convert_alpha()
                if selected:
                    s2.fill((255, 255, 255, 90), None, pygame.BLEND_RGBA_MULT)
                    s1.fill((255, 255, 255, 90), None, pygame.BLEND_RGBA_MULT)
                pos = pygame.Rect(BOARD_POS[0] + x*TILE_SIZE + 1, BOARD_POS[1] + y*TILE_SIZE + 1, TILE_SIZE, TILE_SIZE)
                screen.blit(s2, s2.get_rect(center=pos.center).move(1, 1))
                screen.blit(s1, s1.get_rect(center=pos.center))


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

     os.path.join(base_path, relative_path)


def draw_selector(screen, piece, x, y):
    if piece is not None:
        rect = (BOARD_POS[0] + x * TILE_SIZE, BOARD_POS[1] + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, COLOR_DRAW_SELECT, rect, 3)


def draw_drag(screen, board, selected_piece, font):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x is not None:
            rect = (BOARD_POS[0] + x * TILE_SIZE, BOARD_POS[1] + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, COLOR_DRAW_DRAG, rect, 3)

        color, piece_type = selected_piece[0]
        s1 = pygame.image.load(resource_path(IMAGE_PATH + color + "/" + piece_type + ".png")).convert_alpha()
        s2 = pygame.image.load(resource_path(IMAGE_PATH + color + "/" + piece_type + ".png")).convert_alpha()

         x, y


pygame.init()
REPLAY_MOUSE_POS = pygame.mouse.get_pos()
REPLAY_BUTTON = Button(image=pygame.image.load("chess-main/Assets/back3.png"), pos=(271, 590), 
                            text_input="REPLAY", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
                    
for button in [REPLAY_BUTTON]:
    button.changeColor(REPLAY_MOUSE_POS)
    #button.update(screen) 

def draw_info(screen, chess_board, font):
    last_move_w = "White: "
    last_move_b = "Black: "
    ply = chess_board.ply()
    turn = chess_board.turn
                    
    #for button in [REPLAY_BUTTON]:
        #button.changeColor(REPLAY_MOUSE_POS)
        #button.update(screen)              
       
    if turn == chess.BLACK:
        last_move_b += chess_board.move_stack[ply - 2].uci()
        last_move_w += chess_board.peek().uci()
    else:
        if ply < 2:
            last_move_w += "None"
            last_move_b += "None"
        else:
            last_move_w += chess_board.move_stack[ply - 2].uci()
            last_move_b += chess_board.peek().uci()

    black_win = white_win = checkmate = ""
    outcome = chess_board.outcome()
    if outcome is not None:
        if outcome.winner is None:
            white_win = "Draw"
            black_win = "Draw"
            button.update(screen)
        elif outcome.winner == chess.WHITE:
            white_win = "White wins!"
            #checkmate = "Checkmate"
            button.update(screen)
        else:
            black_win = "Black wins!"
            #checkmate = "Checkmate"
            button.update(screen)


    s1 = font.render(last_move_w, True, pygame.Color(COLOR_LIGHT))
    s2 = font.render(last_move_b, True, pygame.Color(COLOR_DARK))
    s3 = font.render(white_win, True, pygame.Color(COLOR_DRAW_DRAG))
    s4 = font.render(black_win, True, pygame.Color(COLOR_DRAW_SELECT))
    s5 = font.render(checkmate, True, pygame.Color('white'))

    pos1 = pygame.Rect(BORDER, BORDER*3 + TILE_SIZE*8, TILE_SIZE*8, INFO_HEIGHT)
    pos2 = pygame.Rect(BORDER, BORDER*3 + TILE_SIZE*8, TILE_SIZE*8, INFO_HEIGHT)
    pos3 = pygame.Rect(BORDER, BORDER*3 + TILE_SIZE*8 + 25, TILE_SIZE*8, INFO_HEIGHT)
    pos4 = pygame.Rect(BORDER, BORDER*3 + TILE_SIZE*8 + 25, TILE_SIZE*8, INFO_HEIGHT)
    pos5 = pygame.Rect(BORDER, BORDER*3 + TILE_SIZE*8 + 25, TILE_SIZE*8, INFO_HEIGHT)
    screen.blit(s1, s1.get_rect(topleft=pos1.topleft))
    screen.blit(s2, s2.get_rect(topright=pos2.topright))
    screen.blit(s3, s2.get_rect(topleft=pos3.topleft))
    screen.blit(s4, s2.get_rect(topright=pos4.topright))
    screen.blit(s5, s2.get_rect(midtop=pos5.midtop))

w = TILE_SIZE*8 + BORDER*2  # width of window
h = w + INFO_HEIGHT
screen = pygame.display.set_mode((w, h))

def options():
    run_option = True
    while run_option:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        board = chess.Board()
        #move_generator = ChessEngineHelper.MoveGenerator()
        #screen.fill("white")
        #screen.fill("#3a0325")
        screen.fill("#2b021b")
        
        MENU_TEXT = get_font(50).render("OPTIONS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(271, 71))

        LEVEL1_BUTTON = Button(image=pygame.image.load("chess-main/Assets/Play Rect.png"), pos=(271, 195), 
                            text_input="Depth 2", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        LEVEL2_BUTTON = Button(image=pygame.image.load("chess-main/Assets/Play Rect.png"), pos=(271, 324), 
                            text_input="Depth 3", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        LEVEL3_BUTTON = Button(image=pygame.image.load("chess-main/Assets/Play Rect.png"), pos=(271, 454), 
                            text_input="Depth 4", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)
        
        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(OPTIONS_MOUSE_POS):       
                    play_chess(board, black=AlphaBetaMove.BestMove().alpha_beta_move_1)
                    pygame.quit()
                    sys.exit()
                if LEVEL2_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    play_chess(board, black=AlphaBetaMove.BestMove().alpha_beta_move_2)
                    pygame.quit()
                    sys.exit()
                if LEVEL3_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    play_chess(board, black=AlphaBetaMove.BestMove().alpha_beta_move_3)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play_chess(chess_board, white="player", black="player"):
    pygame.init()
    font = pygame.font.SysFont('', 32)
    pygame.display.set_caption("Chess UI")
    #w = TILE_SIZE*8 + BORDER*2  # width of window
    #h = w + INFO_HEIGHT
    #screen = pygame.display.set_mode((w, h))
    # convert the real chess board object to custom board array
    board = create_board_from_fen(chess_board.board_fen())
    board_surface = create_board_surface()
    clock = pygame.time.Clock()
    selected_piece = None
    drop_pos = None
    piece = x = y = None
    
    running = False
    runmenu = True
    
    while runmenu and (not running):
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("CHESS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(271, 71))

        PLAY_BUTTON = Button(image=pygame.image.load("chess-main/Assets/Play Rect.png"), pos=(271, 195), 
                            text_input="PLAY", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("chess-main/Assets/Play Rect.png"), pos=(271, 324), 
                            text_input="OPTIONS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("chess-main/Assets/Play Rect.png"), pos=(271, 454), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = True
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #runmenu = False
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    
    
    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                 chess_board.outcome()
        
        # don't try to play if the game is over
        outcome = chess_board.outcome()
        
        if outcome is None:

            if chess_board.turn == chess.WHITE and white == "player" \
                    or chess_board.turn == chess.BLACK and black == "player":
                piece, x, y = get_square_under_mouse(board)
                # events = pygame.event.get()
                for e in events:
                    if e.type == pygame.QUIT:
                         outcome
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if piece is not None:
                            selected_piece = piece, x, y
                        if BACK_BUTTON.checkForInput(BACK_MOUSE_POS):
                            play_chess(chess.Board(), black=AlphaBetaMove.BestMove().alpha_beta_move)
                            pygame.quit()
                            sys.exit()
                    if e.type == pygame.MOUSEBUTTONUP:
                        if drop_pos:
                            piece, old_x, old_y = selected_piece
                            new_x, new_y = drop_pos
                            if new_x is not None and new_y is not None:
                                # horrible math to convert board array position to chess.Square
                                # I have to reverses the columns since my array starts at A8 not A1
                                move = chess.Move(((7 - old_y)*8 + old_x), ((7 - new_y)*8 + new_x))
                                move2 = chess.Move(((7 - old_y)*8 + old_x), ((7 - new_y)*8 + new_x), chess.QUEEN)
                                # quick hack to enable pawn promotion
                                if move2 in chess_board.legal_moves:
                                    # push the move to the real chess board
                                    chess_board.push(move2)
                                    # update our array representation
                                    board[int(old_y)][old_x] = None
                                    board[int(new_y)][new_x] = ('white', 'queen')
                                elif move in chess_board.legal_moves or ENABLE_ILLEGAL_MOVES:
                                    # push the move to the real chess board
                                    chess_board.push(move)
                                    # update our array representation
                                    board[int(old_y)][old_x] = None
                                    board[new_y][new_x] = piece
                                # this refresh will reset the board if a piece was dragged somewhere invalid
                                board = create_board_from_fen(chess_board.board_fen())
                        selected_piece = None
                        drop_pos = None
                    
            else:
                if chess_board.turn == chess.WHITE:
                    move = white(chess_board)
                    if move is False:
                        
                    chess_board.push(move)
                else:
                    move = black(chess_board)
                    if move is False:
                        
                    chess_board.push(move)
                board = create_board_from_fen(chess_board.board_fen())
        else:
            for e in events:
                if e.type == pygame.QUIT:
                     outcome
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if REPLAY_BUTTON.checkForInput(REPLAY_MOUSE_POS):
                        play_chess(chess.Board(), black=AlphaBetaMove.BestMove().alpha_beta_move)
                        pygame.quit()
                        sys.exit()
            
            REPLAY_MOUSE_POS = pygame.mouse.get_pos()
            REPLAY_BUTTON = Button(image=pygame.image.load("chess-main/Assets/back3.png"), pos=(271, 590), 
                            text_input="REPLAY", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
                      

        
        screen.fill(pygame.Color(COLOR_BG))
        screen.blit(board_surface, BOARD_POS)
        BACK_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON = Button(image=pygame.image.load("chess-main/Assets/back3.png"), pos=(271, 554), 
                            text_input="MENU", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
        for button in [BACK_BUTTON]:
            button.changeColor(BACK_MOUSE_POS)
            button.update(screen)
        
        draw_pieces(screen, board, font, selected_piece)
        
        if drop_pos:
            draw_selector(screen, piece, x, y)
        drop_pos = draw_drag(screen, board, selected_piece, font)
        draw_info(screen, chess_board, font)
             
        pygame.display.flip()
        clock.tick(60)
