
def mostrar_triangulo(h:int):
    assert h>=1, 'Solo se permiten número enteros positivos'
    for f in range(h):
        print('#'* (f+1))

def ingresar_alumnos(cantidad_alumnos:int):

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
    return listado_alumnos
