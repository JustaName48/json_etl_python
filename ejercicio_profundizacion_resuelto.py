# Ejercicio de Profundización: Hackerrank

# Autor ejercicio: Inove Coding School
# Autor resolución: Valentin Imperio
# Version: 1.0

# Importo librerías a utilizar:
import json
import requests
import matplotlib.pyplot as plt
import re
import time
import numpy as np

# Inicializo las variables:
deparment_info = []
lista_listas = []
list_min = []


def fetch():
    response = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50")
    data_json = response.json()

    for currency in data_json["results"]:
        if currency["currency_id"] == "ARS":
            deparment_info.append({"price":currency["price"], "condition":currency["condition"]})

    return deparment_info

def transform(dataset,min,max): 
    min_count = 0
    min_max_count = 0  
    max_count = 0

    list_min=[x for x in dataset if (x["price"]<min)]

    list_min_max=[x for x in dataset if (min<=x["price"]<=max)]

    list_max=[x for x in dataset if (max<x["price"])]

    min_count = len(list_min)
    min_max_count = len(list_min_max)
    max_count = len(list_max)

    return [min_count, min_max_count, max_count]
 

def report(data,min,max): 

    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return "{:.1f}%\n({:d} u)".format(pct, absolute)

    X = data
    Y = ["< $"+str(min),"$"+str(min)+"-"+str(max),"> $"+str(max)]
   
    # Creo mi paleta de colores: 
    colors = ["#7FFFD4","#13EAC9","#04D8B2"]
    fig = plt.figure() 
    fig.suptitle("Rango de Precios de Alquileres", fontsize = 16, weight = "bold")
    ax = fig.add_subplot()
    ax.pie(X, labels=Y, colors = colors, autopct=lambda pct: func(pct, data), wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'})
    ax.set_title("En Porcentaje [%] y Cantidad [u]", fontsize = 12)
    ax.axis("equal")
    plt.show()

if __name__ == "__main__":

    print("Bienvenido a Mercado Liebre! Su buscador predilecto!!")
    
    min = 5000
    max = 15000

    dataset = fetch()
    print("Se muestra la lista de alquileres con su precio en $ARS y su condición de uso: ")
    print(dataset)
    print("En resumen, la lista con la cantidad de alquileres según el rango ingresado es de: ")
    data = transform(dataset, min, max)
    print(data)
    print("Se muestra en una ventana emergente un gráfico de tortas con el Rango de Precios de Alquileres: ")
    time.sleep(6)
    report(data,min,max)


 
    

print("The End.")
