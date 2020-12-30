import pygame

# Laser class
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        self.y += velocity

    def offscreen(self, height):
        return not (self.y >= 0 and self.y <= height)

    def collision(self, obj):
        return collide(obj, self)


# Collide function
def collide(obj1, obj2):
    offsetX = obj2.x - obj1.x
    offsetY = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offsetX, offsetY)) is not None
