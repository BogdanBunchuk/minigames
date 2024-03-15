from core import *
import pygame
from random import randint
bg_color = (200, 255, 255)
screen_block = Picture('flappy bird\screen_cover.png', 0, 0, 0, 0)
pipe_file = 'flappy bird\le_pipe.png'
bird_file = 'flappy bird\le_birb.png'
floor_file = 'flappy bird\le_floor.png'
decoy_file = 'flappy bird\decoy.png'
pop = pygame.mixer.Sound('flappy bird\Everything\sfx_point.wav')
space_sound = pygame.mixer.Sound('flappy bird\Everything\sfx_wing.wav')
play_sound = pygame.mixer.Sound('flappy bird\Everything\sfx_swooshing.wav')
die_sound = pygame.mixer.Sound('flappy bird\Everything\sfx_die.wav')
hit_sound = pygame.mixer.Sound('flappy bird\Everything\sfx_hit.wav')

pipe_spawn = randint(100, 275)
bird = Picture(bird_file, 150, 220, 34, 24)
floor = Picture(floor_file, 0, 406, 0, 22)
le_pipe = Picture(pipe_file, 50, 300, 50, 400)
le_le_pipe = Picture(pipe_file, 900, pipe_spawn, 50, 400)
pipe_le = Picture(pipe_file, 50, -300, 50, 400)
pipe_le_le = Picture(pipe_file, 900, pipe_spawn-500, 50, 400)
decoy = Picture(decoy_file, 100, 303, 50, 300)
title = Picture('flappy bird\le_title.png', 200, 50, 50, 300)
button = Picture('flappy bird\le_button.png', 300, 225, 74, 46)
cloud1 = Picture('flappy bird\le_clond.png', 400, 136, 52, 22)
cloud2 = Picture('flappy bird\le_clond.png', 138, 200, 52, 22)
hill = Picture('flappy bird\grassy_hill.png', 308, 303, 52, 22)
out_play_button = Picture('flappy bird\play_button.png', 460, 480, 70, 70)
out_jump_button = Picture('flappy bird\jump_button.png', 350, 480, 70, 70)
audio_button = Picture('flappy bird\sound_on.png', 25, 20, 40, 40)
game_over = Picture('flappy bird\you_died_lol.png', 250, 1150, 0, 0)
pipes1 = [le_pipe, pipe_le]
pipes2 = [le_le_pipe, pipe_le_le]
pipes_set = [le_pipe, pipe_le, le_le_pipe, pipe_le_le]

point_text = Label(325, 0, 0, 0)
point_text.set_text('0')
point_text.set_text_settings('Arial', 60)