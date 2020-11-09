# Abstract class for general ship declaration
class Ship:
    # Constructor for ship abstract class
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImg = None
        self.lasersImg = None
        self.lasers = []
        self.coolDownCounter = 0

    # Draw ship at its current position
    def draw(self, window):
        window.blit(self.shipImg, (self.x, self.y))

    # Basic get methods
    def get_width(self):
        return self.shipImg.get_width()

    def get_height(self):
        return self.shipImg.get_height()