# 1. Sobre el archivo archivo_modificado.txt
# añada los datos del tipo de cambio 202305


import requests 


URL_BASE = 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={anio}'


def get_tipo_cambio_mes(anio:str, mes:str):
    """Se cinecta a una URL para obtener el tipo de cambio de mes según sunat"""
    respuesta = requests.get(URL_BASE.format(anio=anio, mes=mes))
    data = respuesta.json()
    return data 


# 1. Recupero data de url
data = get_tipo_cambio_mes('2023', '5')


# 2. Empleo listas y cadenas para almacenar data según requiero
columnas = 'fecha,origen,moneda,compra,venta\n'

datos_filas = [columnas]
for registro in data:
    # recupero dato diccionario
    compra = registro['compra']
    venta = registro['venta']
    origen = registro['origen']
    moneda = registro['moneda']
    fecha = registro['fecha']

    # coloco datos en formato csv
    texto_fila = f'{fecha},{origen},{moneda},{compra},{venta}\n'
    # almaceno en cadena
    datos_filas.append(texto_fila)
    pass


# 3. Escribiendo con método writelines en escritura -> requiere un list
with open('datos_sunat.csv', mode='w') as f:
    f.writelines(datos_filas)

