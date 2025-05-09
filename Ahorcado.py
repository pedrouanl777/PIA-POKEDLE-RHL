import json
import numpy as np 
import statistics
print("Ingrese su nickname, este sera guardado para recoleccion de datos y lo podra seguir usando para futuro")
#nombre = input(str("Nickname: "))
archivo = open("datos_estructurados.json", "r")
datos = json.load(archivo)
num = str(np.random.randint(1,151))
palabra = list((datos[num]["nombre"]))
cantidad = len(palabra)
oculto = ['_']*len(palabra)
letras = list('abcdefghijklmnñopqrstuvwxyz')
descartes = []
print("""                       Bienvenidos al prototipo del Pokedle
            Aqui estan los datos del pokemon elegido por nuestro eficiente codigo""") #Por ahora funcionara como un ahorcado

Intentos= 4+cantidad

def estado():
    print(f"Intentos restantes: {Intentos}")
    print(f"Letras descartadas: {", ".join(descartes)}\n")
    print(f"Palabra: {" ".join(oculto)}\n")

def letra_valida(letra):
    if len(letra) != 1 :
        print("Has puesto más de una letra, inténtalo de nuevo")
        return False
    elif letra not in letras:
        print("No has introducido una letra del abecedario")
        return False
    elif letra in oculto:
        print("La letra introducida ya la has acertado")
        return False
    elif letra in descartes:
        print("Esa letra ya la has errado")
        return False
    else:
        return True
def gestion_letra(letra):
    for i in range(cantidad):
        if palabra[i] == letra:
            oculto[i] = letra
            palabra[i] = "_"
while Intentos>0 and "_" in oculto:
    
    print("-"*cantidad)
    print("La entrada de la pokedex es: ", datos[num]["id"])
    print("El peso es: ", datos[num]["peso"])
    print("La altura es: ", datos[num]["altura"])
    print("El tipo es:", datos[num]["tipo_pokemon"])
    print("La cantidad de letras en su nombre son:", cantidad)
    estado()
    letra = input("Introduzca una letra: ").lower()
    while not letra_valida(letra):
        letra = input("Introduzca otra letra: ").lower()

    if letra in palabra:
        gestion_letra(letra)
        print("-"*50)
        print("Has acertado")
    else:
        print("-"*50)
        print("Has fallado")
        descartes.append(letra)
        Intentos -= 1

if "_" not in oculto:
    print("Felicidades has acertado")
else:
    print("No lo has logrado")
print("El pokemon era: ", (datos[num]["nombre"]))