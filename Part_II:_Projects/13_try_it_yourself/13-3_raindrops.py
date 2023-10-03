import sys
import pygame
from pygame.sprite import Sprite
from random import randint


class Drop(Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("raindrop.png")
        self.rect = self.image.get_rect()

    def update(self, speed):
        self.rect.y += speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Raindrops")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = pygame.Color("SkyBlue")
        self.raindrops = pygame.sprite.Group()
        self.drops_spacing = 2
        self.drops_speed = 3
        # self.drop = Drop(self)
        self._create_drops()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.raindrops.draw(self.screen)
            self._update_drops()
            pygame.display.flip()
            self.clock.tick(60)

    def _create_drops(self):
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        screen_width, screen_height = self.screen.get_size()
        print(drop_width, drop_height, screen_width, screen_height)
        # sys.exit()

        current_x, current_y = drop_width, drop_height
        while current_y < (screen_height - 2 * drop_height):
            while current_x < (screen_width - 2 * drop_width):
                self._new_drop(current_x, current_y)
                current_x += self.drops_spacing * drop_width
                # finished a row; reset x value, and increment y value.
            current_x = drop_width
            current_y += self.drops_spacing * drop_height

    def _new_drop(self, x_position, y_position):
        new_star = Drop(self)
        w = int(new_star.rect.width * 0.5)
        h = int(new_star.rect.height * 0.5)
        new_star.rect.x = x_position + randint(-w, w)
        new_star.rect.y = y_position + randint(-h, h)
        self.raindrops.add(new_star)

    def _update_drops(self):
        self.raindrops.update(self.drops_speed)
        h = self.screen.get_height()
        for d in self.raindrops.copy():
            if d.rect.top >= h:
                self.raindrops.remove(d)


if __name__ == "__main__":
    game = Game()
    game.run_game()
