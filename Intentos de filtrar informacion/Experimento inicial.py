import requests
import random #para hacer mas facil el que agarre un numero aleatorio
url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Lista de Pokémon, no uno solo
#Nota, modifuque el 20 por 151 para que tomara los priemeros 151 pokemons (primera generacion)

response = requests.get(url)
data = response.json()

# Verifica qué hay dentro del JSON
print(data.keys())  # Esto debe mostrar: dict_keys(['count', 'next', 'previous', 'results'])  #este se puede quitar sin problemas
x = random.randrange(1, 151) #En un rango de 1 a 151 elije un numero y lo guarda en X
# Ahora accede al Pokémon
pokemon = data["results"][x]["name"]

print(pokemon)
