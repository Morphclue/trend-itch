import requests
from xml.etree.ElementTree import fromstring


def fetch(url: str, page: int) -> dict:
    content = requests.get(url, params={'page': page}).content
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


if __name__ == '__main__':
    fetch_all_pages('https://itch.io/games/made-with-flickgame.xml')
