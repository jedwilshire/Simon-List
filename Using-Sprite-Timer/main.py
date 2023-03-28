import pygame
from settings import *
import settings
from random import randrange

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Global variables
squares = []
solution = []
response = []

for i in range(NUMSQUARES):
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.Surface( (SQSIZE, SQSIZE) )
    sprite.image.fill(SQCOLORS[i])
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = SQSIZE * i
    sprite.glowTimer = 0
    squares.append(sprite)

def update():
    #print(response, solution)
    #turnOffSquares()
    if len(solution) < PUZZLESIZE:
        makePuzzle()
    if len(response) == PUZZLESIZE:
        checkForWin()
        
def checkForWin():
    win = True
    for i in range(PUZZLESIZE):
        if solution[i] != response[i]:
            win = False
    if win == True:
        for i in range(NUMSQUARES):
            sprite.glowTimer = 30
    else:
        turnOffSquares()
        
def squareIsOn():
    for i in range(NUMSQUARES):
        if sprite.glowTimer > 0:
            return True
    return False

        
def makePuzzle():
    turnOnRandomSquare()
        
def turnOnRandomSquare():
    randIndex = randrange(0, NUMSQUARES)
    solution.append(randIndex)
    sprite.glowTimer = 30

def draw():
    screen.fill(BGCOLOR)
    drawsquares()
    pygame.display.update()

def drawsquares():
    for i in range(NUMSQUARES):
        rect = pygame.Rect(i * SQSIZE,
                           0, SQSIZE, SQSIZE)
        pygame.draw.rect(screen, SQCOLORS[i], rect, width = 3)  
        if squares[i].glowTimer > 0:
            screen.blit(squares[i].image, squares[i].rect)
            squares[i].glowTimer -= 1
            
def onMousePress(x, y):
    indexOfClick = x // SQSIZE
    response.append(indexOfClick)
    squares[indexOfClick].glowTimer = 30
    
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
            elif event.type == pygame.KEYDOWN:
                onKeyPress(event.key)
            elif event.type == pygame.KEYUP:
                onKeyRelease(event.key)
        clock.tick(FPS)


pygame.init()
mainloop()
