import pygame

class Bullet:
    picture = pygame.image.load("bullet.png")
    picture = pygame.transform.scale(picture, (10,30))
    rect = picture.get_rect()

    def __init__(self, x, y):
        self.rect.update(x, y, 20, 60)

    def move(self):
        self.rect.y = self.rect.y - 50
