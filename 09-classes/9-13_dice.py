from random import randint


class Die:
    """A simple model of a die"""

    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self) -> int:
        return randint(1, self.sides)


six_sides = Die(6)
print(six_sides.roll_die())

ten_sides = Die(10)
print(ten_sides.roll_die())
