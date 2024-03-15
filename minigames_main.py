import pygame
from core import *
from fb_game import *
from ttt import *
from gate import *
from t_run import *

main_title_screen = Area(0, 0, 1000, 1000, (255, 189, 137))
select_screen = True
starter = 100
icon_gap = 70

dino_title_screen = False
while select_screen:
    window.fill((255, 189, 137))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            select_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if flappy_bird_icon.collidepoint(x,y):
                flappy_launch()
            if t_run_icon.collidepoint(x,y):
                t_run_lauch()
            if gateway_icon.collidepoint(x,y):
                gate_lauch()
            if ttt_icon.collidepoint(x,y):
                ttt_launch()
    flappy_bird_icon = Picture('FB icon.png', starter, icon_gap, 70, 70)
    t_run_icon = Picture('T icon.png', starter+icon_gap*2, icon_gap, 70, 70)
    gateway_icon = Picture('gate icon.png', starter+icon_gap*4, icon_gap, 70, 70)
    ttt_icon = Picture('ttt icon.png', starter+icon_gap*6, icon_gap, 70, 70) 
    flappy_bird_icon.draw()
    t_run_icon.draw()
    gateway_icon.draw()
    ttt_icon.draw()
    pygame.display.update()