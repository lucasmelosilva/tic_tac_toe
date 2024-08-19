import pygame

pygame.init()
WINDOW_WIDTH = 720
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

def load_image(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

ICON_X = load_image('images/x-icon.png', [WINDOW_WIDTH // 3, WINDOW_WIDTH // 3])
ICON_O = load_image('images/o-icon.png', [WINDOW_WIDTH // 3, WINDOW_WIDTH // 3])

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    # Render your game here
    grid = load_image('images/grid.png',[WINDOW_WIDTH, WINDOW_WIDTH])
    screen.blit(grid, (0, 0))
    screen.blit(ICON_X, (0, 0))
    screen.blit(ICON_O, (WINDOW_WIDTH // 3, WINDOW_WIDTH // 3))
    pygame.display.flip()

    clock.tick(60) 

pygame.quit()