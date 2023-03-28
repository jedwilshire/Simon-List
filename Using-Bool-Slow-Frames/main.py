import pygame
from settings import *
import settings
from random import randrange

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Global variables
simonSquares = []
solution = []
response = []

for i in range(NUMSQUARES):
    simonSquares.append(False)

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
            simonSquares[i] = True
    else:
        turnOffSquares()
        
def squareIsOn():
    for i in range(NUMSQUARES):
        if simonSquares[i] == True:
            return True
    return False

def turnOffSquares():
    for i in range(NUMSQUARES):
        simonSquares[i] = False
        
def makePuzzle():
    if squareIsOn():
        turnOffSquares()
    else:
        turnOnRandomSquare()
        
def turnOnRandomSquare():
    randIndex = randrange(0, NUMSQUARES)
    solution.append(randIndex)
    simonSquares[randIndex] = True

def draw():
    screen.fill(BGCOLOR)
    drawSimonSquares()
    pygame.display.update()

def drawSimonSquares():
    for i in range(NUMSQUARES):
        rect = pygame.Rect(i * SQSIZE,
                           0, SQSIZE, SQSIZE)
        if simonSquares[i] == True:
            pygame.draw.rect(screen, SQCOLORS[i], rect)
        else:
            pygame.draw.rect(screen, SQCOLORS[i], rect, width = 3)
            
def onMousePress(x, y):
    indexOfClick = x // SQSIZE
    response.append(indexOfClick)
    turnOffSquares()
    simonSquares[indexOfClick] = True
    
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
