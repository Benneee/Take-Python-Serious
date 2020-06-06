# import urllib.request
from urllib.request import urlopen

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"