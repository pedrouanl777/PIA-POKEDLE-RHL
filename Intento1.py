import pandas as pd
import os

# Nombre del archivo CSV
archivo_csv = "datos.csv"

# Pedir datos
nickname = input("Ingresa tu nickname: ")
valor1 = int(input("Ingresa el valor 1: "))
valor2 = int(input("Ingresa el valor 2: "))

# Si el archivo no existe, creamos el DataFrame vacío
if not os.path.exists(archivo_csv):
    df = pd.DataFrame(columns=["nickname", "valor1", "valor2"])
else:
    df = pd.read_csv(archivo_csv)

# Verificar si el nickname ya existe
if nickname in df["nickname"].values:
    # Sumar a los valores existentes
    df.loc[df["nickname"] == nickname, "valor1"] += valor1
    df.loc[df["nickname"] == nickname, "valor2"] += valor2
    print("Datos actualizados sumando a los anteriores.")
else:
    # Agregar nueva fila (usando concat en lugar de append)
    nuevo = {"nickname": nickname, "valor1": valor1, "valor2": valor2}
    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    print("Nuevo usuario agregado.")

# Guardar el CSV actualizado
df.to_csv(archivo_csv, index=False)
print("✅ Archivo CSV actualizado.")
