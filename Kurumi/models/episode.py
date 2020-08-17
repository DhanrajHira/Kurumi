import json
from Kurumi.utils.html_parser import HtmlParser
from Kurumi.utils.download_network import DownloadNetwork
from Kurumi.models.kwik_data import KwikVideoData
from Yukinoshita.downloader import Downloader, MultiThreadDownloader

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

    def __init__(self, json_response, network):
        self.__network__ = network
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

    async def get_kwik_data(self):
        params = {
            "m": "links",
            "id": self.anime_id,
            "session": self.session,
            "p": "kwik"
        }
        response = await self.__network__.get_from_api(params=params)
        return [KwikVideoData(tuple(quality.keys())[0], quality[tuple(quality.keys())[0]], self.__network__) for quality in response["data"]] #This is horrible, it is not readable at all. We need to find a better way.
        
    async def download(self, quality, file_name=None, multi_threading=False, max_threads=None, use_ffmpeg=True, delete_chunks=True):
        download_network = DownloadNetwork()
        kwik_data = await self.get_kwik_data()
        for video_data in kwik_data:
            if video_data.quality == quality:
                selected_data = video_data
                break 
        m3u8 = await selected_data.get_m3u8()
        if file_name is None:
            file_name = f"{self.id}-{self.episode}"
        if multi_threading:
            dl = MultiThreadDownloader(download_network, m3u8, file_name, self.id, max_threads, use_ffmpeg, {}, delete_chunks)
        else:
            dl = Downloader(download_network, m3u8, file_name, self.id, use_ffmpeg, delete_chunks, {})
        dl.download()
        dl.merge()
        dl.remove_chunks()