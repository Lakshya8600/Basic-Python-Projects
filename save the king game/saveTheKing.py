import pygame
import time
import random
pygame.init()

display_width = 1000
display_height = 560
background = pygame.image.load('background.jpg')
base = pygame.image.load('base.png')
king = pygame.image.load('king2.png')

gamedisplays = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SAVE THE KING")
clock = pygame.time.Clock()

def backgroundfunc():
    gamedisplays.blit(background,(0,0))
    gamedisplays.blit(base,(0,500))

def kingfunc(kingx):
    gamedisplays.blit(king,(kingx,397))

def game_loop():
    bumped = False
    while not bumped:
        kingx = 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

        backgroundfunc()
        kingfunc(kingx)
        pygame.display.update()


game_loop()
pygame.quit()
quit()
