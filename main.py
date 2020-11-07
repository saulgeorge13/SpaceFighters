import pygame
import os
import time
import random
pygame.font.init()

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
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Main Function
def main():
    run = True
    fps = 60
    level = 1
    lives = 3
    mainFont = pygame.font.SysFont("calibri", 50)
    clock = pygame.time.Clock()

    # Function to handle drawing of assets
    def redrawWindow():
        VIEW_WINDOW.blit(BACKGROUND, (0,0))
        # Draw Text
        LivesLabel = mainFont.render(f"Lives:{lives}", 1, (255, 255, 255))
        LevelLabel = mainFont.render(f"Level:{level}", 1, (255, 255, 255))
        VIEW_WINDOW.blit(LivesLabel, (10,10))
        VIEW_WINDOW.blit(LevelLabel, (WIDTH - LevelLabel.get_width() - 10,10))
        # Update display with redrawn assets
        pygame.display.update()

    while run:
        clock.tick(fps)
        redrawWindow()
        # Check for events
        for event in pygame.event.get():
            # Check for quit
            if event.type == pygame.QUIT:
                run = False

# Run Main
main()



