import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=20"  # Lista de Pokémon, no uno solo

response = requests.get(url)
data = response.json()

# Verifica qué hay dentro del JSON
print(data.keys())  # Esto debe mostrar: dict_keys(['count', 'next', 'previous', 'results'])

# Ahora accede al primer Pokémon
pokemon = data["results"][0]["name"]

print(pokemon)
