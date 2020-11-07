import pygame
import Assets
import Ship


# Player Class inherits from Ship
class Player(Ship.Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.shipImg = Assets.PLAYER_SPACE_SHIP
        self.laserImg = Assets.PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.shipImg)
        self.maxHealth = health

