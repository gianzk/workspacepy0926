"""Realizar un programa menu"""
from pprint import pprint

# import <nombre_archivo.py> as ing
import ingreso_datos as ing

# import <nombre_carpeta> import <nombre_archivo.py>
from operaciones import calculos_basicos, calculos_avanzados
from otros import operacion

MENSAJE_BIENVENIDA = 'Bienvenido al menú iteractivo'
OPCIONES_MENU = """
¿Qué quieres hacer?
  1)Sumar dos números
  2)Calcular el factorial de un número
  3)Ingresar el listado de alumnos
  4)Mostrar un triangulo
  5)Salir

Ingrese su opción: 
"""


def opcion_1():
    print('----Suma de 2 números----')
    n1= ing.ingreso_numero_decimal('Ingrese el primer número: ')  
    n2= ing.ingreso_numero_decimal('Ingrese el segundo número: ')

    sumatoria = calculos_basicos.calcular_suma(n1, n2)

    print('La suma de {} y {} es {}'.format(n1,n2,sumatoria))

def opcion_2():
    print('----Calcular el factorial de un número----')

    n= ing.ingreso_numero_entero()
    resultado2=  calculos_avanzados.factorial_recursivo(n)
    print('{}! = {}'. format(n,resultado2))

def opcion_3():
    print('----Ingresar el listado de alumnos----')
    cantidad_alumnos = ing.ingreso_numero_entero('Ingrese la cantidad de alumnos a registrar: ')
    listado_alumnos = operacion.ingresar_alumnos(cantidad_alumnos)

    print('Inprimiendo listado final de alumnos ...')
    pprint(listado_alumnos)

def opcion_4():
    print('----Mostrar un triángulo----')
    h = ing.ingreso_numero_entero('Ingrese la altura del triangulo: ')
    operacion.mostrar_triangulo(h)

# main
def main():

    print(MENSAJE_BIENVENIDA)
    while True:
        opcion=input(OPCIONES_MENU)
        if opcion =='1':
            opcion_1()      
        elif opcion =='2':
            opcion_2()
        elif opcion=='3':
            opcion_3()
        elif opcion=='4':
            opcion_4()
        elif opcion=='5':
            print('Hasta luego')
            break

# Programa principal
if __name__ == '__main__':
    main()