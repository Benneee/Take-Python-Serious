import unittest

class TruthinessAndFalsiness(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue(3 < 5)

    def test_falsiness(self):
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse([])

if __name__ == '__main__':
    unittest.main()