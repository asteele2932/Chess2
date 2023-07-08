
import pygame

# BOARD SETUP
pygame.init()

WIDTH = 900 
HEIGHT = 675
BOARD_LENGTH = 550
CAPTURE_WIDTH = 150
CAPTURE_HEIGHT = 350
CLOCK_WIDTH = 150
CLOCK_HEIGHT = 60
PLAYER_WIDTH = 275
PLAYER_HEIGHT = 50

font = pygame.font.Font('Roboto-Black.ttf', 20)
light_purple = ('#9235f0')
dark_purple = ('#7022bf')
darkest_purple = ('#340761')
white = ('#ffffff')
black = ('#000000')

screen = pygame.display.set_mode([WIDTH, HEIGHT])
# background
screen.fill(light_purple)
# board background
board = pygame.draw.rect(screen, white, pygame.Rect(160, 62, BOARD_LENGTH, BOARD_LENGTH))
# captured pieces area
pygame.draw.rect(screen, dark_purple, pygame.Rect(710, 162, CAPTURE_WIDTH, CAPTURE_HEIGHT))
# clock background
pygame.draw.rect(screen, dark_purple, pygame.Rect(710, 62, CLOCK_WIDTH, CLOCK_HEIGHT))
pygame.draw.rect(screen, dark_purple, pygame.Rect(710, 552, CLOCK_WIDTH, CLOCK_HEIGHT))
# player background
pygame.draw.rect(screen, dark_purple, pygame.Rect(160, 12, PLAYER_WIDTH, PLAYER_HEIGHT))
pygame.draw.rect(screen, dark_purple, pygame.Rect(160, 611, PLAYER_WIDTH, PLAYER_HEIGHT))
pygame.display.set_caption('ChessNow')

def row(EorO: str, Hposition: int, Vposition: int):
    if EorO == 'even':
        for i in range(4):
            pygame.draw.rect(screen, black, pygame.Rect(Hposition, Vposition, 68.75, 68.75))
            Hposition += (68.75 * 2)
    else:
        for i in range(4):
            pygame.draw.rect(screen, black, pygame.Rect(Hposition, Vposition, 68.75, 68.57))
            Hposition += (68.75 * 2)

def board_squares():
    Hposition = 160
    Vposition = 62

    row('even', Hposition, Vposition)
    Hposition += 68.75
    Vposition += 68.75
    row('odd', Hposition, Vposition)
    Hposition = 160
    Vposition += 68.75
    row('even', Hposition, Vposition)
    Hposition += 68.75
    Vposition += 68.75
    row('odd', Hposition, Vposition)
    Hposition = 160
    Vposition += 68.75
    row('even', Hposition, Vposition)
    Hposition += 68.75
    Vposition += 68.75
    row('odd', Hposition, Vposition)
    Hposition = 160
    Vposition += 68.75
    row('even', Hposition, Vposition)
    Hposition += 68.75
    Vposition += 68.75
    row('odd', Hposition, Vposition)

board_squares()

# boarders
pygame.draw.rect(screen, darkest_purple, pygame.Rect(710, 62, CLOCK_WIDTH, CLOCK_HEIGHT), 6)
pygame.draw.rect(screen, darkest_purple, pygame.Rect(710, 552, CLOCK_WIDTH, CLOCK_HEIGHT), 6)
pygame.draw.rect(screen, darkest_purple, pygame.Rect(710, 162, CAPTURE_WIDTH, CAPTURE_HEIGHT), 6)
pygame.draw.rect(screen, darkest_purple, pygame.Rect(160, 12, PLAYER_WIDTH, PLAYER_HEIGHT), 6)
pygame.draw.rect(screen, darkest_purple, pygame.Rect(160, 611, PLAYER_WIDTH, PLAYER_HEIGHT), 6)
pygame.draw.rect(screen, black, pygame.Rect(160, 62, BOARD_LENGTH, BOARD_LENGTH), 6)


font = pygame.font.Font('Roboto-Black.ttf', 20)
clock = pygame.time.Clock()
fps = 60



# game process
run = True
while run == True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()

