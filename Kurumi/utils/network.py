import aiohttp

class Network(object):

    def __init__(self, base_url):
        self.BASE_URL = base_url
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        }
        self.__client__ = aiohttp.ClientSession(headers=headers)

    async def get(self, data):
        response = await self.__client__.get(await self.create_url(data)) 
        return response
        
    async def close(self):
        await self.__client__.close()

    async def create_url(self, params):
        url_params = ''
        for x in params:
            url_params += f'&{x}={params[x]}'
        return f"{self.BASE_URL}/api{url_params.replace('&', '?', 1)}"