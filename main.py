# Ben Nesbit

# Import pygame module
import pygame

# Initialize pygame module
pygame.init()

DISPLAY_WIDTH = 1050
DISPLAY_HEIGHT = 620

TANK_WIDTH = 45
TANK_HEIGHT = 50

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Tank Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CLOCK = pygame.time.Clock()

CRASHED = False

TANK_IMAGE_PLAYER_ONE = \
    pygame.transform.scale(pygame.image.load('images/tank_player_one.png'), \
        (TANK_WIDTH, TANK_HEIGHT))

def car(x_location, y_location):
    GAME_DISPLAY.blit(TANK_IMAGE_PLAYER_ONE, (x_location, y_location))

X = (DISPLAY_WIDTH * 0.45)
Y = (DISPLAY_HEIGHT * 0.8)
X_CHANGE = 0
TANK_SPEED_PLAYER_ONE = 0

while not CRASHED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASHED = True
            print(event)
        
        #############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_CHANGE = -5
                if X_CHANGE < -20:
                    X_CHANGE = -20
            elif event.key == pygame.K_RIGHT:
                X_CHANGE = 5
                if X_CHANGE > 20:
                    X_CHANGE = 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_CHANGE = 0
        ##############################
    ##
    X += X_CHANGE
    
    GAME_DISPLAY.fill(WHITE)
    car(X, Y)
    
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
