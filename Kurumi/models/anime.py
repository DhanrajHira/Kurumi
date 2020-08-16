import json
from Kurumi.models.episode import Episode, Episodes

class Anime(object):

    def __init__(self, json_response, network, loop):
        self.__network = network
        self.__loop = loop
        self.id = json_response.get("id", None)
        self.episodes = json_response.get("episodes", None)
        self.title = json_response.get("title", None)
        self.poster = json_response.get("poster", None)
        self.relevance = json_response.get("relevance", None)
        self.score = json_response.get("score", None)
        self.season = json_response.get("season", None)
        self.session = json_response.get("session", None)
        self.status = json_response.get("status", None)
        self.slug = json_response.get("status", None)
        self.type = json_response.get("type", None)
        self.year = json_response.get("year", None)

    def __repr__(self):
        return f"<Anime {self.id}>"

    async def get_episodes_async(self):
        if self.episodes < 1:
            pages = 1
        else:
            pages = int(self.episodes / 30)
        page = 1
        episodes = []
        while page <= pages:
            data = {'m': 'release', 'id': self.id, 'l': 30, 'sort': 'episode_asc', 'page': page}
            res = await self.__network.get(data)
            res = json.loads(await res.text())
            if page == 1:
                pages = res['last_page']
            episodes += [Episode(episode, self.__network, self.__loop) for episode in res['data']]
            page += 1
        return Episodes(episodes)

    def get_episodes(self):
        return self.__loop.run_until_complete(self.get_episodes_async())