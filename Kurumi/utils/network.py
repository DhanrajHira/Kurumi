import aiohttp

class Network(object):

    def __init__(self, base_url):
        self.BASE_URL = base_url
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "referer": 'https://animepahe.com'
        }
        self.__client__ = aiohttp.ClientSession(headers=headers)

    async def get(self, url, headers=None, params=None):
        response = await self.__client__.get(url, headers=headers, params=params)
        return response
        
    async def get_from_api(self, headers=None ,params=None):
        response = await self.__client__.get(self.BASE_URL, headers=headers, params=params)
        json = await response.json()
        return json

    async def close(self):
        await self.__client__.close()

