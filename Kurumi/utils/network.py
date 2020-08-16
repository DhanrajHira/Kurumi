import aiohttp

class Network(object):

    def __init__(self, base_url):
        self.BASE_URL = base_url
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        }
        self.__client__ = aiohttp.ClientSession(headers=headers)

    async def get(self, url):
        response = await self.__client__.get(f"{self.BASE_URL}{url}") 
        return response
        
    async def close(self):
        await self.__client__.close()
