import unittest

class IdentityTests(unittest.TestCase):
    def test_similarity(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]

        # assertIs checks that two names in the program refers to the same object in the computer's memory
        # It checks for similarity and not equality
        self.assertIs(a, b)
        self.assertIsNot(b, c)

if __name__ == '__main__':
    unittest.main()