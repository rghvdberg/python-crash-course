# 12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop,
# print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run
# the program and press various keys to see how Pygame responds.

import sys
import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            print(event.key)
    screen.fill((255, 255, 255))
    pg.display.flip()
    clock.tick(60)
