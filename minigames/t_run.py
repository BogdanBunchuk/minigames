import pygame
from core import *
from random import randint

def t_run_lauch():
    if True:
        window.fill((255, 255, 255))
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
        int_pc = 0
        dino_title_screen = True
        dino_game = False
        dino_jumped = False
        dino_jump = -4
        dino_fall = 0.6
        dino_frame_swap = 0
        floor_run = 20
        dino_dies = False
        while dino_title_screen:
            window.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    t_run_game = False
                    dino_title_screen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and dino_dies:
                        dino_dies = False
                        floor_run = 6
                        dino.rect.y = dino_on_ground
                        cactus1.rect.x = 1500
                        int_pc = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and dino_jumped:
                dino_jump += dino_fall
            if keys[pygame.K_SPACE] and dino_jumped == False:
                if dino.rect.y == dino_on_ground:
                    jump.play()
                dino_jump = -11+dino_fall
                dino.rect.y += dino_jump
                dino_jumped = True
            if dino_jumped:
                dino.new_file('t-run/dino idle.png')
                dino_frame_swap = 13
                dino_jump += dino_fall
                dino.rect.y += dino_jump
                if dino.rect.y >= dino_on_ground:
                    dino_jumped = False
                    dino_game = True
                    dino_jump = -5+0.15
                    dino.rect.y = dino_on_ground
                    dino_frame_swap = 4
            if dino_game:
                if not dino_dies:
                    int_pc += 0.3
                    points_counter.set_text('Points: '+ str(round(int_pc)))
                    points_counter.set_text_settings('Arial', 10)
                if dino_floor1.rect.x <= -75:
                    floor_run = 6
                if dino.colliderect(cactus1):
                    if not dino_dies:
                        die.play()
                    ts_text.new_file('t-run/you died.png')
                    ts_text.rect.x = 300
                    ts_text.rect.y = 200
                    dino.new_file('t-run\dino dies.png')
                    dino_frame_swap = 300
                    floor_run = 0
                    dino_jump = 0
                    dino_dies = True
                cactus1.rect.x -= floor_run
                for floor in dino_floors:
                    floor.rect.x -= floor_run
                floor_run += 0.001
                for dino_floor in dino_floors:
                    dino_floor.draw()
                dino_frame_swap += 1
                if dino_frame_swap == 6:
                    dino.new_file('t-run\dino run1.png')
                elif dino_frame_swap == 12:
                    dino.new_file('t-run\dino run2.png')
                    dino_frame_swap = 0
                cactus1.draw()
                points_counter.draw_text()
            if dino_floor1.rect.x <= -200 and dino_frame_swap < 199:
                dino_floor1.rect.x = dino_floor3.rect.x + 299
            if dino_floor2.rect.x <= -200 and dino_frame_swap < 199:
                dino_floor2.rect.x = dino_floor1.rect.x + 299
            if dino_floor3.rect.x <= -200 and dino_frame_swap < 199:
                dino_floor3.rect.x = dino_floor2.rect.x + 299
            if cactus1.rect.x <= 0:
                cactus1.rect.x = randint(600, 800)
                cactus1.new_file(cactus_pics[randint(0, 2)])
            
                
            
            dino.draw()
            if not dino_game or dino_dies:
                ts_text.draw()
            dino_cover.draw()
            pygame.display.update()
            clock.tick(60)