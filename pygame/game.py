import random

import pygame
from math import ceil
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 10, 0))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= sky_height:
            self.gravity = -30  # jump
            self.jump_sound.play()
        #  if keys[pygame.K_RIGHT] and self.rect.right <= (SCREEN_WIDTH-50):
        #    self.rect.x += 3
        #  if keys[pygame.K_LEFT] and self.rect.left >= 50:
        #    self.rect.x -= 3

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= sky_height:
            self.rect.bottom = sky_height

    def animation_state(self):
        if self.rect.bottom < sky_height:
            self.image = self.player_jump
        else:
            self.player_index += 0.1  # we are slowly increase the index so the animation is slower
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.apply_gravity()
        self.player_input()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type_of_nucleotide):
        super().__init__()

        if type_of_nucleotide == 'A':
            a_frame_1 = pygame.image.load('graphics/nucleotides/A.png').convert_alpha()
            self.frames = [a_frame_1]
            y_pos = sky_height
        elif type_of_nucleotide == 'T':
            t_frame_1 = pygame.image.load('graphics/nucleotides/T.png').convert_alpha()
            self.frames = [t_frame_1]
            y_pos = sky_height
        elif type_of_nucleotide == 'C':
            c_frame_1 = pygame.image.load('graphics/nucleotides/C.png').convert_alpha()
            self.frames = [c_frame_1]
            y_pos = sky_height
        elif type_of_nucleotide == 'G':
            g_frame_1 = pygame.image.load('graphics/nucleotides/G2.png').convert_alpha()
            self.frames = [g_frame_1]
            y_pos = sky_height
        else:
            n_frame_1 = pygame.image.load('graphics/nucleotides/N.png').convert_alpha()
            self.frames = [n_frame_1]
            y_pos = sky_height

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(1490, y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6


def collision_sprite(k_mer_start):
    k_mer_start2 = k_mer_start
    #   print ("1 k_mer_start2 ",   k_mer_start2)
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True):
        sequence.append(nucleotides[-3])
        obstacle_group.remove()
        k_mer_start2 = k_mer_start2 + 1
        #   print ("2 k_mer_start2 ",   k_mer_start2)
        #   print ("len(nucleotides) " , len(nucleotides), "nucleotides = ", nucleotides )
        if len(nucleotides) == 1:
            #  this case should only be necessary if the sequence from the dictionary is very short,
            #  which will probably not happen.
            display_complement(nucleotides[-1])
        elif len(nucleotides) == 2:  # same for this case.
            display_complement(nucleotides[-2])
        elif len(nucleotides) > 2:
            display_complement(nucleotides[-3])
        #   print ("3 k_mer_start2 ",   k_mer_start2)
        return True, k_mer_start2
    else:
        score_seq = 0
        if len(sequence) == len(sequence_obj):
            for nucl in range(len(sequence_obj)):
                if sequence[nucl] == 'N':
                    score_seq += 0.5
                elif sequence_obj[nucl] == dictionary_nucleotides[sequence[nucl]]:
                    score_seq += 1
            result_of_sequencing = score_seq * 100 / len(sequence_obj)
            score = 1
            return False, result_of_sequencing
        #   print ("4 k_mer_start2 ",   k_mer_start2)
        return True, k_mer_start2


def winSound():
    winnerSound = pygame.mixer.Sound('audio/winner-bell.aiff')
    winnerSound.set_volume(2)
    winnerSound.play()


def loseSound():
    loseSound1 = pygame.mixer.Sound('audio/bad-beep.mp3')
    loseSound1.set_volume(8)
    loseSound1.play()


def display_complement(collidedNucleotide):
    if collidedNucleotide == 'A':
        collidedNucleotideGraphic = pygame.image.load('graphics/nucleotides/A.png')
        screen.blit(collidedNucleotideGraphic, ((SCREEN_WIDTH / 4) * 3 - 10, 40 + 100 - 20))
    elif collidedNucleotide == 'T':
        collidedNucleotideGraphic = pygame.image.load('graphics/nucleotides/T.png')
        screen.blit(collidedNucleotideGraphic, ((SCREEN_WIDTH / 4) * 3 - 10, 40 + 100 - 20))
    elif collidedNucleotide == 'G':
        collidedNucleotideGraphic = pygame.image.load('graphics/nucleotides/G2.png')
        screen.blit(collidedNucleotideGraphic, ((SCREEN_WIDTH / 4) * 3 - 10, 40 + 60))
    elif collidedNucleotide == 'C':
        collidedNucleotideGraphic = pygame.image.load('graphics/nucleotides/C.png')
        screen.blit(collidedNucleotideGraphic, ((SCREEN_WIDTH / 4) * 3 - 10, 40 + 60))
    elif collidedNucleotide == 'N':
        collidedNucleotideGraphic = pygame.image.load('graphics/nucleotides/N.png')
        screen.blit(collidedNucleotideGraphic, ((SCREEN_WIDTH / 4) * 3 - 10, 40 + 100 - 20))
    pygame.display.update()
    #   print ("k_mer_start ", k_mer_start)
    myk_mer_start2 = collision_sprite(k_mer_start)[1]
    #   print ("myk_mer_start2 ", myk_mer_start2)
    if collision_sprite(k_mer_start)[0]:  # if indeed there was a collision
        myk_mer = sequence_obj[myk_mer_start2]
        if dictionary_nucleotides[myk_mer] == collidedNucleotide:
            winSound()
        elif collidedNucleotide == 'N':
            pass
        else:
            loseSound()

    pygame.time.delay(250)


def display_score():
    k_mer_start2 = collision_sprite(k_mer_start)[1]
    k_mer = sequence_obj[k_mer_start2]
    score_surf = k_mer_font.render(f'Nucleotide:', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH / 2, 100))
    screen.blit(score_surf, score_rect)

    if k_mer == 'A':
        KMER = pygame.image.load('graphics/nucleotides/A2.png').convert_alpha()
    elif k_mer == 'T':
        KMER = pygame.image.load('graphics/nucleotides/T2.png').convert_alpha()
    elif k_mer == 'C':
        KMER = pygame.image.load('graphics/nucleotides/C2.png').convert_alpha()
    else:
        KMER = pygame.image.load('graphics/nucleotides/G.png').convert_alpha()
    screen.blit(KMER, ((SCREEN_WIDTH / 4) * 3 - 10, 40))
    return k_mer


pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pyquencing')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 45)
k_mer_font = pygame.font.Font('font/Pixeltype.ttf', 200)
game_active = False
start_time = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops=-1)

# Background
sky_surf = pygame.image.load('graphics/Sky2.png').convert()
sky_width = sky_surf.get_width()
sky_height = sky_surf.get_height()
ground_surf = pygame.image.load('graphics/ground.png').convert()
ground_width = ground_surf.get_width()

scroll = 0
tiles = ceil(SCREEN_WIDTH / ground_width) + 1

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()
# we don't want to add obstacles if the timer is not running so obstacle_group.add(Obstacle(...)) will be used after
# Sequence count
sequence = []
sequence_dictionary = {
    'Felis catus (Tamkatt)':
        '''CTGGAGAAGGAGGGCAGGGCCAGAAGCCAAGTCTGAAGGAAGGAACTTCCAGCCAATGAAAGGGGAACTG''',
    'Canis lupus familiaris (Hund - Labrador retriever)':
        '''AATATAAGGGAATGGAGAAGAATTGTGTAGGAAATATCAGAAAGGGAGACAGAACATAAAGACTCCTAAC''',
    'Elephas maximus (Asiatisk elefant)':
        '''ATGTGTTAAATGTGCCCTTTTCCTTCCACTCAAATACTGGTTAAAGCATGAATTCTAGGAAAGGAAGTTT''',
    'Escherichia coli (Kolibakterie)':
        '''GCATCGAATGGGCTCATCATTAATCGGTATCGGAATCAGGAGAATTTATAATGGCTTACAGCGAAAAAGT''',
    'SARS-CoV-2 (Coronavirus)':
        '''GAAGACATTCAACTTCTTAAGAGTGCTTATGAAAATTTTAATCAGCACGAAGTTCTACTTGCACCATTAT''',
    'Cantharellus cibarius (Kantarell)':
        '''AATGGCTTCTAGTCCGGCATGATCCACCCTATGAGCATCGGTGATCACAACAGAGTTGCTGGGGGCAGGT''',
    'Salmo salar (Atlantlax)':
        '''TATTTATTTTTATCCAAAAATCACAGCTGGAGTGCGATGGCGCCTTCCTGGGTGTCGGGTATGGTCGATG''',
    'Rosa chinensis (Kinarosor)':
        '''ATTAAGTTTCAAATGTCTTCTATGAACCTTATTACTTCATTGTTCAAGAAAATTGCGTTTGACTCCTGCT''',
    'Vaccinium myrtillus (Blåbär)':
        '''CTCTTTGAGTGTTGAGGACGATAGTGTCAATTTGGGCGCCAAGTATTGCGTTATTTATAGGGCTCCGTTC''',
    'Boletus edulis (Karljohanssvamp)':
        '''ATGTCATATATCAACTTTATATCTGTATTCTTGTAGCTGAAACTACCAAGCTAATGCTGTGGTGTGTTCA''',
    'Alces alces (Älgar)':
        '''TCCAGGTGAATGATGCTTTTGTCCTTGTCATCTACCACCACCATCGAAGAAGTGGTGGAAATGGGGTGGA''',


}
organisms = sequence_dictionary.keys()
sequence_organism = random.choice(list(sequence_dictionary.keys()))
random_length_of_sequence = randint(15, 30)
# random_length_of_sequence = randint(5, 7)  # Sam wants a short sequence for debugging
random_start = randint(0, 70 - random_length_of_sequence)
sequence_obj = str(sequence_dictionary[sequence_organism][random_start:random_start + random_length_of_sequence])

dictionary_nucleotides = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

k_mer_start = 0
# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

title_surf = test_font.render('Pyquencing Runner', False, (111, 196, 169))
title_rect = title_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5))

caption_surf = test_font.render('Are you ready? Good luck and press space to start', False, (111, 196, 169))
caption_rect = caption_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2))

# Timer
obstacle_timer = pygame.USEREVENT + 1  # we add +1 to avoid conflict with other pygame events
pygame.time.set_timer(obstacle_timer, 1600)
nucleotides = []

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            nucleotide = choice(['A', 'T', 'C', 'G', 'N'])
            if event.type == obstacle_timer:
                nucleotides.append(nucleotide)
                obstacle_group.add(Obstacle(nucleotides[-1]))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 500)
    # dislpay
    if game_active:
        # background
        for i in range(0, tiles):
            screen.blit(ground_surf, (i * ground_width + scroll, sky_height))
            screen.blit(sky_surf, (i * ground_width + scroll, 0))
        scroll -= 5
        if abs(scroll) > ground_width:
            scroll = 0

        # score
        score = display_score()

        # player
        player.draw(screen)
        player.update()

        # obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        # collisions
        k_mer_start = collision_sprite(k_mer_start)[1]
        game_active = collision_sprite(k_mer_start)[0]

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        result = 0
        result = round(collision_sprite(k_mer_start)[1])
        statement2 = ''
        statement3 = ''
        if result >= 99:
            statement = 'You are an amazing sequencer!'
            statement2 = f'You sequenced part of the genome'
            statement3 = f'{sequence_organism}'
        elif 99 > result >= 70:
            statement = 'You are a good and relatively reliable sequencer.'
            statement2 = f'You sequenced part of the genome'
            statement3 = f'{sequence_organism}'
        elif 60 <= result < 70:
            statement = 'I am sure that you can do better. Try again ;)'
        else:
            statement = 'Please try again, the sequencing did not go well,'
            statement2 = 'so we cannot say what organism you sequenced'

        score_message = test_font.render(f'Your sequencing result is {result} %', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2))
        score_message2 = test_font.render(f'{statement}', False, (111, 196, 169))
        score_message3 = test_font.render(f'{statement2}', False, (111, 196, 169))
        score_message4 = test_font.render(f'{statement3}', False, (111, 196, 169))
        score_message_rect2 = score_message.get_rect(center=(SCREEN_WIDTH / 3 + 150, SCREEN_HEIGHT / 1.2 + 30))
        score_message_rect3 = score_message.get_rect(center=(SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 1.2 + 60))
        score_message_rect4 = score_message.get_rect(center=(SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 1.2 + 90))
        screen.blit(title_surf, title_rect)

        if result == 0:
            screen.blit(caption_surf, caption_rect)
        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(score_message2, score_message_rect2)
            screen.blit(score_message3, score_message_rect3)
            screen.blit(score_message4, score_message_rect4)

    pygame.display.update()
    clock.tick(60)
