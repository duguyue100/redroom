""""This is for cat."""


class Cat(object):
    """This is a cat class."""

    def __init__(self, height, width, weight, num_eyes):
        """Init function.

        Parameter
        ---------
        height : int
            the height of the cat
        width : int
            the width of the cat.
        """
        self.height = height
        self.width = width
        self.weight = weight

    def get_weight(self):
        """get weight."""
        return self.weight
