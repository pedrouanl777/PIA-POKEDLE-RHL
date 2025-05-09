import json
import numpy as np 
import statistics
import time 
print("Ingrese su nickname, este sera guardado para recoleccion de datos y lo podra seguir usando para futuro, solo recuerda donde pusiste mayusculas y minusculas")
#nombre = input(str("Nickname: "))
archivo = open("datos_estructurados.json", "r")
datos = json.load(archivo)
Reintento=0
while Reintento==0:
    num = str(np.random.randint(1,151))
    palabra = list((datos[num]["nombre"]))
    cantidad = len(palabra)
    oculto = ['_']*len(palabra)
    letras = list('abcdefghijklmnñopqrstuvwxyz')
    descartes = []
    invalido = 0
    totalInt = 0
    fallas = 0
    aciertos = 0

    print("""                       Bienvenidos al prototipo del Pokedle
                Aqui estan los datos del pokemon elegido por nuestro eficiente codigo""") #Por ahora funcionara como un ahorcado

    Intentos= 2+cantidad

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
            totalInt = totalInt + 1
            aciertos = aciertos + 1
        else:
            print("-"*50)
            print("Has fallado")
            descartes.append(letra)
            Intentos -= 1
            totalInt = totalInt + 1
            fallas = fallas + 1

    if "_" not in oculto:
        print("Felicidades haz adivinado el pokemon")
    else:
        print("No lo haz logrado")
    promaci = aciertos/totalInt
    promfal = fallas/totalInt
    print("El pokemon era: ", (datos[num]["nombre"]))
    print("Tu total de intentos es: ", totalInt)
    print("Tu promedio de fallas es: ", promfal)
    print("Tu promedio de aciertos es: ", promaci)
    print("¿Deseas intentar otro pokemon?(y/n)")
    while invalido == 0:
        invalido = 1
        respuesta=input(str("")).lower()
        if respuesta == "n":
            Reintento = 1
            print("vuelva otra vez ")
        elif respuesta == "y":
            print("Entendido, iniciando otra vez")
            reintento = 0
        elif respuesta == "desintegrar":
            print("no esta chido cuando ven tu codigo, voa borrar tu cuenta")
            time.sleep(3)
            print("Jk, aun no tengo ese poder, aun asi tendras que volver a iniciar :b")
            Reintento = 1
        else:
            print("Dijo algo invalido, escriba (y) si quiere seguir o (n) si no quiere seguir los parentesis son para remarcar")
            invalido = 0
            Reintento = 1
