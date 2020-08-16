import json
from Kurumi.utils.html_parser import HtmlParser

class Episodes(object):
    def __init__(self, episodes):
        self.episodes = episodes
    
    def __repr__(self):
        return f"<{len(self.episodes)} episodes>"
    
    def get_episode_by_number(self, number):
        for x in self.episodes:
            if x.episode == number:
                return x

class Episode(object):

    def __init__(self, json_response, network, loop):
        self.__network = network
        self.__loop = loop
        self.anime_id = json_response.get("anime_id", None)
        self.created_at = json_response.get("created_at", None)
        self.disc = json_response.get("disc", None)
        self.duration = json_response.get("duration", None)
        self.edition = json_response.get("edition", None)
        self.episode = json_response.get("episode", None)
        self.episode_2 = json_response.get("episode2", None)
        self.filler = json_response.get("filler", None)
        self.id = json_response.get("id", None)
        self.session = json_response.get("session", None)
        self.snapshot = json_response.get("snapshot", None)
        self.fansub = json_response.get("fansub", None)
        self.title = json_response.get("title", None)

    def __repr__(self):
        return f"<Episode {self.id}>"

    async def get_downloads_async(self):
        data = {'m': 'links', 'id': self.anime_id, 'session': self.session, 'p':'kwik'}
        res = await self.__network.get(data=data)
        json_response = json.loads(await res.text())
        return [Downloadable(list(dwn.keys())[0], dwn[list(dwn.keys())[0]], self.__network, self.__loop) for dwn in json_response['data']]

    def get_downloads(self):
        return self.__loop.run_until_complete(self.get_downloads_async())

class Downloadable(object):

    def __init__(self, quality, json_response, network, loop):
        self.__network = network
        self.__loop = loop
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
        return f'<Quality {self.quality}>'

    async def get_m3u8_async(self):
        res = await self.__network.get(url=self.kwik)
        return HtmlParser(await res.text()).get_full_url()
    
    def get_m3u8(self):
        return self.__loop.run_until_complete(self.get_m3u8_async())

    # To get the m3u8 content the referer has to be https://kwik.cx