# Abstract class for general ship declaration
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImg = None
        self.lasersImg = None
        self.lasers = []
        self.coolDownCounter = 0

    def draw(self, window):
        window.blit(self.shipImg, (self.x, self.y))

    def get_width(self):
        return self.shipImg.get_width()

    def get_height(self):
        return self.shipImg.get_height()