import unittest

def explicit_return_sum(a, b):
    return a + b

def implicit_return_sum(a, b):
    # expected to return None
    print(a + b)


class TestNone(unittest.TestCase):
    def test_sum_functions(self):
        self.assertIsNotNone(explicit_return_sum(4, 6))
        self.assertIsNone(implicit_return_sum(4, 7))

if __name__ == '__main__':
    unittest.main()