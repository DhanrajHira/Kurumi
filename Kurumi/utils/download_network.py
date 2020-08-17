import requests

class DownloadNetwork(object):

    def __init__(self):
        headers = {
            "referer": "https://kwik.cx",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        }
        self.__session__ = requests.Session()
        self.__session__.headers.update(headers)

    def get(self, url):
        response = self.__session__.get(url)
        return response