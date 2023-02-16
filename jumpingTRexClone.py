import pygame, sys

#Global variables
screenWidth = 1280
screenHeight = 720
gameVelocity = 1

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

class Player:
    pass

class Enemy:
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))
    drawBackground()
    pygame.display.update()
    clock.tick(60)
    