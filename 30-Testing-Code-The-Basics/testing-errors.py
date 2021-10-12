import unittest

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_divide_another_way(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
    
if __name__ == '__main__':
    unittest.main()