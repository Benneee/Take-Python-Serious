# Testing primer
import unittest

def add(x, y):
    # The assert keyword will evealuate to none if the conditions are met
    assert isinstance(x, int) and isinstance(y, int), "Both arguments must be integers"
    return x + y

# print(add(3, 5))

# Assertions will be made about the code to expect that it meets certain conditions so our code does not break

def multiply(a, b):
    # total = 0
    # for _ in range(a):
    #     total += b
    # return total
    return a * b


class MultiplyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)


if __name__ == "__main__":
    unittest.main()