import requests


IGNORED_STATUES = (200,)


def get_location_info():
    url_status = requests.get('http://ip-api.com/')

    if url_status not in IGNORED_STATUES:
        responce = requests.get('http://ip-api.com/json/').json()
    else:
        responce = 'Geolocation API not available'

    return f'You in {responce["country"]}, {responce["city"]}.'


if __name__ == '__main__':
    print(get_location_info())
    
