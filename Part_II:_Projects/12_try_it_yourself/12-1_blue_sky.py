import sys
import pygame


class BlueSky:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = pygame.Color("#87ceeb")
        # self.bg_color = (135, 206, 235)  # rgb(135,206,235)
        pygame.display.set_caption("Blue Sky")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)


bluesky = BlueSky()
bluesky.run()
