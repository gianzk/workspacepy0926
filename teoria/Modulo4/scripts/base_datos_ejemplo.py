import requests
import sqlite3

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2023'
response = requests.get(url)
content_list = response.json()

lista_guardar = ['compra;venta;origen;fecha\n']
listado_tuplas = []
for dicx in content_list:
    compra = dicx['compra']
    venta = dicx['venta']
    origen = dicx['origen']
    fecha = dicx['fecha']

    texto_linea = f'{compra};{venta};{origen};{fecha}\n'
    lista_guardar.append(texto_linea)
    listado_tuplas.append((compra, venta,origen, fecha ))


# almacenando en un csv

with open('data_api.csv', mode='w') as f:
    f.writelines(lista_guardar)


# almacenando en base datos
with sqlite3.connect('apis.db') as conexion:

    cursor = conexion.cursor()

    # creo tabla sql
    sentencia = open('create.sql').read()
    cursor.execute(sentencia)
    conexion.commit()


with sqlite3.connect('apis.db') as conexion:

    cursor = conexion.cursor()

    # creo tabla sql
    cursor.executemany("INSERT INTO tipo_cambio VALUES (?,?,?,?)", listado_tuplas)
    # Guardamos los cambios haciendo un commit
    conexion.commit()


