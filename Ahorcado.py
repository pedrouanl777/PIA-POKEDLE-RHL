import json
import numpy as np 
import statistics

archivo = open("datos_estructurados.json", "r")
datos = json.load(archivo)
num = str(np.random.randint(1,151))
Palabra = datos[num]*len
print("""Bienvenidos al prototipo del Pokedle
            Aqui estan los datos del pokemon elegido por nuestro eficiente codigo""") #Por ahora funcionara como un ahorcado
print("La entrada de la pokedex es: ", num)
print("El peso es: ", datos[num]["peso"])
print("La altura es: ", datos[num]["altura"])
print("El tipo es:", datos[num]["tipo_pokemon"])
