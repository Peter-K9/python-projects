
from tkinter.tix import DirTree
import pygame
from pygame.locals import *
import time 
import random

snakeSpeed = 15

window_x = 720
window_y = 480

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snakePosition = [100, 50]
snakeBody = [   [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
]

fruitPostition = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

fruitSpawn = True

direction = 'RIGHT'
change_to = direction



score = 0

def displayScore(choice, color, font, size):
    scoreFont = pygame.font.SysFont(font, size)
    scoreSurface = scoreFont.render('Score : ' + str(score), True, color)
    scoreRect = scoreSurface.get_rect()
    game_window.blit(scoreSurface, scoreRect)

def gameOver():
    myFont = pygame.font.SysFont('timese new roman', 50)
    gameOverSurface = myFont.render('Your score is ' + str(score), True, red)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (window_x/2, window_y/4)
    game_window.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snakePosition[1] -= 10
    if direction == 'DOWN':
        snakePosition[1] += 10
    if direction == 'LEFT':
        snakePosition[0] -= 10
    if direction == 'RIGHT':
        snakePosition[0] += 10

    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == fruitPostition[0] and  snakePosition[1] == fruitPostition[1]:
        score += 10
        fruitSpawn = False
    else:
        snakeBody.pop()
    
    if not fruitSpawn:
        fruitPostition = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]


    fruitSpawn = True
    game_window.fill(black)

    for pos in snakeBody:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))    

    pygame.draw.rect(game_window, white, pygame.Rect(
      fruitPostition[0], fruitPostition[1], 10, 10))


    if snakePosition[0] < 0 or snakePosition[0] > window_x-10:
        gameOver()
    if snakePosition[1]< 0 or snakePosition[1] > window_y-10:
        gameOver()

    for block in snakeBody[1:]:
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            gameOver()

    displayScore(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snakeSpeed)        














   




