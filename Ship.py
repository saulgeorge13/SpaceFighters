import Assets
import Laser
# Abstract class for general ship declaration
class Ship:
    COOLDOWN = 30

    # Constructor for ship abstract class
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImg = None
        self.laserImg = None
        self.lasers = []
        self.coolDownCounter = 0

    # Draw ship and lasers
    def draw(self, window):
        window.blit(self.shipImg, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(Assets.viewWindow)

    # Basic get methods
    def get_width(self):
        return self.shipImg.get_width()

    def get_height(self):
        return self.shipImg.get_height()

    # Methods dealing with shooting cooldown
    def cooldown(self):
        if self.coolDownCounter >= self.COOLDOWN:
            self.coolDownCounter = 0
        elif self.coolDownCounter > 0:
            self.coolDownCounter += 1

    # Method to shoot laser
    def shoot(self):
        if self.coolDownCounter == 0:
            laser = Laser.Laser(self.x, self.y, self.laserImg)
            self.lasers.append(laser)
            self.coolDownCounter = 1

    # Laser movement and checks if it hits a player
    def move_lasers(self, velocity, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.offscreen(Assets.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)


