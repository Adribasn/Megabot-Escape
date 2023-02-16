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

bgPosX = 0
bgVelocity = 2 #must be an even number
def drawBackground():
    global bgPosX
    print(str(bgPosX))
    print(str(-screenWidth))
    print('-------')
    pygame.draw.rect(screen, (0, 0, 255), (bgPosX, 0, screenWidth, screenHeight))
    pygame.draw.rect(screen, (255, 0, 0), (screenWidth + bgPosX, 0, screenWidth, screenHeight))

    if bgPosX == -screenWidth:
        bgPosX = 0
    
    bgPosX -= bgVelocity

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))
    drawBackground()
    pygame.display.update()
    clock.tick(60)
    