# Ben Nesbit

# Import pygame module
import pygame

# Initialize pygame module
pygame.init()

DISPLAY_WIDTH = 1050
DISPLAY_HEIGHT = 620

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

TANK_WIDTH = 45
TANK_HEIGHT = 50

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Tank Game')
CLOCK = pygame.time.Clock()

TANK_IMAGE_PLAYER_ONE = \
    pygame.transform.scale(pygame.image.load('images/tank_player_one.png'), \
        (TANK_WIDTH, TANK_HEIGHT))

GAME_EXIT = False

def tank(x_location, y_location):
    GAME_DISPLAY.blit(TANK_IMAGE_PLAYER_ONE, (x_location, y_location))

X = (DISPLAY_WIDTH * 0.45)
Y = (DISPLAY_HEIGHT * 0.8)
X_CHANGE = 0
TANK_SPEED_PLAYER_ONE = 0

while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True
            print(event)
        
        #############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_CHANGE = -5
            elif event.key == pygame.K_RIGHT:
                X_CHANGE = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_CHANGE = 0
        ##############################

    X += X_CHANGE
    
    GAME_DISPLAY.fill(WHITE)
    tank(X, Y)

    if X > DISPLAY_WIDTH - TANK_WIDTH or X < 0:
        GAME_EXIT = True
    # if X > DISPLAY_WIDTH - TANK_WIDTH:
    #     X = DISPLAY_WIDTH - TANK_WIDTH
    # elif X < 0:
    #     X = 0
    
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
