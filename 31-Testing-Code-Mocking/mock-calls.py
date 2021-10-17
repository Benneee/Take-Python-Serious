import unittest
from unittest.mock import MagicMock


class MockCallsTest(unittest.TestCase):
    def test_mock_calls(self):
        mock = MagicMock()
        mock()
        # To check that the mock was called
        mock.assert_called()

    def test_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()

    # To test if the mock object was called with some specific arguments
    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        mock.assert_called_with(1, 2, 3)

    def test_mock_attributes(self):
        mock = MagicMock()
        mock()
        mock(1,2)
        print(mock.called) # Tells us if the mock object has been called
        print(mock.call_count) # Shows the number of times the mock was called
        print(mock.mock_calls) # Shows how the mock object was called

if __name__ == '__main__':
    unittest.main()