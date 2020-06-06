import unittest
from unittest.mock import patch

class WebRequestTest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_execute_with_success_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch('urllib.request.urlopen')
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()