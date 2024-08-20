import pygame

pygame.init()

WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))

clock = pygame.time.Clock()
running = True

def load_image(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

ICON_X = load_image('images/x-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
ICON_O = load_image('images/o-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
GRID = load_image('images/grid.png', [WINDOW_WIDTH, WINDOW_WIDTH])

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

PLAYER_1 = 0
PLAYER_2 = 1
player = PLAYER_1

def play_turn(current_player):
    curr_coordinate = pygame.math.Vector2(pygame.mouse.get_pos())
    normalized_coordinate = curr_coordinate // PIXEL_WIDTH
    if (pygame.mouse.get_pressed()[0]):
        col, row = map(int, normalized_coordinate)
        board[row][col] = current_player
        global player
        player = 1 - player
        
def draw_icons():
    for i, row in enumerate(board):
        for j, col in enumerate(board[i]):
            if board[i][j] == 0:
                screen.blit(ICON_O, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))
            elif board[i][j] == 1:
                screen.blit(ICON_X, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))
            

    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # Render your game here
    pygame.display.flip()
    screen.fill("white")
    screen.blit(GRID, (0, 0))
    pygame.event.wait()
    play_turn(player)
    draw_icons() 
    
    clock.tick(60)

pygame.quit()