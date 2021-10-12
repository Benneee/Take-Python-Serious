import unittest

# Used to check if a value exist in an iterable

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        self.assertIn('k', 'king')
        self.assertIn(1, [1, 2, 4, 5])

    def test_none_inclusion(self):
        self.assertNotIn(10, [1, 2, 3])
        self.assertIn('k', 'queen')

if __name__ == '__main__':
    unittest.main()