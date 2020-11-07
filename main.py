import pygame
import os
import time
import random
import Assets
import Player
import Ship

pygame.font.init()


# Main Function
def main():
    run = True
    fps = 60
    level = 1
    lives = 3
    mainFont = pygame.font.SysFont("calibri", 50)
    playerVelocity = 5
    player = Player.Player(300, 650)

    clock = pygame.time.Clock()

    # Function to handle drawing of assets
    def redrawWindow():
        Assets.viewWindow.blit(Assets.BACKGROUND, (0, 0))
        # Draw Text
        LivesLabel = mainFont.render(f"Lives:{lives}", 1, (255, 255, 255))
        LevelLabel = mainFont.render(f"Level:{level}", 1, (255, 255, 255))
        Assets.viewWindow.blit(LivesLabel, (10, 10))
        Assets.viewWindow.blit(LevelLabel, (Assets.WIDTH - LevelLabel.get_width() - 10, 10))
        # Draw the ship
        player.draw(Assets.viewWindow)
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
        # Check for key presses and move ship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and (player.x - playerVelocity > 0):
            player.x -= playerVelocity
        if keys[pygame.K_d] and (player.x + playerVelocity + player.get_width() < Assets.WIDTH):
            player.x += playerVelocity
        if keys[pygame.K_w] and (player.y - playerVelocity > 0):
            player.y -= playerVelocity
        if keys[pygame.K_s] and (player.y + playerVelocity + player.get_height() < Assets.HEIGHT):
            player.y += playerVelocity


# Run Main
main()
