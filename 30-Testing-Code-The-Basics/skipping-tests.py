import unittest

class TestSkippingStuff(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    # Skipping this test
    # 's' appears in the terminal to signify this test has been skipped
    @unittest.skip('To be implemented later')
    def test_multiplication(self):
        pass

if __name__ == '__main__':
    unittest.main()