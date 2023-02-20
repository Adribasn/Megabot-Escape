import pygame, sys
import random
import math

#Global variables
screenWidth = 1280
screenHeight = 720
score = 0
collisionTolerance = 15
gameRunning = False
gameHasRun = False

groundRectHeight = 250

gameVelocity = 7

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()

background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (269, 470))
backgroundMultiples = math.ceil(screenWidth / background.get_width()) 
backgroundX = screenWidth

foreground0 = pygame.image.load('assets/tilemap/tile001.png')
foreground1 = pygame.image.load('assets/tilemap/tile003.png')
foreground2 = pygame.image.load('assets/tilemap/tile005.png')
foreground3 = pygame.image.load('assets/tilemap/tile008.png')
foreground4 = pygame.image.load('assets/tilemap/tile006.png')
foreground5 = pygame.image.load('assets/tilemap/tile019.png')
foreground5 = pygame.transform.scale(foreground5, (64, 64))
foreground6 = pygame.image.load('assets/tilemap/tile021.png')
foreground7 = pygame.image.load('assets/tilemap/tile023.png')
foreground8 = pygame.image.load('assets/tilemap/tile024.png')
foreground9 = pygame.image.load('assets/tilemap/tile026.png')
foreground10 = pygame.image.load('assets/tilemap/tile028.png')
foreground10 = pygame.transform.scale(foreground10, (64, 64))
foreground11 = pygame.image.load('assets/tilemap/tile010.png')
foreground12 = pygame.image.load('assets/tilemap/tile036.png')
foreground13 = pygame.image.load('assets/tilemap/tile037.png')
foreground14 = pygame.image.load('assets/tilemap/tile039.png')
foreground15 = pygame.image.load('assets/tilemap/tile040.png')
foreground16 = pygame.image.load('assets/tilemap/tile041.png')

foregroundTilemap = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

playerIdle = pygame.image.load('assets\player\idle.png')
playerIdle = pygame.transform.scale(playerIdle, (64, 64))

playerRun1 = pygame.image.load('assets/player/run1.png')
playerRun2 = pygame.image.load('assets/player/run2.png')
playerRun3 = pygame.image.load('assets/player/run2.png')
playerRun4 = pygame.image.load('assets/player/run2.png')

playerRunFrames = [pygame.transform.scale(frame, (64, 64)) for frame in [playerRun1, playerRun2, playerRun3, playerRun4]]
playerRunFrame = 0

playerJump = pygame.image.load('assets\player\jump.png')
playerJump = pygame.transform.scale(playerJump, (64, 64))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.width = 64
        self.height = 64
        self.y = y - self.height
        self.jumping = False
        self.originalYvelocity = 18.75
        self.yVelocity = self.originalYvelocity 
        self.gravity = .75
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
    
    def jump(self):
        if keysPressed[pygame.K_SPACE]:
            self.jumping = True
        
        if self.jumping:
            self.y -= self.yVelocity
            self.yVelocity -= self.gravity

            
            if self.yVelocity < -self.originalYvelocity:
                self.jumping = False
                self.yVelocity = self.originalYvelocity

class Enemy:
    def __init__(self):
        self.dimensionList = [[42, 76], [24, 48], [64, 48]]
        self.randomDimensions = random.randint(0, 2)
        self.width = self.dimensionList[self.randomDimensions][0]
        self.height = self.dimensionList[self.randomDimensions][1]
        self.x = screenWidth
        self.y = screenHeight - groundRectHeight - self.height
    
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

class Tile:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y

def checkCollision(rect1, rect2):
    if rect1.colliderect(rect2):
        if abs(rect1.right) - abs(rect2.left) < collisionTolerance:
            return True
        if abs(rect1.bottom) - abs(rect2.top) < collisionTolerance:
            return True
    
player = Player(100, screenHeight - groundRectHeight)

enemyDistance = random.randint(75, 225)
enemyDistanceCounter = 0

enemyList = []
backgroundList = [Tile(background, background.get_width() * i, 0) for i in range(backgroundMultiples)]

foregroundList = []
for j in range(len(foregroundTilemap)):
    tileList = []
    for i in range(len(foregroundTilemap[j])):
        if foregroundTilemap[j][i] == 5:
            tileList.append(Tile(foreground5, foreground5.get_width() * i, (screenHeight - groundRectHeight)))
        elif foregroundTilemap[j][i] == 10:
            tileList.append(Tile(foreground10, foreground10.get_width() * i, (screenHeight - groundRectHeight) + (j * 64)))

    foregroundList.append(tileList)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    keysPressed = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    for item in backgroundList:
        screen.blit(item.sprite, (item.x, item.y))
    
    for l in foregroundList:
        for tile in l:
            screen.blit(tile.sprite, (tile.x, tile.y))

    if gameHasRun == False and gameRunning == False:
        screen.blit(playerIdle, (player.x, player.y))

        if keysPressed[pygame.K_SPACE]:
            gameRunning = True
    elif gameHasRun == True and gameRunning == False:
        print('Press R to replay')
        if keysPressed[pygame.K_r]:
            score = 0
            enemyList = []
            gameRunning = True

    if gameRunning:
        gameHasRun = True

        if backgroundList[0].x < -background.get_width():
            backgroundList = backgroundList[1:]
        elif backgroundList[-1].x < screenWidth - background.get_width():
            backgroundList.append(Tile(background, backgroundList[-1].x + background.get_width(), 0))
        
        for item in backgroundList:
            item.x -= 1

        for j in range(len(foregroundList)):
            if foregroundList[j][0].x < -foregroundList[j][0].sprite.get_width():
                foregroundList[j] = foregroundList[j][1:]
            elif foregroundList[j][-1].x < screenWidth:
                foregroundList[j].append(Tile(foregroundList[j][-1].sprite, foregroundList[j][-1].x + foregroundList[j][-1].sprite.get_width(), foregroundList[j][-1].y))

            for i in foregroundList[j]:
                i.x -= gameVelocity

        if player.jumping:
            screen.blit(playerJump, (player.x, player.y))
        else:
            screen.blit(playerRunFrames[int(playerRunFrame)], (player.x, player.y))
            playerRunFrame += .15

            if int(playerRunFrame) == len(playerRunFrames):
                playerRunFrame = 0
        
        player.jump()

        enemyDistanceCounter += 1

        if enemyDistanceCounter == enemyDistance:
            enemyList.append(Enemy())
            enemyDistanceCounter = 0
            enemyDistance = random.randint(75, 225)
        
        playerRect = pygame.Rect(player.x, player.y, player.width, player.height)
        for enemy in enemyList:
            enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            if checkCollision(playerRect, enemyRect):
                gameRunning = False

            if enemy.x > -enemy.width:
                enemy.draw()
                enemy.x -= gameVelocity
            else:
                enemyList = enemyList[1:]
        
        score += .1
        #print(str(int(score)))

    pygame.display.update()
    clock.tick(60)
    