import os
import pygame
import random
import sys

from constants import *
from intro import *
from rules import *

pygame.init()


def draw_end(victory):
    global flag_board_garbage, garbage_coords, name, walle_sprites, screen
    global heart_sprites, garbage_sprites, gl_x, gl_y, flag_move, block_coords
    global count_garbage, block_garbage, running0, count_blocks, loops, size
    global width, height, walle, board, garbage, name_sound_image, cube_coords
    global loops, running, count_restart
    count_restart += 1
    if not victory:
        fon_the_end = pygame.image.load('data\end_start.jpg')
        fon_the_end_bold = pygame.image.load('data\end_start_bold.jpg')
        x_0 = 352
        x_1 = 635
        y_0 = 241
        y_1 = 402
    else:
        fon_the_end = pygame.image.load('data\end_start_victory.jpg')
        fon_the_end_bold = pygame.image.load('data\end_start_victory_bold.jpg')
        x_0 = 610
        x_1 = 850
        y_0 = 590
        y_1 = 730
    screen.blit(fon_the_end, (0, 0))
    waiting = True
    while waiting:
        screen.blit(fon_the_end, (0, 0))
        if x_0 < pygame.mouse.get_pos()[0] < x_1:
            if y_0 < pygame.mouse.get_pos()[1] < y_1:
                screen.blit(fon_the_end_bold, (0, 0))
        pygame.time.Clock().tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                waiting = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x_0 < pygame.mouse.get_pos()[0] < x_1:
                        if y_0 < pygame.mouse.get_pos()[1] < y_1:
                            flag_board_garbage = 0
                            garbage_coords = []
                            name = []
                            walle_sprites = pygame.sprite.Group()
                            heart_sprites = pygame.sprite.Group()
                            gl_x = 912
                            gl_y = 372
                            flag_move = 0
                            block_coords = []
                            count_garbage = set()
                            block_garbage = []
                            running0 = 1
                            name_sound_image = 'sound_on.jpg'
                            count_blocks = 0
                            loops = -1
                            size = width, height = 1160, 800
                            screen = pygame.display.set_mode(size)
                            walle = Walle(walle_sprites)
                            board = Board(19, 13)
                            garbage = Garbage()
                            running = True
                            cube_coords = []
                            main()
        pygame.display.flip()
    pygame.quit()


class Board:
    def __init__(self, width, height):
        global w, h
        w = width
        h = height
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 60
        self.render(screen)
        self.draw_lines()
        self.draw_grey_garbage()
        self.draw_arrow()

    def draw_sound(self):
        global name_sound_image
        self.sound_on = pygame.image.load(os.path.join('data',
                                                       name_sound_image))
        screen.blit(self.sound_on, ((w - 2) * 60 + 11, 131))

    def draw_arrow(self):
        self.arrow = pygame.image.load(os.path.join('data', 'заново.png'))
        screen.blit(self.arrow, ((w - 1) * 60 + 11, 131))

    def draw_grey_garbage(self):
        self.garbage321_image = pygame.image.load(os.path.join(
                                                  'data', 'grbg_321.jpg'))
        self.garbage_image = pygame.transform.scale(self.garbage321_image,
                                                    (56, 56))
        self.garbage1 = self.garbage_image
        self.garbage2 = self.garbage_image
        self.garbage3 = self.garbage_image
        screen.blit(self.garbage1, ((w - 3) * 60 + 12, 72))
        screen.blit(self.garbage2, ((w - 2) * 60 + 12, 72))
        screen.blit(self.garbage3, ((w - 1) * 60 + 12, 72))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(surface, 'white',
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size), DEPTH)
                else:
                    pygame.draw.rect(surface, 'white',
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size))

    def draw_lines(self):
        pygame.draw.line(screen, pygame.Color('black'),
                         (self.left, self.top + self.cell_size),
                         (self.left + self.cell_size, self.top), 2)
        for i in range(self.height - 1):
            pygame.draw.line(screen, 'black',
                             (self.left, self.top + (i + 2) * self.cell_size),
                             (self.cell_size * 2 + self.left,
                              self.top + i * self.cell_size), 2)
        pygame.draw.line(screen, 'black',
                         (self.left + self.cell_size,
                          self.top + self.cell_size * self.height),
                         (self.cell_size * 2 + self.left,
                          self.top + self.cell_size * (self.height - 1)), 2)
        pygame.draw.line(screen, (77, 77, 77), (self.left, self.top),
                         (2 * self.cell_size + self.left, self.top), 3)
        pygame.draw.line(screen, (77, 77, 77),
                         (self.left, self.top + self.height * self.cell_size),
                         (self.left + 2 * self.cell_size,
                          self.top + self.height * self.cell_size), 3)
        pygame.draw.line(screen, (77, 77, 77), (self.left, self.top),
                         (self.left, self.top + self.height * self.cell_size),
                         3)
        pygame.draw.line(screen, (77, 77, 77),
                         (self.left + 2 * self.cell_size, self.top),
                         (self.left + 2 * self.cell_size,
                          self.top + self.height * self.cell_size), 3)
        pygame.draw.line(screen, 'black',
                         ((self.width - 4) * self.cell_size + self.left,
                          self.top + 1),
                         ((self.width - 4) * self.cell_size + self.left,
                          20), 5)
        for i in range(1, self.height):
            pygame.draw.line(screen, 'black',
                             (self.cell_size * (self.width - 4) + self.left,
                              i * self.cell_size - 10),
                             ((self.width - 4) * self.cell_size + self.left,
                              20 + i * self.cell_size), 5)
        pygame.draw.line(screen, 'black',
                         ((self.width - 4) * self.cell_size + self.left,
                          self.height * self.cell_size - 10),
                         ((self.width - 4) * self.cell_size + self.left,
                          self.cell_size * self.height + 8), 5)


class Garbage():
    def __init__(self):
        global flag_board_garbage, garbage_coords, name, garbage_sprites
        for i in range(60):
            if i == 0:
                garbage_coords = random.sample(COORDS, 60)
            name.append(GARBAGE[random.randint(0, len(GARBAGE) - 1)])
        for i in range(60):
            image = pygame.image.load(os.path.join('data',
                                                   name[i] + '.png'))
            self.image = pygame.transform.scale(image, (58, 58))
            screen.blit(self.image, (garbage_coords[i][0],
                                     garbage_coords[i][1]))
        pygame.image.save(screen, 'data\screen.png')

    def update(self):
        global block_coords, flag_grey, count_garbage, block_garbage
        for i in block_coords:
            if gl_x == i[0] and gl_y == i[1]:
                name_image = 'block_with_walle'
                if (gl_x, gl_y) not in block_garbage:
                    count_garbage.add((gl_x, gl_y))
            else:
                name_image = 'block'
            self.image = pygame.image.load(os.path.join('data',
                                                        name_image + '.jpg'))
            self.image = pygame.transform.scale(self.image, (57, 57))
            screen.blit(self.image, (i[0], i[1]))

    def draw_count_garbage(self):
        global board, flag_grey
        self.gb3211_image = pygame.image.load(os.path.join('data',
                                                           'garbage_3211.jpg'))
        self.gb_image = pygame.transform.scale(self.gb3211_image,
                                               (56, 56))
        self.gb1 = self.gb_image
        self.garbage321_image = pygame.image.load(os.path.join('data',
                                                               'grbg_321.jpg'))
        self.garbage_image = pygame.transform.scale(self.garbage321_image,
                                                    (56, 56))
        self.garbage1 = self.garbage_image
        if len(count_garbage) == 1:
            screen.blit(self.garbage1, ((w - 1) * 60 + 12, 72))
            screen.blit(self.garbage1, ((w - 2) * 60 + 12, 72))
            screen.blit(self.gb1, ((w - 3) * 60 + 12, 72))
        elif len(count_garbage) == 2:
            screen.blit(self.garbage1, ((w - 1) * 60 + 12, 72))
            screen.blit(self.gb1, ((w - 3) * 60 + 12, 72))
            screen.blit(self.gb1, ((w - 2) * 60 + 12, 72))
        elif len(count_garbage) == 3:
            screen.blit(self.gb1, ((w - 3) * 60 + 12, 72))
            screen.blit(self.gb1, ((w - 2) * 60 + 12, 72))
            screen.blit(self.gb1, ((w - 1) * 60 + 12, 72))


class Cube_garbage:
    def __init__(self):
        self.make_cube()

    def make_cube(self):
        global gl_x, gl_y, count_garbage, flag_walle, block_garbage
        global count_blocks, cube_coords
        self.cube_garbage_image = pygame.image.load(os.path.join('data',
                                                    'cube_garbage.jpg'))
        self.cube_image = pygame.transform.scale(self.cube_garbage_image,
                                                 (56, 56))
        if 10 <= gl_x <= 130 and len(count_garbage) == 3 and \
           (gl_x, gl_y) not in cube_coords:
            screen.blit(self.cube_image, (gl_x, gl_y))
            pygame.image.save(screen, 'data\screen.png')
            for i in count_garbage:
                block_garbage.append(i)
            count_garbage = set()
            flag_walle = 1
            count_blocks += 1
            cube_coords.append((gl_x, gl_y))


class Walle(pygame.sprite.Sprite):
    image = pygame.image.load('data\wall-e.vtjkl (2).png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Walle.image
        self.rect = self.image.get_rect()
        self.left = 10
        self.top = 10
        self.cell_size = 60
        self.rect.x = (1160 - 4) * self.cell_size + self.left + 3
        self.rect.y = self.top + 4 + 800 // 2 * self.cell_size

    def draw_walle(self, x=0, y=0, flag_walle=0):
        global gl_x, gl_y, block_coords, count_garbage, garbage_coords
        self.rect.x = gl_x
        self.rect.y = gl_y
        count = 0
        condition1 = (gl_x + x * 60 > 910 and len(count_garbage) != 0)
        condition2 = (gl_x + x * 60 < 130 and len(count_garbage) != 3)
        if (gl_x, gl_y) in garbage_coords and (gl_x, gl_y) in count_garbage:
            block_garbage.append((gl_x, gl_y))
        if len(count_garbage) == 3:
            if (gl_x + x * 60, gl_y + y * 60)\
               in garbage_coords:
                if (gl_x + x * 60, gl_y + y * 60) not in block_garbage:
                    flag_walle = 0
        if len(count_garbage) == 0:
            if 10 <= gl_x <= 130:
                flag_walle = 1
                if gl_x + x * 60 < 10 or gl_x + x * 60 > 910:
                    flag_walle = 0
                if gl_y + y * 60 < 10 or gl_y + y * 60 > 790:
                    flag_walle = 0
        elif (gl_x + x * 60, gl_y + y * 60) in block_coords:
            flag_walle = 1
        elif condition1 or condition2:
            flag_walle = 0
        elif len(count_garbage) == 0 and gl_x < 130:
            flag_walle = 1
        elif gl_y + y * 60 < 10 or gl_y + y * 60 > 790:
            flag_walle = 0
        elif len(count_garbage) == 0 and gl_x + x * 60 > 970:
            flag_walle = 0
        elif len(count_garbage) == 3 and gl_x + x * 60 < 10:
            flag_walle = 0
        if flag_walle:
            self.rect.x += x * 60
            self.rect.y += y * 60
            gl_x += x * 60
            gl_y += y * 60


flag_board_garbage = 0
garbage_coords = []
name = []
walle_sprites = pygame.sprite.Group()
heart_sprites = pygame.sprite.Group()
gl_x = 912
gl_y = 372
flag_move = 0
block_coords = []
count_garbage = set()
block_garbage = []
running0 = 1
name_sound_image = 'sound_on.jpg'
count_blocks = 0
loops = -1
size = width, height = 1160, 800
screen = pygame.display.set_mode(size)
walle = Walle(walle_sprites)
board = Board(19, 13)
garbage = Garbage()
running = True
count_restart = 0
cube_coords = []


def main():
    global flag_board_garbage, garbage_coords, name, walle_sprites, screen
    global heart_sprites, gl_x, gl_y, flag_move, block_coords, garbage
    global count_garbage, block_garbage, running0, count_blocks, loops, size
    global width, height, walle, board, count_restart, name_sound_image
    global cube_coords
    pygame.init()
    pygame.display.set_caption('Board')
    size = width, height = 1160, 800
    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load('data\Background.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops)
    running = True
    if not count_restart:
        draw_intro()
    walle = Walle(walle_sprites)
    screen.fill('grey')
    screen.blit(pygame.image.load(
        'data\hhh.png'), (0, 0))
    board = Board(19, 13)
    board.set_view(10, 10, 60)
    garbage = Garbage()
    pygame.image.save(screen, 'data\screen.png')
    while running:
        screen.blit(pygame.image.load('data\screen.png'), (0, 0))
        walle.draw_walle()
        walle_sprites.draw(screen)
        garbage.update()
        arrow_bold = pygame.image.load(os.path.join('data',
                                                    'заново_bold.png'))
        if 1090 < pygame.mouse.get_pos()[0] < 1150:
            if 130 < pygame.mouse.get_pos()[1] < 190:
                screen.blit(arrow_bold, ((w - 1) * 60 + 11, 131))
        if len(count_garbage):
            garbage.draw_count_garbage()
        else:
            board.draw_grey_garbage()
        board.draw_sound()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 1090 < event.pos[0] < 1150:
                        if 130 < event.pos[1] < 190:
                            running = 0
                            draw_end(0)
                    if 1030 < pygame.mouse.get_pos()[0] < 1090:
                        if 130 < pygame.mouse.get_pos()[1] < 190:
                            if name_sound_image == 'sound_on.jpg':
                                pygame.mixer.music.pause()
                                name_sound_image = 'sound_off.jpg'
                                board.draw_sound()
                            else:
                                pygame.mixer.music.unpause()
                                name_sound_image = 'sound_on.jpg'
                                board.draw_sound()
            if event.type == pygame.QUIT:
                running = False
                loops = 0
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == 'enter':
                    Cube_garbage()
                    if count_blocks == 20:
                        running = 0
                        draw_end(1)
                if key_name == 'left' or key_name == '[4]':
                    x_plus = -1
                    y_plus = 0
                    flag_move = 1
                elif key_name == 'right' or key_name == '[6]':
                    x_plus = 1
                    y_plus = 0
                    flag_move = 1
                elif key_name == 'up' or key_name == '[8]':
                    x_plus = 0
                    y_plus = -1
                    flag_move = 1
                elif key_name == 'down' or key_name == '[2]':
                    x_plus = 0
                    y_plus = 1
                    flag_move = 1
                else:
                    flag_move = 0
                if flag_move:
                    walle.draw_walle(x=x_plus, y=y_plus, flag_walle=1)
                    if (gl_x, gl_y) in garbage_coords:
                        block_coords.append((gl_x, gl_y))
        pygame.display.flip()
        pygame.time.Clock().tick(50)
    pygame.quit()

main()
