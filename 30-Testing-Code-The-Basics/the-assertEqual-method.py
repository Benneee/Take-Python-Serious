import unittest

# The Assert Method
# An assertion is a validation that an operation returns an expected value

# The assertEqual method receives two arguments and asserts that both arguments are equal
class TestStringMethod(unittest.TestCase):
    # Every test case we will need to create will inherit from the TestCase class
    # Each method defined here represents one test
    # Each test method should start with the string 'test' as this is how unittest finds the test cases we define

    # It is good for organisation that one test should have just one assertion
    def test_split(self):
        self.assertEqual("a-b-c".split('-'), ['a', 'b', 'c'])
        # If this test passes, we see a dot in the output terminal, that dot signifies that
        # all the assertions made in the test were met. The dot also represents a single test

    def test_count(self):
        self.assertEqual("beautiful".count('u'), 2)

        # For every single failing test, we are going to have an F in the output
        # self.assertEqual("beautiful".count('z'), 3)

if __name__ == "__main__":
    unittest.main()