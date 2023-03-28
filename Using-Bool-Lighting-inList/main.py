import pygame
from settings import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Global variables
squares = []

for i in range(NUMSQUARES):
    squares.append(False)

def update():
    pass
def draw():
    screen.fill(BGCOLOR)
    drawSquares()
    pygame.display.update()
def drawSquares():
    for i in range(NUMSQUARES):
        rect = pygame.Rect(i * SQSIZE,
                           0, SQSIZE, SQSIZE)
        if squares[i] == True:
            pygame.draw.rect(screen, SQCOLORS[i], rect)  
        else:
            pygame.draw.rect(screen, SQCOLORS[i], rect, width = 5)  
        
def onMousePress(x, y):
    indexOfClick = x // SQSIZE
    squares[indexOfClick] = True

def onMouseRelease(x, y):
    for i in range(NUMSQUARES):
        squares[i] = False

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
