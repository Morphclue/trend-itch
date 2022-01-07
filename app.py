import requests
from xml.etree.ElementTree import fromstring


def fetch(url: str, page: int):
    content = requests.get(url, params={'page': page}).content
    xml = fromstring(content)


if __name__ == '__main__':
    fetch('https://itch.io/games/made-with-godot.xml', 1)
