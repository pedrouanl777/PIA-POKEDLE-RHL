import requests
import json
base_url = "https://pokeapi.co/api/v2/"
pokemon = {}
def get_pokemon_info(id): #Una funcion para usar después 
    url = f"{base_url}/pokemon/{id}" #Esto para que podamos cambiar la url a lo que necesitamos, una url que puede cambiar la id
    response = requests.get(url)
    if response.status_code == 200: #Esto es por si la URL esta caida o tiene problemas no tire directamente error
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Fallo al recuperar la información {response.status_code}") #Aqui terminaria el programa si no logra conectar con la URL 

def gotta_catch_em_all():
    for poke_num in range(1,152):
        info = get_pokemon_info(poke_num) #saca la informacion de la id
        if info: 
            pokemon_name = info["name"]
            pokemon[pokemon_name] = {
                "id": info["id"],
                "altura": info["height"],
                "peso": info["weight"],
                "tipo_pokemon": [pokemon_type["type"]["name"] for pokemon_type in info["types"]]
            }
gotta_catch_em_all()
json_string = json.dumps(pokemon, indent=4)
print(json_string)
with open("datos_estructurados.json", "w") as f:
        json.dump(pokemon, f, indent=4)