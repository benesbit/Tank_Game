# Ben Nesbit

# Import pygame module
import pygame

# Initialize pygame module
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Tank Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CLOCK = pygame.time.Clock()

CRASHED = False

CAR_IMG = pygame.image.load('images/tank_player_one.png')

def car(x_location, y_location):
    GAME_DISPLAY.blit(CAR_IMG, (x_location, y_location))

X = (DISPLAY_WIDTH * 0.45)
Y = (DISPLAY_HEIGHT * 0.8)

while not CRASHED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASHED = True
            print(event)
    
    GAME_DISPLAY.fill(WHITE)
    car(X, Y)
    
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
