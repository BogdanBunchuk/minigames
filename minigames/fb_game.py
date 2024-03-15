import pygame
from core import *
from random import randint
from fb_creation import *

def flappy_launch():
    if True:
        pipe_spawn = randint(100, 275)
        game = True
        title_screen = True
        sound_on = True

        while title_screen:
            window.fill(bg_color)
            for event in pygame.event.get():
                if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if button.collidepoint(x,y) or out_play_button.collidepoint(x,y):
                        title_screen = False
                        game_continues = True
                        restart = True
                        if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                            play_sound.play()
                    elif audio_button.collidepoint(x,y):
                        if sound_on:
                            audio_button.new_file('flappy bird\sound_off.png')
                            sound_on = False
                        else:
                            audio_button.new_file('flappy bird\sound_on.png')
                            sound_on = True
                if event.type == pygame.QUIT:
                    title_screen = False
                    game_continues = False
                    restart = False
            cloud1.reset_x(500)
            hill.reset_x(408)
            cloud2.reset_x(238)
            title.reset_pos(200, 50)

            title.draw()
            cloud1.draw()
            cloud2.draw()

            decoy.draw()
            bird.draw()
            button.draw()
            screen_block.draw()
            out_play_button.draw()
            out_jump_button.draw()
            audio_button.draw()
            pygame.display.update()
            clock.tick(60)

        button.rect.y = 700
        point_counter = 0
        title_fall = 0.1
        while game_continues:
            for event in pygame.event.get():
                if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if button.collidepoint(x,y) or out_play_button.collidepoint(x,y) and game == False:
                        restart = True
                        if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                            play_sound.play()
                    if out_jump_button.collidepoint(x,y):
                        fall_speed = -5
                        if sound_on and game and audio_button.image == 'flappy bird\sound_on.png':
                            space_sound.play()
                    if audio_button.collidepoint(x,y):
                        if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                            audio_button.new_file('flappy bird\sound_off.png')
                            sound_on = False
                        else:
                            audio_button.new_file('flappy bird\sound_on.png')
                            sound_on = True
                if event.type == pygame.QUIT:
                    game_continues = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        fall_speed = -5
                        if sound_on and game and audio_button.image == 'flappy bird\sound_on.png':
                            space_sound.play()
            window.fill(bg_color)
            if restart:
                fall_speed = 0.1
                point_counter = 0
                point_text.set_text(str(point_counter))
                point_text.set_text_settings('Arial', 60)
                bird.reset_pos(150, 220)

                for i in range(2):
                    pipes1[i].reset_x(0)
                    pipes2[i+2].reset_x(925)

                pipe_spawn = randint(100, 275)    
                pipes1[0].reset_y(pipe_spawn)
                pipes1[1].reset_y(pipe_spawn - 500)

                pipe_spawn = randint(100, 275)        
                pipes2[0].reset_y(pipe_spawn)
                pipes2[1].reset_y(pipe_spawn - 500)

                game_over.reset_y(1000)
                button.reset_y(600)

                restart = False
                game = True
                not_counted = False
            if game:
                fall_speed += 0.275
                bird.rect.y += fall_speed
                pipes1[0].move_x(-3)
                pipes1[1].move_x(-3)
                pipes2[0].move_x(-3)
                pipes2[1].move_x(-3)
                title_fall += 0.5
                title.rect.y -= title_fall
                cloud1.move_x(-1.2)
                cloud2.move_x(-1.4)

                if bird.colliderect(pipes1[0].rect) or bird.colliderect(pipes1[1].rect) or bird.colliderect(pipes2[0].rect) or bird.colliderect(pipes2[1].rect):
                    game = False
                    if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                        hit_sound.play()

                hill.rect.x -= 1.8
                if cloud1.rect.x < -52:
                    cloud1.reset_pos(randint(602, 800), randint(100, 350))
                if cloud2.rect.x < -52:
                    cloud2.reset_pos(randint(602, 800), randint(100, 350))
                if hill.rect.x < -107:
                    hill.reset_x(randint(707, 1100))

                if pipes1[0].rect.x < 100 and not_counted:
                    point_counter += 1
                    point_text.set_text(str(point_counter))
                    point_text.set_text_settings('Arial', 60)
                    not_counted = False
                    if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                        pop.play()
                    
                if pipes2[0].rect.x < 100 and not_counted:
                    point_counter += 1
                    point_text.set_text(str(point_counter))
                    point_text.set_text_settings('Arial', 60)
                    not_counted = False
                    if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                        pop.play()

                if pipes1[0].rect.x < 50:
                    le_pipe_thing = randint(100, 350)
                    pipes1[0].reset_pos(650, le_pipe_thing)
                    pipes1[1].reset_pos(650, le_pipe_thing - 500)
                    not_counted = True

                if pipes2[0].rect.x < 50:
                    le_pipe_thing = randint(100, 350)
                    pipes2[0].reset_pos(650, le_pipe_thing)
                    pipes2[1].reset_pos(650, le_pipe_thing - 500)
                    not_counted = True
                if bird.rect.y > 390:
                    game = False
                    if sound_on and audio_button.image == 'flappy bird\sound_on.png':
                        die_sound.play()
                elif bird.rect.y < 0:
                    bird.rect.y -= fall_speed

            else:
                button.rect.y = 225
                game_over.rect.y = 50
                
            title.draw()
            cloud1.draw()
            cloud2.draw()
            hill.draw()
            pipes2[0].draw()
            pipes2[1].draw()
            pipes1[1].draw()
            pipes1[0].draw()
            floor.draw()
            bird.draw()
            point_text.draw_text()
            game_over.draw()
            button.draw()
            screen_block.draw()
            out_play_button.draw()
            out_jump_button.draw()
            audio_button.draw()

            pygame.display.update()
            clock.tick(60)