import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'daaa3e82a4539e82c46eb5fcbfabe12e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = { 
    "name": "wiwiwi",
    "photo_id": 1008
    }
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text) 
pokemon_id = response_create.json()['id']
print(pokemon_id)

body_put = {
    "pokemon_id": "322438",
    "name": "slivka",
    "photo_id": 985
}
response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
message = response_put.json()['message']
print(message)

body_add = {
    "pokemon_id": "322438"
}
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
message = response_add.json()['message']
print(message)