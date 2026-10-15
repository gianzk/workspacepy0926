"""Leer un archivo y cambiar la palbra 'caluroso' por 'frio', escribir el nuevo texto en otro archivo"""


ruta_archivo = 'archivo.txt' # ruta absoluta o ruta relativa


# Permite recuperar información de un archivo
# With permite cerrado automatico de archivo una vez terminada la sentencia
with open(ruta_archivo, mode='r') as file:
    # recupero data de archivo en variable
    data = file.read()
    pass


# empleo funciones de cadena para reemplazar contenido
new_data = data.replace('caluroso', 'frio')

# Escribiendo un nuevo archivo
with open('nuevo_archivo.txt', mode='w') as file:
    file.write(new_data)
