import json
from Kurumi.models.episode import Episode, Episodes

class Anime(object):

    def __init__(self, json_response, network):
        self.__network__ = network
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
        return f"<Anime {self.title}>"

    async def get_episodes(self):
        if self.episodes < 1:
            pages = 1
        else:
            pages = (self.episodes // 30)+1
        episodes = []
        for page in range(pages):
            params = {
                "m": "release",
                "id": self.id,
                "l": 30,
                "sort": "episode_asc",
                "page": page
            }
            json_response = await self.__network__.get_from_api(params = params)
            episodes.extend([
                Episode(episode_data, self.__network__, self.title) for episode_data in json_response["data"]
                ])

        return Episodes(episodes)
