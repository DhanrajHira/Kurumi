class Anime(object):

    def __init__(self, json_response):
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
