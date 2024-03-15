import pygame
from core import *
from random import randint, shuffle

if True:
    if True:
        window.fill((0, 0, 40))
        player = Label(385, 500, 30, 30, (191,191,10))
        player.set_text('0')
        player.set_text_settings('Arial', 15)
        bridge = Label(250, 0, 200, 600, (0,0,73))
        play_button = Picture('gateway\play.png', 320, 400, 60, 60)
        gates = []
        stars = []
        star_move = []
        for i in range(500):
            star = Label(randint(0, 700), randint(0, 600), randint(1, 2), randint(1, 2), (255, 255, 255))
            star_move.append(randint(1,4))
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