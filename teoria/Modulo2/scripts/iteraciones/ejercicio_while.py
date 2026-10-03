

OPCIONES_MENU = """
¿Qué quieres hacer? Escribe una opción
  1) Sumar
  2) Restar
  3) Multiplicar
  4) Salir
"""

print("Bienvenido al menú interactivo")
while True:
    opcion = input(OPCIONES_MENU).lstrip()

    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))

        suma = n1 + n2
        suma = round(suma, 0) # redondeando numero

        print(f"El resultado de la suma es: {suma}")
    elif opcion == '2':
        n1 = int(input("Introduce el primer número: ")) # int para tomar valor como entero
        n2 = int(input("Introduce el segundo número: "))
        print(f"El resultado de la resta es: {n1-n2}")
    elif opcion == '3':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))

        multiplicacion = n1 * n2

        print(f"El resultado de la multiplicacion es: {multiplicacion:.4f}")   # format string con redondeo a 4 decimales  
    elif opcion =='4':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")

