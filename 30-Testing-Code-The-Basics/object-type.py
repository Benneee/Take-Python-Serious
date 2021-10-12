# Test whether an object or value is an instance of or made from a particular class
import unittest

class ObjectTypeTests(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(8.765, float)
        self.assertIsInstance([], list)

    
    def test_not_is_instance(self):
        self.assertNotIsInstance(8.765, int)
        self.assertNotIsInstance([], int)

if __name__ == '__main__':
    unittest.main()