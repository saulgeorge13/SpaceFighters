import pygame
import os
import time
import random

# Window Setup
WIDTH = 750
HEIGHT = 750
VIEW_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE FIGHTERS")

# Load Images from assets

# Ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
PLAYER_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
Background = pygame.image.load(os.path.join("assets", "background-black.png"))


