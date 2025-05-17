import pandas as pd
import json
import numpy as np 
import time 
import os
print("Ingrese su nickname, este sera guardado para recoleccion de datos y lo podra seguir usando para futuro")
nombre = input("Nickname: ").lower() #por si ponen mayusculas no se genere otro nickname
archivo = open("datos_estructurados.json", "r") #accede al archivo 
datos = json.load(archivo) 
global_data = "global_data.csv"
Reintento=0
persona = {}

while Reintento==0:
    num = str(np.random.randint(1,151)) #Elije un pokemon del 1 al 151
    palabra = list((datos[num]["nombre"])) #saca su nombre
    cantidad = len(palabra) #cuenta la cantidad de letras 
    oculto = ["_"]*len(palabra) #oculta la palabra
    letras = list('abcdefghijklmnñopqrstuvwxyz-') #Para filtrar los caracteres validos
    descartes = [] #para contar las letras ya usadas
    invalido = 0
    totalInt = 0
    fallas = 0
    aciertos = 0

    print("""                       Bienvenidos la ahora Beta del Pokedle
                Aqui estan los datos del pokemon elegido por nuestro eficiente codigo""") 

    Intentos= 2+cantidad #Siento que algunos pokemon podria ser muy desbalanceado que  algunos tengan 12 intentos y otros 6, pero por algo es una beta :b
    def estado(): #Es el estado en el que esta el juego, checa la cantidad de intentos, las letras descartadas y la palabra oculta, con las letras que hayan sido ya adivinadas
        print(f"Intentos restantes: {Intentos}")
        print(f"Letras descartadas: {", ".join(descartes)}\n")
        print(f"Palabra: {" ".join(oculto)}\n")

    def letra_valida(letra): #Verifica que el caracter ingresado es una letra, también checa si la letra ya ha sido ingresada
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
    def gestion_letra(letra):  #Gestiona lo que te muestra la palabra, y cambia los "_" cuando aciertas a la letra 
        for i in range(cantidad):
            if palabra[i] == letra:
                oculto[i] = letra
                palabra[i] = "_"
    while Intentos>0 and "_" in oculto:
        #Finalmente, las pistas
        print("-"*cantidad)
        print("La entrada de la pokedex es: ", datos[num]["id"])
        print("El peso es: ", datos[num]["peso"])
        print("La altura es: ", datos[num]["altura"])
        print("El tipo es:", datos[num]["tipo_pokemon"])
        print("La cantidad de letras en su nombre son:", cantidad)
        estado() #Te dice el estado del juego
        letra = input("Introduzca una letra: ").lower() #En lowercase por si las dudas
        while not letra_valida(letra):
            letra = input("Introduzca otra letra: ").lower() #Por si la letra no fue valida

        if letra in palabra: #Checa si la letra ha sido acertada
            gestion_letra(letra)
            print("-"*50)
            print("Has acertado")
            totalInt = totalInt + 1
            aciertos = aciertos + 1
        else: #Checa si la leta ha sido errada
            print("-"*50)
            print("Has errado")
            descartes.append(letra)
            Intentos -= 1
            totalInt = totalInt + 1
            fallas = fallas + 1

    if "_" not in oculto: #Si adivinas todas las letras ya no deberia haber "_" entonces lo has logrado
        print("Felicidades haz adivinado el pokemon")
    else: #Pues has fallado :b
        print("No lo haz logrado")
    print("El pokemon era: ", (datos[num]["nombre"]))
    print("Tu total de intentos es: ", totalInt)
    print("Tu cantidad de fallas fueron: ", fallas)
    print("Tu cantidad de aciertos fueron: ", Intentos)
# Recoleccion de datos para posteriormente graficarlos
    if not os.path.exists(global_data):  #Si no existe el archivo lo crea
        df = pd.DataFrame(columns=["Nombre", "Fallas", "Aciertos"])  #Añade esto en la primera linea
    else: #si existe el archivo lo lee
        df = pd.read_csv(global_data) 
    if nombre in df["Nombre"].values: #Si el nombre existe añade los datos y los actualiza
        df.loc[df["Nombre"] == nombre, "Fallas"] += fallas
        df.loc[df["Nombre"] == nombre, "Aciertos"] += aciertos
        print("Datos actualizados")
    else: #Si no existe el nombre, añade al nuevo jugador
        nuevo = {"Nombre": nombre, "Fallas": fallas, "Aciertos": aciertos}
        df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
        print("Nuevo usuario agregado.")
    df.to_csv(global_data, index=False)
    print("¿Deseas intentar otro pokemon?(y/n)") 

    while invalido == 0: #Un ciclo por si quieres jugar otra vez
        invalido = 1
        respuesta=input(str("")).lower() #Si pones en mayusculas algo no romperas el codigo
        if respuesta == "n":
            Reintento = 1
            print("vuelva otra vez ")
        elif respuesta == "y":
            print("Entendido, iniciando otra vez")
            reintento = 0
        elif respuesta == "desintegrar": #????
            print("no esta chido cuando ven tu codigo, voa borrar tu cuenta")
            time.sleep(3)
            print("Jk, aunque tengo ese poder soy un ser benevolo, aun asi tendras que volver a iniciar :b")
            Reintento = 1
        else:
            print("Dijo algo invalido, escriba (y) si quiere seguir o (n) si no quiere seguir los parentesis son para remarcar") 
            invalido = 0
            Reintento = 1

