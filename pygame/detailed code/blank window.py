import pygame
from sys import exit #module that closes any code entirely

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("cdt")
clock = pygame.time.Clock() #object that will be use for the framerate

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60) #the loop cannot run faster thatn 60 fps