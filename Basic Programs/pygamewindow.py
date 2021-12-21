import pygame
#important
pygame.init()
#creating window
pygame.display.set_mode((1111,111))
#creating window name
pygame.display.set_caption("MY FIRST GAME")

#game specific variable
game_exit = False
game_over = False

#game loop
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            game_exit = True


#after gameloop
pygame.quit
quit