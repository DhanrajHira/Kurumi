from Kurumi.kurumi import Kurumi
import asyncio

async def main():
    client = Kurumi()
    res = await client.search("date")
    anime = res[2]
    print(anime.title)
    episodes = await anime.get_episodes()
    episode = episodes.get_episode_by_number(2)
    await episode.download("720", delete_chunks = False)
    await client.close()

asyncio.run(main())