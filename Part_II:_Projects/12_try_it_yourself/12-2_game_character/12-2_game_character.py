import sys
import pygame


class Character:
    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class GameCharacter:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.alien = Character(self)
        pygame.display.set_caption("Blue Sky")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((135, 206, 235))  # rgb(135,206,235)
            self.alien.blitme()
            pygame.display.flip()
            self.clock.tick(60)


bluesky = GameCharacter()
bluesky.run()
