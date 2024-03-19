import requests

URL = 'https://api.pokemonbattle.me/v2/'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : '3b1fbdcc03e5ee6802f4be2292fdf8bb'}


body = {
    "name": "Буль",
    "photo": "https://dolnikov.ru/pokemons/albums/032.png"
    }

response = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body)

print(response.text)

body = {
    "pokemon_id": "14135",
    "name": "Гуль",
    "photo": "https://dolnikov.ru/pokemons/albums/032.png"
}

response = requests.put(url = f'{URL}pokemons', headers = HEADERS, json = body)

print(response.text)

body = {
    "pokemon_id": "14135"
}

response = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)