import pygame, sys

#Global variables
screenHeight = 1080
screenWidth = 1920

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    pygame.display.update()