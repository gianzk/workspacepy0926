"""Los bucles WHILE permiten repetir una tarea mientras la condición establecida sea VERDADERA"""



# Mientras la hora sea entre las 9 y 1 estaré viendo mi curso de python

# hora = int(input('ingrese la hora: '))

# while hora >=9 and hora <=13:
#     print('Estoy estudiando python')

#     # Vuelvo a consultar por la hora
#     hora = int(input('ingrese la hora: '))

# print('Termino el bucle')



# Mientras este lloviendo, jugaré en casa

esta_lloviendo = True

while esta_lloviendo:
    print('Estoy jugando en casa porque esta lloviendo')

    esta_lloviendo = bool(int(input('sigue lloviendo ?')))

print('Dejo de llover')