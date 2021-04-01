import requests


IGNORED_STATUES = (200,)


def get_location_info() -> str:
    """Возвращает местоположение по IP."""
    url_status = requests.get('http://ip-api.com/')

    if url_status not in IGNORED_STATUES:
        response = requests.get('http://ip-api.com/json/').json()
    else:
        response = 'Geolocation API not available.'

    return f'You in {response["country"]}, {response["city"]}.'


if __name__ == '__main__':
    print(get_location_info())
