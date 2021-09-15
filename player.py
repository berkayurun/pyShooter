import pygame

class Player:
    picture = pygame.image.load("player.png")
    picture = pygame.transform.scale(picture, (46, 78))
    rect = picture.get_rect()

    def __init__(self, startX, startY):
        self.rect.update(startX, startY, 46, 78)
        
