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

texto_unificado = ''  # se emplea para paso 3
lista_lineas = []  # se emplea para paso 4
for registro in data:
    data_fecha = registro['fecha']
    precio_compra = registro['compra']

    x = f'====={data_fecha}=====\n'
    y = f'{precio_compra}\n'


    # consolido texto paso 3
    texto_unificado = texto_unificado+ x+y

    # incremento listado paso 4
    lista_lineas.append(x)
    lista_lineas.append(y)
    pass

# 3. Escribiendo con método write en escritura -> requiere un str
with open('nuevo_archivo.txt', mode='w') as f:
    f.write(texto_unificado)

# 4. Escribiendo con método writelines en escritura -> requiere un iterable

with open('nuevo_archivo2.txt', mode='w') as f:
    f.writelines(lista_lineas)

