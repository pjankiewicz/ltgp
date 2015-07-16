
import sys

import pygame
from pygame.locals import *

from ants import get_best_ant

from const import *

FOOD_CELL = "#"
EMPTY_CELL = "."
ANT_CELL = "S"


def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))


def draw_pixel(surface, pos, col, size=SCALE):
    x, y = pos
    for x_ in range(size):
        for y_ in range(size):
            surface.set_at((x-x_, y-y_), col)


def draw_state(surface, ant):
    for x, row in enumerate(ant.matrix_exc):
        for y, col in enumerate(row):
            # FOOD
            if col == "food":
                draw_pixel(surface, (x*SCALE, y*SCALE), CLR_FOOD)
            elif col == "passed":
                draw_pixel(surface, (x*SCALE, y*SCALE), CLR_PASSED)

    ant_pos = (ant.row*SCALE, ant.col*SCALE)
    draw_pixel(surface, ant_pos, CLR_ANT)


def pprint(expr):
    indent = 0
    for l in expr:
        sys.stdout.write(l)
        if l == '(':
            indent += 1
            sys.stdout.write('\n' + indent * '\t')
        if l == ')':
            indent -= 1
            sys.stdout.write('\n' + indent * '\t')
        if l == ",":
            sys.stdout.write("\n" + indent * '\t')


def main():
    ant, hof, routine = get_best_ant()
    pprint(str(hof).replace(" ", ""))

    yes = raw_input("Continue?")

    ant._reset()
    scale = SCALE
    size = width, height = ant.matrix_row*SCALE, ant.matrix_col*SCALE

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("ANTS")
    clock = pygame.time.Clock()

    iteration = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0

        surface = pygame.Surface(size)
        surface.fill(CLR_BACKGROUND)
        draw_state(surface, ant)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

        routine()

        iteration += 1

if __name__ == "__main__":
    main()
