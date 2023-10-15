import csv
import os
import requests

from xml.etree.ElementTree import fromstring

engines = [
    'renpy',
    'adventure-game-studio',
    'stencyl',
    'rpg-maker',
    'gb-studio',
    'unreal-engine',
    'gamemaker',
    'unity',
    'pico-8',
    'godot',
    'love2d',
    'tyranobuilder',
    'bitsy',
    'libgdx',
    'twine',
    'clickteam-fusion',
    'defold',
    'appgamekit',
    'construct',
    'cryengine',
    'gdevelop',
    'puzzlescript',
    'tic-80',
    'p5js',
    'multimedia-fusion',
    'processing',
    'flickgame',
    'dragonruby-gtk',
    'ctjs',
    'easyrpg',
    'rpg-in-a-box',
    'impact',
    'melonjs',
    'pixel-vision-8',
    'torque-3d',
    'ogre3d',
    'mugen',
    'torque-2d',
    'amulet',
    'scummvm',
    'adlengine',
    'superpowers',
    'orx'
]

session = requests.session()


def fetch(url: str, page: int) -> dict:
    content = session.get(url, params={'page': page}).content
    xml = fromstring(content)
    games = dict()

    for item in xml.iterfind('channel/item'):
        title = item.findtext('title')
        publish_date = item.findtext('pubDate')
        games[title] = publish_date

    return games


def fetch_all_pages(url: str) -> dict:
    page = 1
    all_games = dict()

    while True:
        result = fetch(url, page)
        if not len(result):
            break
        all_games = {**all_games, **result}
        page += 1

    return all_games


def fetch_all_engines():
    for index, engine in enumerate(engines):
        url = f'https://itch.io/games/made-with-{engine}.xml'
        print(f"Currently fetching: {index}/{len(engines)} - {engine}")
        with open(os.path.join('output', f"{engine}.csv"), 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            all_games = fetch_all_pages(url)
            for key, value in all_games.items():
                writer.writerow([key, value])
    print("Fetching done.")


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    fetch_all_engines()
