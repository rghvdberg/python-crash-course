""" 13-5. Sideways Shooter Part 2: We’ve come a long way since Exercise 12-6,
Sideways Shooter. For this exercise, try to develop Sideways Shooter to the
same point we’ve brought Alien Invasion to. Add a fleet of aliens, and make
them move sideways toward the ship. Or, write code that places aliens at ran-
dom positions along the right side of the screen and then sends them toward
the ship. Also, write code that makes the aliens disappear when they’re hit. """


import pygame
from sys import exit
from pygame.sprite import Sprite


class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.color = pygame.Color("red")
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.ship_speed = 10

        # Movement flags; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False

        self.x = 0
        self.y = float(self.rect.y)

    def update(self):
        """Update the ship's position based on the movement flag."""

        if self.moving_up and self.rect.top > 10:
            self.y -= self.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed

        # Update rect objecct from self.x
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw_ship(self):
        pygame.draw.polygon(
            self.screen, self.color, [[0, self.y], [25, self.y + 25], [0, self.y + 50]]
        )

    pass


class Bullet(Sprite):
    """A class to manage bu xxllets fired from the ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.color = pygame.Color("#E7DFCF")

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 25, 3)
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.x = 0.0
        self.y = float(self.rect.y + 25)

    def update(self):
        """Move the bullet right over the screen."""
        # Update the decimal position of the bullet.
        self.x += 10
        # Update the rect position.
        self.rect.y = int(self.y)
        self.rect.x = int(self.x)

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.y = float(self.rect.y)
        self.color = pygame.Color("red")
        self.radius = 20

    def update(self):
        pass

    def check_edges(self):
        pass

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.background_color = pygame.Color("#182030")
        # https://www.color-name.com/dark-space.color
        pygame.display.set_caption("Sideways Shooter")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    self._handle_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._handle_keyup(event)

            self.ship.update()

            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.x >= 1200:
                    self.bullets.remove(bullet)

            # Draw the screen
            self.screen.fill(self.background_color)

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.ship.draw_ship()
            pygame.display.flip()
            self.clock.tick(60)

    def _handle_keydown(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < 5:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _handle_keyup(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


game = Game()
game.run()
