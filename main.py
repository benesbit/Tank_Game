# Ben Nesbit
# Simple "tank game"

# Import pygame module
import time
import random
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

def draw_tank(x_location, y_location):
    GAME_DISPLAY.blit(TANK_IMAGE_PLAYER_ONE, (x_location, y_location))

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    GAME_DISPLAY.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def tank_crash():
    message_display('You Crashed!')
    game_loop()

def game_loop():
    x_position = (DISPLAY_WIDTH * 0.45)
    y_position = (DISPLAY_HEIGHT * 0.8)

    x_change = 0
    
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x_position += x_change
        
        GAME_DISPLAY.fill(WHITE)
        draw_tank(x_position, y_position)

        if x_position > DISPLAY_WIDTH - TANK_WIDTH or x_position < 0:
            tank_crash()
        # if X > DISPLAY_WIDTH - TANK_WIDTH:
        #     X = DISPLAY_WIDTH - TANK_WIDTH
        # elif X < 0:
        #     X = 0
        
        pygame.display.update()
        CLOCK.tick(60)

game_loop()
pygame.quit()
quit()
