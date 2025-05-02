import requests
import random #importar random para no solo limitar la cantidad de pokemon, si no tambien que se elija un pokemon aleatorio cada que se active el modulo
base_url = "https://pokeapi.co/api/v2/"
x=0
pokemon = {}
while x < 2:
    def get_pokemon_info(id): #Una funcion para usar después 
        url = f"{base_url}/pokemon/{id}" #Esto para que podamos cambiar la url a lo que necesitamos, una url que puede cambiar la id
        response = requests.get(url)

        if response.status_code == 200: #Esto es por si la URL esta caida o tiene problemas no tire directamente error
            pokemon_data = response.json()
            return pokemon_data
        else:
            print(f"Fallo al recuperar la información {response.status_code}") #Aqui terminaria el programa si no logra conectar con la URL 
    x = x+1 #elige un numero del 1 al 151
    pokemon_id = x #lo graba en la id
    pokemon_info = get_pokemon_info(pokemon_id) #saca la informacion de la id
    y = f"Nombre: {pokemon_info["name"].capitalize()}"
    if pokemon_info: #Ando pensando en quitar este if, pero no estoy seguro 
        Tipos = [typ["type"]["name"] for typ in pokemon_info["types"]] #este tuvo que ser diferente, porque al haber 2 instancias de "Types" soltaba error
        pokemon.update({y: "id: " f"{pokemon_info["id"]}, " "altura: " f"{pokemon_info["height"]}" "m, " "Peso: " f"{pokemon_info["weight"]}" "Kg, " "Pokemon de tipo: "})
print (pokemon)