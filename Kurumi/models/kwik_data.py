from Kurumi.utils.html_parser import HtmlParser
from m3u8 import M3U8

class KwikVideoData(object):

    def __init__(self, quality, json_response, network):
        self.__network__ = network
        self.quality = quality
        self.filesize = json_response.get('filesize', None)
        self.crc32 = json_response.get('crc32', None)
        self.revision = json_response.get('revision', None)
        self.fansub = json_response.get('fansub', None)
        self.audio = json_response.get('audio', None)
        self.disc = json_response.get('disc', None)
        self.hq = json_response.get('hq', None)
        self.kwik = json_response.get('kwik', None)
        self.kwik_adfly = json_response.get('kwik_adfly', None)
        self.kwik_shst = json_response.get('kwik_shst', None)
        self.server = json_response.get('server', None)
    
    def __repr__(self):
        return f'<Quality {self.quality}p>'
    
    async def get_m3u8_url(self):
        headers = {"referer": "https://kwik.cx"}
        html_response = await self.__network__.get(self.kwik, headers=headers)
        html = await html_response.text()
        parser = HtmlParser(html)
        m3u8_url = parser.get_full_m3u8_url()
        return m3u8_url
    
    # To get the m3u8 content the referer has to be https://kwik.cx

    async def get_m3u8(self):
        headers = {"referer": "https://kwik.cx"}
        m3u8_url = await self.get_m3u8_url()
        response = await self.__network__.get(m3u8_url, headers=headers)
        return M3U8(await response.text())