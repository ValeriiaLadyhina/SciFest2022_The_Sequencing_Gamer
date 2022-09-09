import pygame
from sys import exit #module that closes any code entirely

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('cdt')
clock = pygame.time.Clock() #object that will be use for the framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert() #Convert the image to something python can run easily
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #keep the alpha values of a png
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #take a surface and draw a rectangle on it

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):print('collision !')

    screen.blit(sky_surface,(0,0)) #blit = block image transfer (put a surface on another)
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect): #return 0 or 1 depending on if there is a collision
    #     print('collision')
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60) #the loop cannot run faster thatn 60 fps