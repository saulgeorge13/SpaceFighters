import pygame
import Assets
import Ship

# Enemy class inherits from ship
class Enemy(Ship.Ship):
    # Map to store characteristics
    COLOR_MAP = {
        "red": (Assets.RED_SPACE_SHIP, Assets.RED_LASER),
        "green": (Assets.GREEN_SPACE_SHIP, Assets.GREEN_LASER),
        "blue": (Assets.BLUE_SPACE_SHIP, Assets.BLUE_LASER)
    }
    # Constructor for enemy class
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.color = color
        self.shipImg, self.laserImg = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.shipImg)

    def move(self, velocity):
        self.y += velocity

