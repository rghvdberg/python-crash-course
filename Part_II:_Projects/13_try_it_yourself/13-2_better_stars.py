import sys
import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Better Stars")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 400))
        self.bg_color = pygame.Color("#191970")
        self.stars = pygame.sprite.Group()
        self.star = Star(self)
        self._create_stars()

    def run_game(self):
        print("run_game")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def _create_stars(self):
        print("_create_stars")
        star = Star(self)
        star_width, star_height = star.rect.size
        screen_width, screen_height = self.screen.get_size()
        print(star_width, star_height, screen_width, screen_height)
        # sys.exit()

        current_x, current_y = star_width, star_height
        while current_y < (screen_height - 2 * star_height):
            while current_x < (screen_width - 2 * star_width):
                self._new_star(current_x, current_y)
                current_x += 5 * star_width
                # finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 5 * star_height

    def _new_star(self, x_position, y_position):
        new_star = Star(self)
        w = new_star.rect.width * 2
        h = new_star.rect.height * 2
        new_star.rect.x = x_position + randint(-w, w)
        new_star.rect.y = y_position + randint(-h, h)
        self.stars.add(new_star)


if __name__ == "__main__":
    game = Game()
    game.run_game()
