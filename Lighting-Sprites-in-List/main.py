import pygame
from settings import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Global variables
squares = []

for i in range(NUMSQUARES):
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.Surface( (SQSIZE, SQSIZE) )
    sprite.image.fill(SQCOLORS[i])
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = SQSIZE * i
    sprite.glowTimer = 0
    sprite.clickedOn = False
    squares.append(sprite)

def update():
    for i in range(NUMSQUARES):
        square = squares[i]
        if square.glowTimer > 0:
            square.glowTimer -= 1
        
def draw():
    screen.fill(BGCOLOR)
    drawsquares()
    pygame.display.update()

def drawsquares():
    for i in range(NUMSQUARES):
        rect = pygame.Rect(i * SQSIZE,
                           0, SQSIZE, SQSIZE)
        pygame.draw.rect(screen, SQCOLORS[i], rect, width = 5)  
        if squares[i].glowTimer > 0 or squares[i].clickedOn == True:
            screen.blit(squares[i].image, squares[i].rect)
            
def onMousePress(x, y):
    indexOfClick = x // SQSIZE
    squares[indexOfClick].clickedOn = True
#     for square in squares:
#         if square.rect.collidepoint(x, y):
#             square.clickedOn = True
def onMouseRelease(x, y):
    for square in squares:
        square.clickedOn = False

def onMouseMove(x, y):
    pass

def onKeyPress(key):
    pass

def onKeyRelease(key):
    pass

def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        update()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                onMouseMove(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                onMousePress(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                onMouseRelease(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN:
                onKeyPress(event.key)
            elif event.type == pygame.KEYUP:
                onKeyRelease(event.key)
        clock.tick(FPS)


pygame.init()
mainloop()
