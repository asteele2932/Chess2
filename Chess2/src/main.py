# note - there are giant section headers rn, will be removed when finalizing, just helpful atm
import pygame
pygame.init()


WIDTH = 900 
HEIGHT = 700
BOARD_LENGTH = 550
CAPTURE_WIDTH = 150
CAPTURE_HEIGHT = 350
CLOCK_WIDTH = 150
CLOCK_HEIGHT = 60
PLAYER_WIDTH = 275
PLAYER_HEIGHT = 50
PIECE_SCALE = (60, 60)
SMALL_PIECE_SCALE = (30, 30)

screen = pygame.display.set_mode([WIDTH, HEIGHT])


lighter_purple = ('#c08bf7')
light_purple = ('#9235f0')
dark_purple = ('#7022bf')
darkest_purple = ('#340761')
white = ('#ffffff')
black = ('#000000')
font = pygame.font.Font('Roboto-Black.ttf', 16)
clock = pygame.time.Clock()
fps = 60


white_board = pygame.transform.scale(pygame.image.load('assets/white_board_labeled.png'), (BOARD_LENGTH, BOARD_LENGTH))
# board labels also a work in progress, will make new ones with better resolution

# ______________________________________________________________________________________________
#  ___ _               
# | _ (_)___ __ ___ ___
# |  _/ / -_) _/ -_|_-<
# |_| |_\___\__\___/__/
piece_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king'] # this corresponds w/ image lists
turn_phase = 0 
selection = 1000 # start at random impossible val
# 0 = white turn, no select; 1 = white turn, made select; 
# 2 = black turn, no select; 3 = black turn, made select
legal_moves = []
squares = {
    'a8': (235, 95),
    'a7': (235, 165),
    'a6': (235, 235),
    'a5': (235, 305),
    'a4': (235, 370),
    'a3': (235, 440),
    'a2': (235, 510),
    'a1': (235, 580),
    'b8': (305, 95),
    'b7': (305, 165),
    'b6': (305, 235),
    'b5': (305, 305),
    'b4': (305, 370),
    'b3': (305, 440),
    'b2': (305, 510),
    'b1': (305, 580),
    'c8': (370, 95),
    'c7': (370, 165),
    'c6': (370, 235),
    'c5': (370, 305),
    'c4': (370, 370),
    'c3': (370, 440),
    'c2': (370, 510),
    'c1': (370, 580),
    'd8': (440, 95),
    'd7': (440, 165),
    'd6': (440, 235),
    'd5': (440, 305),
    'd4': (440, 370),
    'd3': (440, 440),
    'd2': (440, 510),
    'd1': (440, 580),
    'e8': (510, 95),
    'e7': (510, 165),
    'e6': (510, 235),
    'e5': (510, 305),
    'e4': (510, 370),
    'e3': (510, 440),
    'e2': (510, 510),
    'e1': (510, 580),
    'f8': (580, 95),
    'f7': (580, 165),
    'f6': (580, 235),
    'f5': (580, 305),
    'f4': (580, 370),
    'f3': (580, 440),
    'f2': (580, 510),
    'f1': (580, 580),
    'g8': (645, 95),
    'g7': (645, 165),
    'g6': (645, 235),
    'g5': (645, 305),
    'g4': (645, 370),
    'g3': (645, 440),
    'g2': (645, 510),
    'g1': (645, 580),
    'h8': (715, 95),
    'h7': (715, 165),
    'h6': (715, 235),
    'h5': (715, 305),
    'h4': (715, 370),
    'h3': (715, 440),
    'h2': (715, 510),
    'h1': (715, 580)
}



white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
# coords store current position, not necessarily referenced for starting positions
white_coords = [squares['a1'], squares['b1'], squares['c1'], squares['d1'], 
                squares['e1'], squares['f1'], squares['g1'], squares['h1'],
                squares['a2'], squares['b2'], squares['c2'], squares['d2'], 
                squares['e2'], squares['f2'], squares['g2'], squares['h2'],]

black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_coords = [squares['a8'], squares['b8'], squares['c8'], squares['d8'], 
                squares['e8'], squares['f8'], squares['g8'], squares['h8'],
                squares['a7'], squares['b7'], squares['c7'], squares['d7'], 
                squares['e7'], squares['f7'], squares['g7'], squares['h7'],]

captured_white = []
captured_black = []


# piece images
pWhite = pygame.transform.scale(pygame.image.load('assets/wp.png'), PIECE_SCALE)
pW_small = pygame.transform.scale(pWhite, SMALL_PIECE_SCALE)
NWhite = pygame.transform.scale(pygame.image.load('assets/wN.png'), PIECE_SCALE)
NW_small = pygame.transform.scale(NWhite, SMALL_PIECE_SCALE)
BWhite = pygame.transform.scale(pygame.image.load('assets/wB.png'), PIECE_SCALE)
BW_small = pygame.transform.scale(BWhite, SMALL_PIECE_SCALE)
RWhite = pygame.transform.scale(pygame.image.load('assets/wR.png'), PIECE_SCALE)
RW_small = pygame.transform.scale(RWhite, SMALL_PIECE_SCALE)
QWhite = pygame.transform.scale(pygame.image.load('assets/wQ.png'), PIECE_SCALE)
QW_small = pygame.transform.scale(QWhite, SMALL_PIECE_SCALE)
KWhite = pygame.transform.scale(pygame.image.load('assets/wK.png'), PIECE_SCALE)
white_images = [pWhite, NWhite, BWhite, RWhite, QWhite, KWhite]
white_images_small = [pW_small, NW_small, BW_small, RW_small, QW_small]


pBlack = pygame.transform.scale(pygame.image.load('assets/bp.png'), PIECE_SCALE)
pB_small = pygame.transform.scale(pBlack, SMALL_PIECE_SCALE)
NBlack = pygame.transform.scale(pygame.image.load('assets/bN.png'), PIECE_SCALE)
NB_small = pygame.transform.scale(NBlack, SMALL_PIECE_SCALE)
BBlack = pygame.transform.scale(pygame.image.load('assets/bB.png'), PIECE_SCALE)
BB_small = pygame.transform.scale(BBlack, SMALL_PIECE_SCALE)
RBlack = pygame.transform.scale(pygame.image.load('assets/bR.png'), PIECE_SCALE)
RB_small = pygame.transform.scale(RBlack, SMALL_PIECE_SCALE)
QBlack = pygame.transform.scale(pygame.image.load('assets/bQ.png'), PIECE_SCALE)
QB_small = pygame.transform.scale(QBlack, SMALL_PIECE_SCALE)
KBlack = pygame.transform.scale(pygame.image.load('assets/bK.png'), PIECE_SCALE)
black_images = [pBlack, NBlack, BBlack, RBlack, QBlack, KBlack]
black_images_small = [pB_small, NB_small, BB_small, RB_small, QB_small]



# ______________________________________________________________________________________________
#  ___                     _   ___       _               
# | _ ) ___  __ _  _ _  __| | / __| ___ | |_  _  _  _ __ 
# | _ \/ _ \/ _` || '_|/ _` | \__ \/ -_)|  _|| || || '_ \
# |___/\___/\__,_||_|  \__,_| |___/\___| \__| \_,_|| .__/
#                                                  |_| 
def make_board():
    screen.fill(light_purple)
    screen.blit(white_board, ((200, 60)))
    # captured pieces area
    pygame.draw.rect(screen, dark_purple, pygame.Rect(750, 160, CAPTURE_WIDTH, CAPTURE_HEIGHT))
    # clock background
    pygame.draw.rect(screen, dark_purple, pygame.Rect(750, 60, CLOCK_WIDTH + 1, CLOCK_HEIGHT + 1))
    pygame.draw.rect(screen, dark_purple, pygame.Rect(750, 550, CLOCK_WIDTH + 1, CLOCK_HEIGHT + 1))
    # player background
    pygame.draw.rect(screen, dark_purple, pygame.Rect(200, 10, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, dark_purple, pygame.Rect(200, 610, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.display.set_caption('ChessNow')

    # boarders
    pygame.draw.rect(screen, darkest_purple, pygame.Rect(750, 60, CLOCK_WIDTH, CLOCK_HEIGHT), 5)
    pygame.draw.rect(screen, darkest_purple, pygame.Rect(750, 550, CLOCK_WIDTH, CLOCK_HEIGHT), 5)
    pygame.draw.rect(screen, darkest_purple, pygame.Rect(750, 160, CAPTURE_WIDTH, CAPTURE_HEIGHT), 5)
    pygame.draw.rect(screen, darkest_purple, pygame.Rect(200, 10, PLAYER_WIDTH, PLAYER_HEIGHT), 5)
    pygame.draw.rect(screen, darkest_purple, pygame.Rect(200, 610, PLAYER_WIDTH, PLAYER_HEIGHT), 5)
    # this black boarder is a work in progress
    pygame.draw.rect(screen, black, pygame.Rect(198, 58, BOARD_LENGTH + 5, BOARD_LENGTH + 5), 8)

def square_markers():
    # A's
    pygame.draw.circle(screen, 'red', (235, 95), 5) # 35 =~ the center of 1 square
    a8 = (235, 95)
    pygame.draw.circle(screen, 'red', (235, 165), 5)
    a7 = (235, 165)
    pygame.draw.circle(screen, 'red', (235, 235), 5)
    a6 = (235, 235)
    pygame.draw.circle(screen, 'red', (235, 305), 5)
    a5 = (235, 305)
    pygame.draw.circle(screen, 'red', (235, 370), 5)
    a4 = (235, 370)
    pygame.draw.circle(screen, 'red', (235, 440), 5)
    a3 = (235, 440)
    pygame.draw.circle(screen, 'red', (235, 510), 5)
    a2 = (235, 510)
    pygame.draw.circle(screen, 'red', (235, 580), 5)
    a1 = (235, 580)


    # B's
    pygame.draw.circle(screen, 'red', (305, 95), 5)
    b8 = (305, 95)
    pygame.draw.circle(screen, 'red', (305, 165), 5)
    b7 = (305, 165)
    pygame.draw.circle(screen, 'red', (305, 235), 5)
    b6 = (305, 235)
    pygame.draw.circle(screen, 'red', (305, 305), 5)
    b5 = (305, 305)
    pygame.draw.circle(screen, 'red', (305, 370), 5)
    b4 = (305, 370)
    pygame.draw.circle(screen, 'red', (305, 440), 5)
    b3 = (305, 440)
    pygame.draw.circle(screen, 'red', (305, 510), 5)
    b2 = (305, 510)
    pygame.draw.circle(screen, 'red', (305, 580), 5)
    b1 = (305, 580)

    # C's
    pygame.draw.circle(screen, 'red', (370, 95), 5)
    c8 = (370, 95)
    pygame.draw.circle(screen, 'red', (370, 165), 5)
    c7 = (370, 165)
    pygame.draw.circle(screen, 'red', (370, 235), 5)
    c6 = (370, 235)
    pygame.draw.circle(screen, 'red', (370, 305), 5)
    c5 = (370, 305)
    pygame.draw.circle(screen, 'red', (370, 370), 5)
    c4 = (370, 370)
    pygame.draw.circle(screen, 'red', (370, 440), 5)
    c3 = (370, 440)
    pygame.draw.circle(screen, 'red', (370, 510), 5)
    c2 = (370, 510)
    pygame.draw.circle(screen, 'red', (370, 580), 5)
    c1 = (370, 580)

    # D's
    pygame.draw.circle(screen, 'red', (440, 95), 5)
    d8 = (440, 95)
    pygame.draw.circle(screen, 'red', (440, 165), 5)
    d7 = (440, 165)
    pygame.draw.circle(screen, 'red', (440, 235), 5)
    d6 = (440, 235)
    pygame.draw.circle(screen, 'red', (440, 305), 5)
    d5 = (440, 305)
    pygame.draw.circle(screen, 'red', (440, 370), 5)
    d4 = (440, 370)
    pygame.draw.circle(screen, 'red', (440, 440), 5)
    d3 = (440, 440)
    pygame.draw.circle(screen, 'red', (440, 510), 5)
    d2 = (440, 510)
    pygame.draw.circle(screen, 'red', (440, 580), 5)
    d1 = (440, 580)


    # E's
    pygame.draw.circle(screen, 'red', (510, 95), 5)
    e8 = (510, 95)
    pygame.draw.circle(screen, 'red', (510, 165), 5)
    e7 = (510, 165)
    pygame.draw.circle(screen, 'red', (510, 235), 5)
    e6 = (510, 235)
    pygame.draw.circle(screen, 'red', (510, 305), 5)
    e5 = (510, 305)
    pygame.draw.circle(screen, 'red', (510, 370), 5)
    e4 = (510, 370)
    pygame.draw.circle(screen, 'red', (510, 440), 5)
    e3 = (510, 440)
    pygame.draw.circle(screen, 'red', (510, 510), 5)
    e2 = (510, 510)
    pygame.draw.circle(screen, 'red', (510, 580), 5)
    e1 = (510, 580)


    # F's
    pygame.draw.circle(screen, 'red', (580, 95), 5)
    f8 = (580, 95)
    pygame.draw.circle(screen, 'red', (580, 165), 5)
    f7 = (580, 165)
    pygame.draw.circle(screen, 'red', (580, 235), 5)
    f6 = (580, 235)
    pygame.draw.circle(screen, 'red', (580, 305), 5)
    f5 = (580, 305)
    pygame.draw.circle(screen, 'red', (580, 370), 5)
    f4 = (580, 370)
    pygame.draw.circle(screen, 'red', (580, 440), 5)
    f3 = (580, 440)
    pygame.draw.circle(screen, 'red', (580, 510), 5)
    f2 = (580, 510)
    pygame.draw.circle(screen, 'red', (580, 580), 5)
    f1 = (580, 580)


    # G's
    pygame.draw.circle(screen, 'red', (645, 95), 5)
    g8 = (645, 95)
    pygame.draw.circle(screen, 'red', (645, 165), 5)
    g7 = (645, 165)
    pygame.draw.circle(screen, 'red', (645, 235), 5)
    g6 = (645, 235)
    pygame.draw.circle(screen, 'red', (645, 305), 5)
    g5 = (645, 305)
    pygame.draw.circle(screen, 'red', (645, 370), 5)
    g4 = (645, 370)
    pygame.draw.circle(screen, 'red', (645, 440), 5)
    g3 = (645, 440)
    pygame.draw.circle(screen, 'red', (645, 510), 5)
    g2 = (645, 510)
    pygame.draw.circle(screen, 'red', (645, 580), 5)
    g1 = (645, 580)


    # H's
    pygame.draw.circle(screen, 'red', (715, 95), 5)
    h8 = (715, 95)
    pygame.draw.circle(screen, 'red', (715, 165), 5)
    h7 = (715, 165)
    pygame.draw.circle(screen, 'red', (715, 235), 5)
    h6 = (715, 235)
    pygame.draw.circle(screen, 'red', (715, 305), 5)
    h5 = (715, 305)
    pygame.draw.circle(screen, 'red', (715, 370), 5)
    h4 = (715, 370)
    pygame.draw.circle(screen, 'red', (715, 440), 5)
    h3 = (715, 440)
    pygame.draw.circle(screen, 'red', (715, 510), 5)
    h2 = (715, 510)
    pygame.draw.circle(screen, 'red', (715, 580), 5)
    h1 = (715, 580)

def make_pieces():
    # white pieces
    screen.blit(RWhite, (squares['a1'][0] - 30, squares['a1'][1] - 35)) # x -30, y -35
    screen.blit(NWhite, (squares['b1'][0] - 30, squares['b1'][1] - 35))
    screen.blit(BWhite, (squares['c1'][0] - 30, squares['c1'][1] - 35))
    screen.blit(QWhite, (squares['d1'][0] - 30, squares['d1'][1] - 35))
    screen.blit(KWhite, (squares['e1'][0] - 30, squares['e1'][1] - 35))
    screen.blit(BWhite, (squares['f1'][0] - 30, squares['f1'][1] - 35))
    screen.blit(NWhite, (squares['g1'][0] - 30, squares['g1'][1] - 35))
    screen.blit(RWhite, (squares['h1'][0] - 30, squares['h1'][1] - 35))
    # white pawns
    screen.blit(pWhite, (squares['a2'][0] - 30, squares['a2'][1] - 35))
    screen.blit(pWhite, (squares['b2'][0] - 30, squares['b2'][1] - 35))
    screen.blit(pWhite, (squares['c2'][0] - 30, squares['c2'][1] - 35))
    screen.blit(pWhite, (squares['d2'][0] - 30, squares['d2'][1] - 35))
    screen.blit(pWhite, (squares['e2'][0] - 30, squares['e2'][1] - 35))
    screen.blit(pWhite, (squares['f2'][0] - 30, squares['f2'][1] - 35))
    screen.blit(pWhite, (squares['g2'][0] - 30, squares['g2'][1] - 35))
    screen.blit(pWhite, (squares['h2'][0] - 30, squares['h2'][1] - 35))

    # black pieces
    screen.blit(RBlack, (squares['a8'][0] - 30, squares['a8'][1] - 30))
    screen.blit(NBlack, (squares['b8'][0] - 30, squares['b8'][1] - 30))
    screen.blit(BBlack, (squares['c8'][0] - 30, squares['c8'][1] - 30))
    screen.blit(QBlack, (squares['d8'][0] - 30, squares['d8'][1] - 30))
    screen.blit(KBlack, (squares['e8'][0] - 30, squares['e8'][1] - 30))
    screen.blit(BBlack, (squares['f8'][0] - 30, squares['f8'][1] - 30))
    screen.blit(NBlack, (squares['g8'][0] - 30, squares['g8'][1] - 30))
    screen.blit(RBlack, (squares['h8'][0] - 30, squares['h8'][1] - 30))
    # black pawns
    screen.blit(pBlack, (squares['a7'][0] - 30, squares['a7'][1] - 30))
    screen.blit(pBlack, (squares['b7'][0] - 30, squares['b7'][1] - 30))
    screen.blit(pBlack, (squares['c7'][0] - 30, squares['c7'][1] - 30))
    screen.blit(pBlack, (squares['d7'][0] - 30, squares['d7'][1] - 30))
    screen.blit(pBlack, (squares['e7'][0] - 30, squares['e7'][1] - 30))
    screen.blit(pBlack, (squares['f7'][0] - 30, squares['f7'][1] - 30))
    screen.blit(pBlack, (squares['g7'][0] - 30, squares['g7'][1] - 30))
    screen.blit(pBlack, (squares['h7'][0] - 30, squares['h7'][1] - 30))
    
    



# ______________________________________________________________________________________________
#   ___                     _                    
#  / __| __ _  _ __   ___  | |    ___  ___  _ __ 
# | (_ |/ _` || '  \ / -_) | |__ / _ \/ _ \| '_ \
#  \___|\__,_||_|_|_|\___| |____|\___/\___/| .__/
#                                          |_|  
#
run = True
while run == True:
    make_board()
    # square_markers() -> this was a visual helper to find proper coords, can
    # repurposed later to highlight legal moves
    make_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
