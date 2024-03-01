import pygame
from core import *
from random import randint, shuffle

def gate_lauch():
    if True:
        window.fill((0, 0, 40))
        player = Label(385, 500, 30, 30, (191,191,10))
        player.set_text('0')
        player.set_text_settings('Arial', 15)
        player_text = 0
        bridge = Label(250, 0, 200, 600, (0,0,73))
        play_button = Picture('gateway\play.png', 320, 400, 60, 60)
        gates = []
        stars = []
        star_move = []
        for i in range(300):
            star = Label(randint(0, 700), randint(0, 600), randint(1, 2), randint(1, 2), (255, 255, 255))
            star_move.append(randint(1,3))
            stars.append(star)
        good_gate_color = (0, 63, 147)
        bad_gate_color = (127, 31, 20)
        coordinates_x = [260, 360, 260, 360]
        coordinates_y = [0, 0, 350, 350]
        good_numbers = ['+2', '+20', 'X2', 'X10', 'X20', '+2', 'X2', '+2', '+20', 'X2', 'X10', 'X10', '+10', 'X20', '+10', '+10', '+2', '+2', '+2', '+2']
        shuffle(good_numbers)
        bad_numbers = ['-2', '-20', '÷2', '÷10', '÷20', '-2', '÷2', '-2', '-20', '÷2', '÷10', '÷10', '÷10', '÷20', '÷10', '÷10', '-2', '-2', '-2', '-2']
        shuffle(bad_numbers)
        numbers = [good_numbers, bad_numbers]
        for i in range(4):
            gate = Label(coordinates_x[i], coordinates_y[i], 80, 35, good_gate_color)
            set_numbers = 0
            gate.set_text(numbers[0][randint(0, 9)])
            gate.set_text_settings('Arial', 15, (0,0,0))
            if set_numbers == 0:
                gate.color(good_gate_color)
            else:
                gate.color(bad_gate_color)
            gates.append(gate)
        play_scene = True
        title_screen = True
        count = True
        while title_screen:
            window.fill((0, 0, 40))
            for event in pygame.event.get():
                if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if play_button.collidepoint(x, y):
                        title_screen = False
                if event.type == pygame.QUIT:
                    gateway_game = False
                    play_scene = False
                    title_screen = False
            bridge.fill()
            for gate in gates:
                gate.fill()
            for star in stars:
                if star.colliderect(bridge):
                    star.color((128, 128, 208))
                star.fill()
            player.fill()
            player.draw_text(0, 5)
            play_button.draw()
            pygame.display.update()
            clock.tick(60)
        while play_scene:
            window.fill((0, 0, 40))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gateway_game = False
                    play_scene = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and player.rect.x == 285:
                        player.rect.x = 385
                    elif event.key == pygame.K_LEFT and player.rect.x == 385:
                        player.rect.x = 285
            bridge.fill()
            for gate in gates:
                if gate.rect.y > 600+gate.rect.height:
                    gate.rect.y = 0-gate.rect.height
                    set_numbers = randint(0,1)
                    gate.set_text(numbers[set_numbers][randint(0, 19)])
                    gate.set_text_settings('Arial', 15, (0,0,0))
                    count = True
                    if set_numbers == 0:
                        gate.color(good_gate_color)
                    else:
                        gate.color(bad_gate_color)

                if player.colliderect(gate) and count:
                    count = False
                    if gate.text == '+2':
                        player_text += 2
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '+10':
                        player_text += 10
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '+20':
                        player_text += 2
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == 'X2':
                        player_text *= 2
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == 'X10':
                        player_text *= 10
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == 'X20':
                        player_text *= 20
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '-2':
                        player_text -= 2
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '-20':
                        player_text -= 20
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '-10':
                        player_text -= 10
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '÷2':
                        player_text = round(player_text/2)
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '÷10':
                        player_text = round(player_text/10)
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                    elif gate.text == '÷20':
                        player_text = round(player_text/20)
                        player.set_text(str(player_text))
                        player.set_text_settings('Arial', 15)
                gate.rect.y -= -2
                gate.fill()
                gate.draw_text(30, 10)
            star_counter = 0
            for star in stars:
                if star.colliderect(bridge):
                    star.color((128, 128, 208))
                star.rect.y += star_move[star_counter]
                star.fill()
                if star.rect.y > 605:
                    star.rect.y = -5
                    star.rect.x = randint(0, 700)
                    star.rect.height, star.rect.width = randint(1, 2), randint(1, 2)
                    star_move[star_counter] = randint(1, 3)
                star_counter+=1
            player.fill()
            player.draw_text(0, 5)
            pygame.display.update()
            clock.tick(60)