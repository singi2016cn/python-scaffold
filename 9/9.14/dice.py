"""骰子"""

from random import randint


class Die:
    """骰子"""

    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        return randint(1, self.side)


dice = Die()
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())

dice = Die(10)
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())

dice = Die(20)
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
print(dice.roll_die())
