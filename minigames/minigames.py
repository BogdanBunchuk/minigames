import pygame
from random import randint, shuffle, random

pygame.init()
bg_color = (200, 255, 255)
window = pygame.display.set_mode((700, 600))
window.fill(bg_color)
clock = pygame.time.Clock()
font_size = 30
font = pygame.font.SysFont("Futura",font_size)

class Area():
    def __init__(self, x, y, width=75, height=75, color=None):
        self.rect = pygame.Rect(x, y, width, height) 
        self.fill_color = color
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def new_file(self, filename):
        self.image = pygame.image.load(filename)

class Label(Area):
    def set_text(self, text):
        self.text = text
    def set_text_settings(self, font_name, font_size, text_color=(0,0,0)):
        font = pygame.font.SysFont(font_name, font_size)
        self.text_render = font.render(self.text, True, text_color)

    def draw_text(self, shift_x=0, shift_y=0):
        x = self.rect.x + shift_x
        y = self.rect.y + shift_y
        window.blit(self.text_render,(x,y))
flappy_bird_game = False
t_run_game = False
gateway_game = False
ttt_launch = False
main_title_screen = Area(0, 0, 1000, 1000, (255, 189, 137))
select_screen = True
starter = 100
icon_gap = 70
sound_on = True
dino_title_screen = False
while select_screen:
    window.fill((255, 189, 137))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            select_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if flappy_bird_icon.collidepoint(x,y):
                flappy_bird_game = True
            if t_run_icon.collidepoint(x,y):
                t_run_game = True
            if gateway_icon.collidepoint(x,y):
                gateway_game = True
            if ttt_icon.collidepoint(x,y):
                ttt_launch = True
    flappy_bird_icon = Picture('FB icon.png', starter, icon_gap, 70, 70)
    t_run_icon = Picture('T icon.png', starter+icon_gap*2, icon_gap, 70, 70)
    gateway_icon = Picture('gate icon.png', starter+icon_gap*4, icon_gap, 70, 70)
    ttt_icon = Picture('ttt icon.png', starter+icon_gap*6, icon_gap, 70, 70) 
    flappy_bird_icon.draw()
    t_run_icon.draw()
    gateway_icon.draw()
    ttt_icon.draw()
    while flappy_bird_game:
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
    while t_run_game:
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
    while gateway_game:
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
    while ttt_launch:
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
                    ttt_launch = False
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
    pygame.display.update()
