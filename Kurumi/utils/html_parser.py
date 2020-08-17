import re
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")
        
    def get_full_m3u8_url(self):
        return f"{self.get_cdn()}/stream/{self.get_kwik_poster_url().replace('.jpg', '').replace('https://i.kwik.cx/snapshot/','')}/uwu.m3u8"

    def get_cdn(self):
        regex = re.search('kwik\|key\|(..)\|(..)\|stream', self.html)
        region = regex.group(1)
        server = regex.group(2)
        cdn_url = f"https://cdn-{region}-{server}.nextstream.org"
        return cdn_url

    def get_kwik_poster_url(self):
        return self.soup.find("video").get("poster")