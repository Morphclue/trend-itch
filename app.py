import requests


def fetch(url: str, page: int):
    content = requests.get(url, params={'page': page}).content


if __name__ == '__main__':
    fetch('https://itch.io/games/made-with-godot.xml', 1)
