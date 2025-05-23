import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'daaa3e82a4539e82c46eb5fcbfabe12e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 36236

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert  response_get.json()['data'][0]['trainer_name'] == 'Sova'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Sova'), ('id', f'{TRAINER_ID}')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert  response_parametrize.json()['data'][0][key] == value    