print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    
    opcion = input("ingresa un valor: ") # me devuelve un string ''
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
        continue
    print("programa ejecutable")

print("el blucle fue roto")