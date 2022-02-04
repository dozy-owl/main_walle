import pygame
import sys

from rules import *

pygame.init()


def draw_intro():
    global running, running0, waiting
    running0 = 1
    while running0:
        fon = pygame.image.load('data\start.png')
        fon_bold = pygame.image.load('data\start_bold.png')
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running0 = False
                running = 0
                waiting = 0
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 823 < event.pos[0] < 1078:
                        if 603 < event.pos[1] < 705:
                            draw_rules()
                            running0 = 0
        screen.blit(fon, (0, 0))
        if 823 < pygame.mouse.get_pos()[0] < 1078:
            if 603 < pygame.mouse.get_pos()[1] < 705:
                screen.blit(fon_bold, (0, 0))
        pygame.display.flip()

size = width, height = 1160, 800
screen = pygame.display.set_mode(size)
