# Ben Nesbit
# main.py
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

TANK_WIDTH = 95
TANK_HEIGHT = 100
TANK_SPEED = 8

POWER_UP_WIDTH = 55
POWER_UP_HEIGHT = 100

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Tank Game')
CLOCK = pygame.time.Clock()

IMAGE_TANK_PLAYER_ONE = \
    pygame.transform.scale(pygame.image.load('images/tank_player_one.png'), \
        (TANK_WIDTH, TANK_HEIGHT))

IMAGE_POWER_UP_BOMB = \
    pygame.transform.scale(pygame.image.load('images/bomb_power_up.png'), \
        (POWER_UP_WIDTH, POWER_UP_HEIGHT))

def draw_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, BLACK)
    GAME_DISPLAY.blit(text, (0,0))

def draw_block(x_location, y_location, block_width, block_height, color):
    pygame.draw.rect(GAME_DISPLAY, color, [x_location, y_location, block_width, block_height])

def draw_tank(x_location, y_location):
    GAME_DISPLAY.blit(IMAGE_TANK_PLAYER_ONE, (x_location, y_location))

def draw_power_up(x_location, y_location):
    GAME_DISPLAY.blit(IMAGE_POWER_UP_BOMB, (x_location, y_location))

def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()

def draw_message_center_screen(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    GAME_DISPLAY.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(2)

def tank_crash():
    draw_message_center_screen('You Crashed!')
    game_loop()

def game_loop():
    x_location = (DISPLAY_WIDTH * 0.45)
    y_location = (DISPLAY_HEIGHT * 0.8)

    x_change = 0

    block_x_location = random.randrange(0, DISPLAY_WIDTH)
    block_y_location = -600
    block_speed = 7
    block_width = 100
    block_height = 100

    dodged = 0
    
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -TANK_SPEED
                elif event.key == pygame.K_RIGHT:
                    x_change = TANK_SPEED

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x_location += x_change
        block_y_location += block_speed
        
        GAME_DISPLAY.fill(WHITE)

        draw_tank(x_location, y_location)
        draw_block(block_x_location, block_y_location, block_width, block_height, BLACK)
        draw_score(dodged)

        if x_location > DISPLAY_WIDTH - TANK_WIDTH or x_location < 0:
            tank_crash()
            # if X > DISPLAY_WIDTH - TANK_WIDTH:
            #     X = DISPLAY_WIDTH - TANK_WIDTH
            # elif X < 0:
            #     X = 0

        if block_y_location > DISPLAY_HEIGHT:
            block_y_location = 0 - block_height
            block_x_location = random.randrange(0, DISPLAY_WIDTH)
            dodged += 1
            block_speed += 1
            block_width += (dodged * 1.2)

        if y_location < block_y_location + block_height:
            print('y crossover')

            if x_location > block_x_location and x_location < block_x_location + block_width or x_location + TANK_WIDTH > block_x_location and x_location + TANK_WIDTH < block_x_location+block_width:
                print('x crossover')
                tank_crash()
        
        pygame.display.update()
        CLOCK.tick(60)

game_loop()
pygame.quit()
quit()
