import pygal

from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides=6, dice_num=1):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        self.dice_num = dice_num

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    def labels(self):
        hist = pygal.Bar()

        if self.dice_num == 1:
            hist.title = "Results of rolling a D6 die " + str(self.num_sides) + " times."
        else:
            hist.title = "Results of rolling " + str(self.dice_num) + " D6 die " + str(self.num_sides) + " times."

        hist.x_labels = []
        for num in range(self.dice_num, self.num_sides * self.dice_num):
            hist.x_labels.append(num)

        hist.x_title = "Result"
        hist.y_title = "Frequency of Result"
