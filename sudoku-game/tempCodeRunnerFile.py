import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{400},{100}"
surface = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Sudoku")

pygame.font.init()
game_font = pygame.font.SysFont(name='Comic Sa ns MS', size=50)  # ✅ fixed here

grid = Grid(pygame,game_font)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0], pos[1])

    surface.fill((0, 0, 0))

    grid.draw_all(pygame,surface)

    pygame.display.flip()
 