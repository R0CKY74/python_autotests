import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : '3b1fbdcc03e5ee6802f4be2292fdf8bb'}


def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {"trainer_id" : 146})
    assert response.status_code == 200

def test_part_of_response():
        response = requests.get(url = f'{URL}trainers', params = {"trainer_id" : 146})
        assert response.json()['data'][0]['trainer_name'] == 'Микки'
