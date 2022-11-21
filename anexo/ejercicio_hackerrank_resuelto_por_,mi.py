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

# Inicializo las variables:
lista_dicc = []
lista_listas = []

def fetch(page_number, location_id):
    response = requests.get("https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page="+str(page_number))
    data_json = response.json()
 

    for user in data_json["data"]:
        if user["location"]["id"] == location_id:
            lista_dicc.append({"userId":user["userId"], "amount":user["amount"]})

    return lista_dicc

def transform(dataset):   
    max = 0
    for user in dataset:
        if user["userId"] > max:
            max = user["userId"]
 
    for i in range(1, max+1):
        amount = 0
        lista_i = []
        for user in dataset:
            if user["userId"] == i:
                user_ID = i
                amount_i = float(re.sub(r'[^\d\-.]', '', user["amount"]))
                amount += amount_i
            lista_i = [i,amount] 

        if user_ID == i:
            lista_listas.append(lista_i)   

    return lista_listas


def report(data,page_number,location_id):

    X = [x[0] for x in data]
    Y = [y[1] for y in data]
    
    fig = plt.figure() 
    ax = fig.add_subplot()
    ax.bar(X,Y, color="tab:purple", label="N° usuario")
    ax.set_title("Gasto efectuado por cada usuario para el location id "+str(location_id)
    + " de la página N° "+str(page_number), fontsize = 10, weight = "bold")
    ax.set_ylabel(" Monto [$] ")
    ax.set_xlabel(" N° Usuario ")
    plt.xticks(X)
    plt.show() 

if __name__ == "__main__":

    print("Bienvenido a Voogle.SA!!")
    
    page_number = 1
    location_id = 7

    dataset = fetch(page_number,location_id)
    print("El dataset obtenido para el location id",location_id,"de la página N°",page_number,"es:")
    print(dataset)
    
    data = transform(dataset)
    print("En resumen, la lista con el numero de usario y lo que gastó cada uno en $ es:")
    print(data)

    print("Se muestra en una ventana emergente un gráfico de barras con el N° usuario vs Gasto $")
    time.sleep(12)
    report(data,page_number,location_id)

print("The End.")
