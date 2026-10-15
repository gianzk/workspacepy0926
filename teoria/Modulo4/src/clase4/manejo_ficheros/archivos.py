"""
El manejo de ficheros o archivos me va a permitir realizar un 
con junto de acciones sobre estos como:
- Leer 
- Escribir


txt, csv
"""

# 1. Lectura
# -------------------------
#  Recupero informacion de archivo y con esta manipulo la data

# 1. Lectura

ruta_archivo = './archivo.txt'

with open(ruta_archivo, mode='r') as f:
    # extraer la data en una variable
    data = f.read()
    pass


# imprimo data
data_modificada = data.replace('2023', '2022')
print(data_modificada)



# 2. Escritura
# -----------------------------
ruta_archivo_escribir = 'archivo_modificado.txt'
with open(ruta_archivo_escribir, mode='w') as f:
    f.write(data_modificada)

