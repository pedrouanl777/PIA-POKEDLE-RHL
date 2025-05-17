import pandas as pd
import matplotlib.pyplot as plt
import os
from openpyxl import Workbook
from openpyxl.drawing.image import Image

global_data = "global_data.csv"
df = pd.read_csv(global_data)
if not os.path.exists('graficas'):
    os.makedirs('graficas')
promedio_fallas = df["Fallas"].mean()
promedio_aciertos = df["Aciertos"].mean()
def graficar_individual(nombre):
    usuario = df[df["Nombre"] == nombre].iloc[0]
    plt.figure(figsize=(6, 5))
    plt.bar(["Fallas", "Aciertos"], [usuario["Fallas"], usuario["Aciertos"]], color=["red", "green"])
    plt.title(f"Fallas y Aciertos: {nombre}")
    plt.xlabel("Tipo de Acción")
    plt.ylabel("Cantidad")
    plt.grid(True, linestyle="--", alpha=0.5)
    path = f"graficas/{nombre}_fallas_aciertos.png"
    plt.savefig(path)
    plt.close()
    return path

def graficar_promedios_usuario(nombre):
    usuario = df[df["Nombre"] == nombre].iloc[0]
    plt.figure(figsize=(6, 5))
    plt.pie([usuario["Fallas"], usuario["Aciertos"]],
            labels=["Fallas", "Aciertos"],
            autopct='%1.1f%%',
            colors=["red", "green"],
            startangle=90)
    plt.title(f"Promedio Fallas/Aciertos: {nombre}")
    path = f"graficas/{nombre}_promedios.png"
    plt.savefig(path)
    plt.close()
    return path

def graficar_global():
    total_fallas = df["Fallas"].sum()
    total_aciertos = df["Aciertos"].sum()
    plt.figure(figsize=(6, 5))
    plt.barh(["Fallas", "Aciertos"], [total_fallas, total_aciertos], color=["red", "green"])
    plt.title("Fallas y Aciertos Globales")
    plt.xlabel("Cantidad")
    plt.grid(True, linestyle="--", alpha=0.5)
    path = "graficas/global_fallas_aciertos.png"
    plt.savefig(path)
    plt.close()
    return path

def graficar_promedios_global():
    plt.figure(figsize=(6, 5))
    plt.pie([promedio_fallas, promedio_aciertos],
            labels=["Promedio de Fallas", "Promedio de Aciertos"],
            autopct='%1.1f%%',
            colors=["red", "green"],
            startangle=90)
    plt.title("Promedios Globales de Fallas y Aciertos")
    path = "graficas/global_promedios.png"
    plt.savefig(path)
    plt.close()
    return path

def guardar_en_excel(imagenes):
    wb = Workbook()
    ws = wb.active
    ws.title = "Gráficas"
    fila = 4
    for img_path in imagenes:
        img = Image(img_path)
        img.width, img.height = 400, 300
        ws.add_image(img, f"A{fila}")
        fila += 20  

    wb.save("graficas/graph_data.xlsx")
    print("Excel con gráficas guardado en 'graficas/graph_data.xlsx'.")


imagenes_total = []

for nombre in df["Nombre"]:
    imagenes_total.append(graficar_individual(nombre))
    imagenes_total.append(graficar_promedios_usuario(nombre))

imagenes_total.append(graficar_global())
imagenes_total.append(graficar_promedios_global())

guardar_en_excel(imagenes_total)
