import requests
import pytest
from async_api_call import async_api_call
from app import read_data

app_url = 'http://127.0.0.1:5000/'
external_api_url = 'https://api.zippopotam.us/ca/'


def test_external_api_status_code_200():
    response = requests.get(external_api_url + 'n7s')
    assert response.status_code == 200


def test_external_api_response_json():
    response = requests.get(external_api_url + 'n7s')
    assert response.headers['Content-type'] == 'application/json'


def test_home_page_200():
    response = requests.get(app_url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_call_200():
    response = await async_api_call(read_data())
    assert type(response) == list
