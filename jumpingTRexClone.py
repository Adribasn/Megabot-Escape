import pygame, sys
import random

#Global variables
screenWidth = 1280
screenHeight = 720
score = 0
collisionTolerance = 10

groundRectHeight = 250

enemyVelocity = 5
enemyWidth = 32
enemyHeight = 64

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.width = 32
        self.height = 64
        self.y = y - self.height
        self.jumping = False
        self.originalYvelocity = 10
        self.yVelocity = self.originalYvelocity 
        self.gravity = .25
    
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
        self.width = enemyWidth
        self.height = enemyHeight
        self.x = screenWidth
        self.y = screenHeight - groundRectHeight - self.height
    
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    keysPressed = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (0, screenHeight - groundRectHeight, screenWidth, groundRectHeight))
    
    player.jump()
    player.draw()

    enemyDistanceCounter += 1

    if enemyDistanceCounter == enemyDistance:
        enemyList.append(Enemy())
        enemyDistanceCounter = 0
        enemyDistance = random.randint(75, 225)
    
    playerRect = pygame.Rect(player.x, player.y, player.width, player.height)
    for enemy in enemyList:
        enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        if checkCollision(playerRect, enemyRect):
            score = 0
            enemyList = []

        if enemy.x > -enemyWidth:
            enemy.draw()
            enemy.x -= 3.5
        else:
            enemyList = enemyList[1:]
    
    score += 1
    print(str(score))
    pygame.display.update()
    clock.tick(144)
    