import csv

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
        dict_to_csv(fetch_all_pages(url), engine)
    print("Fetching done.")


def dict_to_csv(data: dict, name: str):
    file = open(f"{name}.csv", 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    for key, value in data.items():
        writer.writerow([key, value])
    file.close()


if __name__ == '__main__':
    fetch_all_engines()
