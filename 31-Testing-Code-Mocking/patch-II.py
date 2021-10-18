# Using patch as a decorator
import urllib, unittest
from urllib import request
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "Success"
        
        return "Failure"


# wr = WebRequest("http://google.com")
# wr.execute()

class WebRequestTest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_execute_with_success_response(self, mock_urlopen):
        # 'package.module.attribute'
        mock_urlopen.return_value.status = 200
        wr = WebRequest("http://google.com")
        self.assertEqual(wr.execute(), "Success")

    @patch('urllib.request.urlopen')
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 400
        wr = WebRequest("http://google.com")
        self.assertEqual(wr.execute(), "Failure")  


if __name__ == "__main__":
    unittest.main()