# Patch is a feature that can be used as a function or decorator to create a MagicMock object in place of some module

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
    def test_execute_with_success_response(self):
        # Patch helps us avoid the dependencies the class we're testing is dependent on
        # Patch expects a 'target' argument
        # You should patch the target where it's been looked up, not where it is defined e.g where a function is called, not where it is defined
        
        # 'package.module.attribute'
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequest("http://google.com")
            self.assertEqual(wr.execute(), "Success")

    
    def test_execute_with_failure_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 400
            wr = WebRequest("http://google.com")
            self.assertEqual(wr.execute(), "Failure")  


if __name__ == "__main__":
    unittest.main()