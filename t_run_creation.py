from core import *
import pygame
from random import randint
dino_on_ground = 261
cactus_pics = ['t-run\cacti 1.png', 't-run\cacti 2.png', 't-run\cacti 3.png']
dino_cover = Picture('t-run\dino cover.png')
dino_floor1 = Picture('t-run\dino floor.png', 600, 300, 70, 70)
dino_floor2 = Picture('t-run\dino floor.png', 900, 300, 70, 70)
dino_floor3 = Picture('t-run\dino floor.png', 1200, 300, 70, 70)
dino_floors = [dino_floor1, dino_floor2, dino_floor3]
dino = Picture('t-run\dino idle.png', 200, dino_on_ground, 40, 40)
ts_text = Picture('t-run\main screen text.png', 100, 100, 80, 80)
cactus1 = Picture(cactus_pics[randint(0, 2)], 1500, dino_on_ground-4, 15, 50)
points_counter = Label(100, 100, 75, 75, (0,0,0))
points_counter.set_text('Очки:')
points_counter.set_text_settings(font_name='Futura', font_size=10, text_color=(0,0,0))
jump = pygame.mixer.Sound('t-run\jump.wav')
die = pygame.mixer.Sound('t-run\die.wav')
