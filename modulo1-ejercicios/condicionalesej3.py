msg="""
    1.dese sumar los numeros
    2.desea multiplicar los numeros
    3.desea la resta de los numeros
"""
print(msg)
a=int(input("ingrese un numero "))
b=int(input("ingrese un numero "))
opcion=int(input("ingresa una opcion"))
if opcion==1:
    print(a+b)
elif opcion==2:
    print(a*b)
elif opcion==3:
    print(a-b)
else:
    print("ingrese una opcion valida")