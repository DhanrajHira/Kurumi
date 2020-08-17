from Kurumi.utils.network import Network
from Kurumi.models.anime import Anime
import asyncio
import json

class Kurumi():
    def __init__(self, base_url="https://animepahe.com/api"):
        self.network = Network(base_url)

    async def search(self, query, results=12):
        params = {
            "m": "search",
            "l": results,
            "q": query
        }
        json_response = await self.network.get_from_api(params=params)
        return [Anime(anime, self.network) for anime in json_response["data"]]
    
    async def close(self):
        await self.network.close()