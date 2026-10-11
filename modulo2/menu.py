
dato1=input("ingrese un valor")
dato2=input("ingrese un valor")
while True:

    opcion = int(input("opcion 1 : mostrar, opcion 2 : mostrar mensaje 2 , opcion 3: "))
    if opcion==1:
        print("el mensaje es",dato1)
    elif opcion == 2:
        print("el mensaje es",dato2)
    elif opcion==3:
        print("saludos,hasta luego")
        break
    else:
        print("no hay opcion valida")

