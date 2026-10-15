"""
Almacenar la información proveniente de mi API en una base de datos. Posterior a ello, leer los registros 
"""

import requests 
import sqlite3

URL_BASE = 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={anio}'


def get_tipo_cambio_mes(anio:str, mes:str)-> list:
    """Se cinecta a una URL para obtener el tipo de cambio de mes según sunat"""
    respuesta = requests.get(URL_BASE.format(anio=anio, mes=mes))
    data = respuesta.json()

    nuevo_listado = []
    for registro in data:
        x = tuple([ str(v) for k, v in registro.items()])
        nuevo_listado.append(x)

    return nuevo_listado


def main():

    # 1. Creacion de BD
    conexion = sqlite3.connect('public.db')
    cursor = conexion.cursor()

    # 2. Creo tabla sunat si no existe
    sentencia_create_table = open('creacion_tabla_sunat.sql').read()
    cursor.execute(sentencia_create_table)
    conexion.commit()

    # 3. Inserto registros en tabla
    datos_sunat = get_tipo_cambio_mes('2023', '1')
    cursor.executemany("INSERT INTO sunat VALUES (?,?,?,?,?)", datos_sunat)
    conexion.commit()

    # 4. Mostrar registros
    cursor.execute("SELECT * FROM sunat")
    valores_sunat = cursor.fetchall()

    # Ahora podemos recorrer todos los usuarios
    for usuario in valores_sunat:
        print(usuario)
    
    conexion.close()

if __name__ == '__main__':
    main()
