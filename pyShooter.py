import pygame
import player
import Level
import time
import bullet as b

pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)

player = player.Player(640, 620)
playerRect = player.rect

level = Level.Level()
levelRect = level.background.get_rect()

bullets = []

def visualUpdate():
    screen.fill(black)
    screen.blit(level.background, levelRect)
    screen.blit(player.picture, playerRect)
    
    for bullet in bullets:
        screen.blit(bullet.picture, bullet.rect)

    pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerRect.move_ip(-10, 0)
            elif event.key == pygame.K_d:
                playerRect.move_ip(10, 0)
            elif event.key == pygame.K_w:
                bullet = b.Bullet(playerRect.x, playerRect.y)
                bullets.append(bullet)
    
    for bullet in bullets:
        if bullet.rect.y < 0:
            bullets.remove(bullet)
        bullet.move()

    visualUpdate()


