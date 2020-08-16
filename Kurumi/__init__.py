from Kurumi.utils.network import Network
from Kurumi.models.anime import Anime
import atexit
import asyncio
import json

class Kurumi():
    def __init__(self, base_url="https://animepahe.com"):
        self.network = Network(base_url)
        self.loop = asyncio.get_event_loop()
        atexit.register(self.__cleanup)

    def __cleanup(self):
        self.loop.run_until_complete(self.network.close())

    async def search_async(self, query, results=12):
        res = await self.network.get(f'/api?m=search&l={results}&q={query}')
        json_response = json.loads(await res.text())
        return [Anime(anime, self.network, self.loop) for anime in json_response['data']]

    def search(self, query, results=12):
        # I have no idea how asyncio works or how i'm supposed to use the aiohttp session, sorry!
        # Ok might have figured it out not sure
        return self.loop.run_until_complete(self.search_async(query, results))
