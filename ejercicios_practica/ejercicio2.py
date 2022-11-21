# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    
    # Inicialización de variables:
    titulos_completados = []
    nombre_usuarios = []
    j = 1
    max = 0
    completos = 0

    # Aclaración: Se podría obviar el calculo del usuario máximo y en la línea 59 usar 10
    # en vez de la variable max, pero de esta forma se puede ejecutar el programa sin tener
    # que saber la cantidad máxima de usuarios.

    for user in data:
        if user["userId"] > max:
            max = user["userId"] 

    for i in range(1, max+1):
        for user in data:
            if user["userId"] == i:
                if user["completed"] == True:
                    completos += 1
        
        titulos_completados.append(completos)  
        completos = 0
    
    print(titulos_completados)
   

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    for i in range(1, max+1):
        for user in data:
            if user["userId"] == j:
                nombre_usuarios.append(j)
                j += 1

    fig = plt.figure() 

    ax = fig.add_subplot()
    ax.bar(nombre_usuarios,titulos_completados, color="tab:purple", label="N° usuario")
    ax.set_title("Titulos Completados")
    ax.set_ylabel(" Titulos ")
    ax.set_xlabel(" Usuarios ")
    ax.legend()
    plt.xticks(nombre_usuarios)
    plt.show() 

print("terminamos")