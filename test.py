from Kurumi import Kurumi

client = Kurumi()
print(client.search('Naruto')[0].get_episodes().get_episode_by_number(4))
