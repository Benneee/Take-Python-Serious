import unittest
# These classes are used during expensive processes e.g connecting to a DB during a test
class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # No matter how many test cases we have in this suite, this will only run once
        print('Runs once before the test suite starts')

    @classmethod
    def tearDownClass(cls):
        print('Runs once after the test cases in the test suite runs')

    def setUp(self):
        print('Runs before each test')
    
    def tearDown(self):
        print('Runs after each test')

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__ == "__main__":
    unittest.main()