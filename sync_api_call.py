import requests


def sync_api_calls(postal_codes):
    url = "https://api.zippopotam.us/ca/{}"
    data = []
    for code in postal_codes:
        response = requests.get(url.format(code))
        data.append(response.json())
    return data
