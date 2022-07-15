import pygame
from sys import exit #module that closes any code entirely

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('cdt')
clock = pygame.time.Clock() #object that will be use for the framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png').convert() #Convert the image to something python can run easily
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0)) #blit = block image transfer (put a surface on another)
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,265))

    pygame.display.update()
    clock.tick(60) #the loop cannot run faster thatn 60 fps