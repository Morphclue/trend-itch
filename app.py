import requests
from xml.etree.ElementTree import fromstring


def fetch(url: str, page: int) -> dict:
    content = requests.get(url, params={'page': page}).content
    xml = fromstring(content)
    games = dict()

    if not len(xml.findall('channel/item')):
        return games

    for item in xml.iterfind('channel/item'):
        title = item.findtext('title')
        publish_date = item.findtext('pubDate')
        games[title] = publish_date

    return games


if __name__ == '__main__':
    print(fetch('https://itch.io/games/made-with-godot.xml', 10000))
