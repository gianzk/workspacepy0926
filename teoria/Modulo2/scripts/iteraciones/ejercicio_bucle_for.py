""" 
1. Relizar un listado de n alumnos donde se ingresen 3 notas 
 por cada alumno en el listado
"""
from pprint import pprint

# 1.Consulto el usuario la cantidad de alumnos a ingresar
cantidad_alumnos = int(input('Ingrese la cantidad de alumnos a registrar: '))

# 2. Generando el listado de alumnos
listado_alumnos = []

for i in range(cantidad_alumnos):
    print(f'----- Registrando al alumno {i+1} -----')
    alumno = {}
    alumno['nombre'] = input('Ingrese nombre del alumno: ')
    alumno['apellido'] = input('Ingrese apellido del alumno: ')

    notas = []
    for j in range(3):
        nota = int(input(f'Ingrese nota {j+1}: '))
        notas.append(nota)
    alumno['notas'] = notas
    alumno['prom_notas'] = sum(notas) /3

    # añado dicx a lista
    listado_alumnos.append(alumno)


print('Inprimiendo listado final de alumnos ...')
pprint(listado_alumnos)

# Calcular el promedio final de la clase (Suma de los promedios de cada alumno entre el numero de alumnos)

suma_promedios = 0
for alumno in listado_alumnos:
    suma_promedios += alumno['prom_notas']

print(f'El promedio de notas de la clase es: {suma_promedios /len(listado_alumnos)}')











# Estructura para 1 alumno
# alumno = {
    # codigo_alumno = 'xxxxxxs45'
#     'nombre': 'Gonzalo',
#     'apellido': 'Delgado',
#     'notas': [12,14,15],
#     'prom_final': alumno[notas][0] + alumno[notas][1] + alumno[notas][2]  /3
# }

# notas = {
#     'xxxxxxs45' = []
# }



# input('Ingrese nota1: ')
# input('Ingrese nota2: ')
# input('Ingrese nota2: ')

# notas = []

# for i in range(3):
#     nota = input(f'Ingrese nota {i+1}: ')
#     notas.append(nota)