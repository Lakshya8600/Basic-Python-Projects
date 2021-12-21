import pygame
import time
import random
pygame.init()

display_width = 1000
display_height = 560
background = pygame.image.load('background.jpg')
background2 = pygame.image.load('background2.jpg')
background3 = pygame.image.load('background3.jpg')
base = pygame.image.load('base.png')
king = pygame.image.load('king2.png')
king = pygame.transform.flip(king,True,False)
shield = pygame.image.load('shield1.png')
apple = pygame.image.load('apple.png')
applegreen = pygame.image.load('applegreen.png')
banana = pygame.image.load('banana.png')
grapes = pygame.image.load('grapes.png')
orange = pygame.image.load('orange.png')
blast = pygame.image.load('boom.png')
fruitlist = [apple,applegreen,banana,grapes,orange]
fruit = random.choice(fruitlist)
fruitx = random.randint(100,900)
bgtype = 0
fruity = -30
shieldx = 50

gamedisplays = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SAVE THE KING")
clock = pygame.time.Clock()


def backgroundfunc():
    if bgtype == 0:
        gamedisplays.blit(background,(0,0))
        gamedisplays.blit(base,(0,500))
    elif bgtype == 1:
        gamedisplays.blit(background2,(0,0))
        gamedisplays.blit(base,(0,500))
    elif bgtype == 2 :
        gamedisplays.blit(background3,(0,0))
        gamedisplays.blit(base,(0,500))
def kingfunc(kingx):
    gamedisplays.blit(king,(kingx,397))          
def shieldfunc(shieldx):
    gamedisplays.blit(shield,(shieldx,320))
def fruitfunc():
    global fruit
    global fruity
    global fruitx
    gamedisplays.blit(fruit,(fruitx,fruity))
    if fruity == 500:
        fruity = 0
        fruit = random.choice(fruitlist)
        fruitx = random.randint(100,900)


    if fruitx > shieldx and fruitx < shieldx+150 and fruity + 51 > 320 and fruity + 51 > 370 and 150 + 50 < fruity :
        fruit = pygame.image.load('boom.png')
        gamedisplays.blit(fruit,(fruitx,fruity))
        # fruity = 

def game_loop():
    global bgtype
    global fruity
    global shieldx
    bumped = False
    kingx = 50
    kingvelocity = 2
    shieldvelocity = 0
    fruitvelocity = 5
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shieldvelocity = -5

            if event.key == pygame.K_RIGHT:
                shieldvelocity = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                shieldvelocity = 0

        if kingx == 1010 and bgtype == 0:
            kingx = 50
            bgtype = 1
        elif kingx == 1010 and bgtype == 1:
            kingx = 50
            bgtype = 2
        elif kingx == 1010 and bgtype == 2:
            kingx = 50
            bgtype = 0

        if shieldx < 5:
            shieldvelocity = 0
            shieldx = 5
        if shieldx>867:
            shieldvelocity = 0
            shieldx = 867

        kingx += kingvelocity
        shieldx += shieldvelocity
        
        backgroundfunc()
        kingfunc(kingx)
        shieldfunc(shieldx)
        fruitfunc()
        fruity += fruitvelocity

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
