# 12-4. Rocket: Make a game that begins with a rocket in the center of the screen.
# Allow the player to move the rocket up, down, left, or right using the four arrow
# keys. Make sure the rocket never moves beyond any edge of the screen.

import sys
import pygame


class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("rocket_small.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.ship_speed = 10

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed

        if self.moving_up and self.rect.top > 10:
            self.y -= self.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed

        # Update rect objecct from self.x
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


class Rocket:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.ship = Ship(self)
        pygame.display.set_caption("Rocket")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._handle_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._handle_keyup(event)

            self.screen.fill((4, 26, 64))  # rgb(4,26,64)
            self.ship.update()
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

    def _handle_keydown(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

    def _handle_keyup(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


rocket = Rocket()
rocket.run()
