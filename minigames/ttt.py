import pygame
from core import *

def ttt_launch():
    if True:
        window.fill((63, 63, 63))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ttt_launch = False

        cells = []
        backcells = []
        num = [100, 220, 340]
        num2 = 100
        backpanel = Label(85, 85, 370, 370, (31, 31, 31))
        reset_btn = Label(500, num[2], 100, 100, (0, 175, 0))
        rbtn_back = Label(495, 335, 110, 110, (0, 127, 0))
        reset_btn.set_text('Reset')
        reset_btn.set_text_settings('Arial', 35)
        for i in range(3):
            for a in range(3):
                backcell = Label((num[a-1]-5), num2-5, 110, 110, (95, 95, 95))
                backcells.append(backcell)
            num2 += 120
        num2 = 100
        for i in range(3):
            for a in range(3):
                cell = Label(num[a-1], num2, 100, 100, (127, 127, 127))
                cell.set_text('')
                cell.set_text_settings('Arial', 50)
                cells.append(cell)
            num2 += 120
        ttt_game = True
        blue_turn = 0
        blue_color = (63, 63, 95)
        red_color = (95, 63, 63)
        neutral_color = (63, 63, 63)
        while ttt_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ttt_game = False
                if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    for cell in cells:
                        if cell.collidepoint(x, y):
                            if blue_turn == 0:
                                cell.color((127, 127, 191))
                                blue_turn = 1
                                cell.set_text('X')
                            elif blue_turn == 1:
                                cell.color((191, 127, 127))
                                blue_turn = 0
                                cell.set_text('O')
                            cell.set_text_settings('Arial', 60)
                        if reset_btn.collidepoint(x,y):
                            for cell in cells:
                                cell.color((127, 127, 127))
                                cell.set_text('')
                                blue_turn = 0
                                cell.set_text_settings('Arial', 60)
                            window.fill(neutral_color)
            if cells[0].text == 'X' and cells[1].text == 'X' and cells[2].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[0].text == 'X' and cells[4].text == 'X' and cells[8].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[3].text == 'X' and cells[4].text == 'X' and cells[5].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[6].text == 'X' and cells[7].text == 'X' and cells[8].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[0].text == 'X' and cells[3].text == 'X' and cells[6].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[1].text == 'X' and cells[4].text == 'X' and cells[7].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[2].text == 'X' and cells[5].text == 'X' and cells[8].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[6].text == 'X' and cells[4].text == 'X' and cells[2].text == 'X':
                blue_turn = 3
                window.fill(blue_color)
            if cells[0].text == 'O' and cells[1].text == 'O' and cells[2].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[0].text == 'O' and cells[4].text == 'O' and cells[8].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[3].text == 'O' and cells[4].text == 'O' and cells[5].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[6].text == 'O' and cells[7].text == 'O' and cells[8].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[0].text == 'O' and cells[3].text == 'O' and cells[6].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[1].text == 'O' and cells[4].text == 'O' and cells[7].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[2].text == 'O' and cells[5].text == 'O' and cells[8].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            if cells[6].text == 'O' and cells[4].text == 'O' and cells[2].text == 'O':
                blue_turn = 3
                window.fill(red_color)
            backpanel.fill()
            for backcell in backcells:
                backcell.fill()
            for cell in cells:
                cell.fill()
                cell.draw_text(32, 13)
            rbtn_back.fill()
            reset_btn.fill()
            reset_btn.draw_text(10, 20)
            pygame.display.update()
            clock.tick(60)