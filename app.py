import csv

import requests
from xml.etree.ElementTree import fromstring

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


def dict_to_csv(data: dict, name: str):
    file = open(name + '.csv', 'w', encoding='utf-8')
    writer = csv.writer(file)
    for key, value in data.items():
        writer.writerow([key, value])
    file.close()


if __name__ == '__main__':
    dict_to_csv(fetch_all_pages('https://itch.io/games/made-with-flickgame.xml'), 'flickgame')
