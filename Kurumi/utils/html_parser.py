from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def get_m3u8_url(self):
        link_tags = self.soup.findAll("link", {"rel": "dns-prefetch"})
        cdn_base_url = None
        for link_tag in link_tags:
            if "cdn-" in link_tag.get("href"):
                cdn_base_url = link_tag.get("href")
                break
        
    def get_kwik_poster_url(self):
        return self.soup.find("video").get("poster")