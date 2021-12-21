import pygame
import time
import random
pygame.init()

grey = (166, 171, 179)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CAR GAME")
clock = pygame.time.Clock()
carwidth = 74
carimg = pygame.image.load('car.png')
side = pygame.image.load('side.jpg')
road = pygame.image.load('road.png')
line = pygame.image.load('line.png')
obs_startx = random.randint(180,520)
obs_starty = -200
obs_width = 74
obs_height = 149
bumped = False
obs = random.randint(1, 6)
score = 0
hiscore = 0
bgcount = 1

def obstacle(carx,cary):
    global score
    global obs_startx
    global obs_starty
    global obs
    obslist = [[1,"ob1.png"],[2,"ob2.png"],[3,"ob3.png"],[4,"ob4.png"],[5,"ob5.png"],[6,"ob6.png"]]
    for a,ob in obslist:
        if obs==a:
            car_pic = pygame.image.load(ob)

    gamedisplays.blit(car_pic,(obs_startx,obs_starty))

    if obs_starty > display_height:
        obs_starty = -200
        obs_startx = random.randint(180,580)
        obs = random.randint(1, 6)
        score += 1

    if cary < obs_starty + obs_height:
        if carx > obs_startx and carx < obs_startx + obs_width or carx + carwidth > obs_startx and carx + carwidth < obs_startx + obs_width:
            crash()
            bumped = True
def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()
def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 70)
    textsurf,textrect = text_objects(text,largetext)
    textrect.center = (int((display_width/2)),int((display_height/2)))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()
    bumped = True
    # game_loop()
def score_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 30)
    textsurf,textrect = text_objects(text,largetext)
    textrect.center = (68,72)
    gamedisplays.blit(textsurf,textrect)
    textsurf, textrect = text_objects(f"Highscore : {hiscore}", largetext)
    textrect.center = (100,30)
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
def crash():
    message_display("YOU CRASHED")
def car(x,y):
     gamedisplays.blit(carimg,(x,y))
def background():
    global bgcount
    gamedisplays.blit(side, (-10, 0))
    gamedisplays.blit(side, (640, 0))
    gamedisplays.blit(line, (170, 0))
    gamedisplays.blit(line, (625, 0))
    gamedisplays.blit(road, (360, 20))
    gamedisplays.blit(road, (360, 120))
    gamedisplays.blit(road, (360, 230))
    gamedisplays.blit(road, (360, 340))
    gamedisplays.blit(road, (360, 450))
    gamedisplays.blit(road, (360, 560))

def hiiscore():
    global hiscore
    cs = open("gm.txt","rt")
    hiscore = int(cs.read())
    cs.close()
    if score>hiscore:
        f = open("gm.txt","wt")
        f.write(str(score))
        hiscore = score
        f.close()

def game_loop():
    global bumped
    global obs_starty
    global obs_startx
    global obs
    global hiscore
    obstacle_speed = 6
    y_change = 0
    
    carx = int((display_width*0.45))
    cary = int((display_height*0.7))
    xchange = 0
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -5

            if event.key == pygame.K_RIGHT:
                xchange = 5

            if event.key == pygame.K_q:
                obstacle_speed+=0.25
                # print(obstacle_speed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                xchange = 0
        if carx<170:
            carx = 175
        if carx+carwidth>625:
            carx = 550

        gamedisplays.fill(grey)
        carx+=xchange
        background()
        car(carx, cary)
        obstacle(carx,cary)
        hiiscore()
        score_display(f"Score : {score}")

        obs_starty += obstacle_speed
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
