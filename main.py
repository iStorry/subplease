import argparse
import requests

parser = argparse.ArgumentParser(description="Fetch the magnet link.")
parser.add_argument("--anime", type=str, help="Anime name", required=True)
parser.add_argument("--episode", type=int, help="The episode number.")
args = parser.parse_args()

if args.episode is None:
    print("Episode number is not specified will search for the latest episode.")

anime_name = args.anime.lower().replace(" ", "-")

session = requests.Session()
fetch = session.get(f"https://subsplease.org/shows/{anime_name}/")
sid = fetch.text.split('sid="')[1].split('"')[0]
fetch = session.get(f"https://subsplease.org/api/?f=show&tz=Asia/Tokyo&sid={sid}")
data = fetch.json()
episode_list = data["episode"]
episode_keys = list(episode_list.keys())

episode_number = episode_keys[0]
if args.episode:
    # Check if title contains the number and get the index
    episode_key = [key for key in episode_keys if str(args.episode) in key]
    if episode_key:
        episode_number = episode_key[0]

obj = episode_list[episode_number]["downloads"][2]["magnet"]
print(obj)
