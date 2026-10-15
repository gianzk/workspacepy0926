ruta_archivo = 'archivo.txt' # ruta absoluta o ruta relativa


# Permite recuperar información de un archivo
# With permite cerrado automatico de archivo una vez terminada la sentencia
with open(ruta_archivo, mode='r') as file:
    # recupero data de archivo en variable
    data = file.read()
    pass



# Agregar contenido a archivo

with open(ruta_archivo, mode='a') as f:
    f.write('SE AÑADE NUEVO CONTENIDO')
