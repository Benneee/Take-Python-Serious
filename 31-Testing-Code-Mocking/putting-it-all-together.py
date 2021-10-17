import unittest
from unittest.mock import MagicMock

class Actor():
    def jump_out_of_helicopter(self):
        return "Nope, not doing it!"

    def light_on_fire(self):
        return "Heck no, where's my agent?"


class Movie():
    def __init__(self, actor):
        self.actor = actor

    def start_filming(self):
        self.actor.jump_out_of_helicopter()
        self.actor.light_on_fire()


class MovieTest(unittest.TestCase):
    def test_start_filming(self):
        stuntman = MagicMock()
        movie = Movie(stuntman)

        movie.start_filming()
        stuntman.jump_out_of_helicopter.assert_called()
        stuntman.light_on_fire.assert_called()


if __name__ == '__main__':
    unittest.main()