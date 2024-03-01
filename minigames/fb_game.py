import pygame
from core import *
from random import randint

bg_color = (200, 255, 255)
sound_on = True
def flappy_launch():
    if True:
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
        if sound_on:
            audio_button = Picture('flappy bird\sound_on.png', 25, 20, 40, 40)
        else:
            audio_button = Picture('flappy bird\sound_off.png', 25, 20, 40, 40)

        game_over = Picture('flappy bird\you_died_lol.png', 250, 1150, 0, 0)

        point_text = Label(325, 0, 0, 0)
        point_text.set_text('0')
        point_text.set_text_settings('Arial', 60)

        game = True
        title_screen = True

        while title_screen:
            window.fill(bg_color)
            for event in pygame.event.get():
                if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if button.collidepoint(x,y) or out_play_button.collidepoint(x,y):
                        title_screen = False
                        game_continues = True
                        restart = True
                        if sound_on:
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
                    flappy_bird_game = False
            cloud1.rect.x = 500
            hill.rect.x = 408
            cloud2.rect.x = 238

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
        not_counted = False
        while game_continues:
            for event in pygame.event.get():
                if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if button.collidepoint(x,y) or out_play_button.collidepoint(x,y) and game == False:
                        restart = True
                        if sound_on:
                            play_sound.play()
                    if out_jump_button.collidepoint(x,y):
                        fall_speed = -5
                        if sound_on and game:
                            space_sound.play()
                    if audio_button.collidepoint(x,y):
                        if sound_on:
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
                        if sound_on and game:
                            space_sound.play()
            window.fill(bg_color)
            if restart:
                fall_speed = 0.1
                point_counter = 0
                point_text.set_text(str(point_counter))
                point_text.set_text_settings('Arial', 60)
                bird.rect.x = 150
                bird.rect.y = 220

                le_pipe.rect.x = 0
                pipe_le_le.rect.x = 925
                le_le_pipe.rect.x = 925
                pipe_le.rect.x = 0

                pipe_spawn = randint(100, 275)        
                le_pipe.rect.y = pipe_spawn
                pipe_le.rect.y = pipe_spawn - 500

                pipe_spawn = randint(100, 275)        
                le_le_pipe.rect.y = pipe_spawn
                pipe_le_le.rect.y = pipe_spawn - 500

                game_over.rect.y = 1000
                button.rect.y = 600

                restart = False
                game = True
                not_counted = False
            if game:
                fall_speed += 0.275
                bird.rect.y += fall_speed
                le_pipe.rect.x -= 3
                pipe_le.rect.x -= 3
                le_le_pipe.rect.x -= 3
                pipe_le_le.rect.x -= 3
                title_fall += 0.5
                title.rect.y -= title_fall
                cloud1.rect.x -= 1.2
                cloud2.rect.x -= 1.4

                if bird.colliderect(le_pipe.rect) or bird.colliderect(pipe_le.rect) or bird.colliderect(le_le_pipe.rect) or bird.colliderect(pipe_le_le.rect):
                    game = False
                    if sound_on:
                        hit_sound.play()

                hill.rect.x -= 1.8
                if cloud1.rect.x < -52:
                    cloud1.rect.y = randint(100, 350)
                    cloud1.rect.x = randint(602, 800)
                if cloud2.rect.x < -52:
                    cloud2.rect.y = randint(100, 350)
                    cloud2.rect.x =randint(602, 800)
                if hill.rect.x < -107:
                    hill.rect.x = randint(707, 1100)

                if le_pipe.rect.x < 100 and not_counted:
                    point_counter += 1
                    point_text.set_text(str(point_counter))
                    point_text.set_text_settings('Arial', 60)
                    not_counted = False
                    if sound_on:
                        pop.play()
                    
                if le_le_pipe.rect.x < 100 and not_counted:
                    point_counter += 1
                    point_text.set_text(str(point_counter))
                    point_text.set_text_settings('Arial', 60)
                    not_counted = False
                    if sound_on:
                        pop.play()

                if le_pipe.rect.x < 50:
                    le_pipe.rect.x = 650
                    pipe_le.rect.x = 650
                    le_pipe_thing = randint(100, 350)
                    le_pipe.rect.y = le_pipe_thing
                    pipe_le.rect.y = le_pipe_thing - 500
                    not_counted = True

                if le_le_pipe.rect.x < 50:
                    le_le_pipe.rect.x = 650
                    pipe_le_le.rect.x = 650
                    le_pipe_thing = randint(100, 350)
                    le_le_pipe.rect.y = le_pipe_thing
                    pipe_le_le.rect.y = le_pipe_thing - 500
                    not_counted = True
                if bird.rect.y > 390:
                    game = False
                    if sound_on:
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
            le_le_pipe.draw()
            pipe_le_le.draw()
            pipe_le.draw()
            le_pipe.draw()
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