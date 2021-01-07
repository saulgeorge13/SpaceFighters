import pygame
import os
import time
import random
import Assets
import Player
import Enemy
import Ship
import Laser

pygame.font.init()


# Main Function
def main():
    run = True
    fps = 60
    level = 0
    lives = 3
    lost = False
    lostCount = 0
    mainFont = pygame.font.SysFont("calibri", 50)
    lostFont = pygame.font.SysFont("calibri", 75)

    enemies = []
    waveLength = 0
    enemyVelocity = 1
    laserVelocity = 5

    playerVelocity = 5
    player = Player.Player(300, 650)

    clock = pygame.time.Clock()

    # Function to handle drawing of assets
    def redrawWindow():
        Assets.viewWindow.blit(Assets.BACKGROUND, (0, 0))

        # Draw Text
        livesLabel = mainFont.render(f"Lives:{lives}", 1, (255, 255, 255))
        levelLabel = mainFont.render(f"Level:{level}", 1, (255, 255, 255))
        Assets.viewWindow.blit(livesLabel, (10, 10))
        Assets.viewWindow.blit(levelLabel, (Assets.WIDTH - levelLabel.get_width() - 10, 10))

        # Draw all enemies
        for enemy in enemies:
            enemy.draw(Assets.viewWindow)

        # Draw the ship
        player.draw(Assets.viewWindow)

        # Draw loss screen
        if lost:
            lostLabel = lostFont.render("You Lost!", 1, (255, 255, 255))
            Assets.viewWindow.blit(lostLabel, (Assets.WIDTH / 2 - lostLabel.get_width() / 2, Assets.HEIGHT / 2))

        # Update display with redrawn assets
        pygame.display.update()

    while run:
        clock.tick(fps)
        redrawWindow()

        # Check if game is lost
        if lives < 0:
            lost = True
            lostCount += 1
        if lost:
            if lostCount > fps * 5:
                run = False
            else:
                continue

        # Spawn enemies after updating to level
        if len(enemies) == 0:
            level += 1
            waveLength += 5
            for i in range(waveLength):
                enemy = Enemy.Enemy(random.randrange(50, Assets.WIDTH - 50), random.randrange(-1500, -100),
                                    random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        # Check for events
        for event in pygame.event.get():

            # Check for quit
            if event.type == pygame.QUIT:
                run = False

        # PLayer ship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and (player.x - playerVelocity > 0):
            player.x -= playerVelocity
        if keys[pygame.K_d] and (player.x + playerVelocity + player.get_width() < Assets.WIDTH):
            player.x += playerVelocity
        if keys[pygame.K_w] and (player.y - playerVelocity > 0):
            player.y -= playerVelocity
        if keys[pygame.K_s] and (player.y + playerVelocity + player.get_height() < Assets.HEIGHT):
            player.y += playerVelocity

        # Laser shooting
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Enemy ship movement
        for enemy in enemies:
            enemy.move(enemyVelocity)
            enemy.move_lasers(laserVelocity, player)

            # Enemy shooting probability
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            # Enemy collision or breach
            if Laser.collide(enemy, player):
                player.health -= 10
                if player.health == 0:
                    player.health = 100
                    lives -= 1
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > Assets.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laserVelocity, enemies)


# Main Menu function
def main_menu():
    title_font = pygame.font.SysFont("calibri", 70)
    run = True
    while run:
        Assets.viewWindow.blit(Assets.BACKGROUND, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        Assets.viewWindow.blit(title_label, (Assets.WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
