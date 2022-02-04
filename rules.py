import pygame
import sys

pygame.init()


def draw_rules():
    global running, running0, waiting
    running1 = 1
    while running1:
        fon_rules = pygame.image.load('data\game_rules.jpg')
        fon_rules_bold = pygame.image.load('data\game_rules_bold.jpg')
        size = width, height = 1160, 800
        screen = pygame.display.set_mode(size)
        screen.blit(fon_rules, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                waiting = 0
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 985 < event.pos[0] < 1128:
                        if 702 < event.pos[1] < 746:
                            running0 = 0
                            running1 = 0
        screen.blit(fon_rules, (0, 0))
        if 985 < pygame.mouse.get_pos()[0] < 1128:
            if 702 < pygame.mouse.get_pos()[1] < 746:
                screen.blit(fon_rules_bold, (0, 0))
        pygame.display.flip()
