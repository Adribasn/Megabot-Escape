import pygame, sys

#Global variables
screenWidth = 1280
screenHeight = 720
gameVelocity = 1

collisionTolerance = 10

groundRectHeight = 250
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.height = 32
        self.width = 32
        self.y = y - self.height
        self.jumping = False
        self.jumpHeight = 20
        self.yVelocity = self.jumpHeight
        self.gravity = 1
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
    
    def jump(self):
        if keysPressed[pygame.K_SPACE]:
            self.jumping = True
        
        if self.jumping:
            self.y -= self.yVelocity
            self.yVelocity -= self.gravity

            if self.yVelocity < -self.jumpHeight:
                self.jumping = False
                self.yVelocity = self.jumpHeight

class Enemy:
    pass

def checkCollision(rect1, rect2):
    if rect1.colliderect(rect2):
        if abs(rect1.right) - abs(rect2.left) < collisionTolerance:
            return True
        if abs(rect1.bottom) - abs(rect2.top) < collisionTolerance:
            return True

player = Player(50, screenHeight - groundRectHeight)
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
    pygame.display.update()
    clock.tick(60)
    