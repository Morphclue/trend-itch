import requests
from xml.etree.ElementTree import fromstring


def fetch(url: str, page: int) -> bool:
    content = requests.get(url, params={'page': page}).content
    xml = fromstring(content)

    if not len(xml.findall('channel/item')):
        return False

    return True


if __name__ == '__main__':
    print(fetch('https://itch.io/games/made-with-godot.xml', 10000))
