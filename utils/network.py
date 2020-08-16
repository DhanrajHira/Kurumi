import aiohttp
import random

class Network(object):

    BASE_URL = "https://animepahe.com/api"

    def __init__(self):
        xsrf_token = self.__generate_xsrf_token__()
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "cookie": f"XSRF-TOKEN={xsrf_token};",
        }
        self.__client__ = aiohttp.ClientSession(headers=headers)

    async def get(self, url):
        response = await self.__client__.get(url) 
        return response
        
    async def close(self):
        await self.__client__.close()

    @staticmethod
    def __generate_xsrf_token__():
        characters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]
        return "".join(random.choice(characters) for i in range(246))        