# Ben Nesbit
# tank.py

# import pygame module
import pygame

TANK_WIDTH = 95
TANK_HEIGHT = 100
TANK_SPEED = 8

def get_image_tank_player_one():
    return pygame.transform.scale(pygame.image.load('images/tank_player_one.png'), \
        (TANK_WIDTH, TANK_HEIGHT))