from pygame import Color


class Settings:
    """A class to store all settings for Alien Invastion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = Color("#e6e6e6")
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = Color("#3c3c3c")
        self.bullet_allowed = 3
