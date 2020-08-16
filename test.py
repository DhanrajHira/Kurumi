from Kurumi import Kurumi

client = Kurumi()
print(client.search('Boruto')[0].get_episodes().get_episode_by_number(1).get_downloads()[0].get_m3u8())
