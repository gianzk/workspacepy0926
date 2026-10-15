#Proyecto de finanzas 

#Menu 
#riesgo 

# funcion calculointeres
def calculoInteresv2(i=5):
    c=float(input("ingresa el capital: "))
    i = riskInteres(i)
    t=float(input("ingresa el tiempo:"))
    interes = (c*i*t)/100
    #print(interes)
    return interes
def procesoPrestamo():
    print("......iniciando proceso......")
    confirmacion = input("ingresa si acepto(S) si confirma el prestamo")
    if confirmacion.upper()=='S':
        print("prestamo entregado")
    pass
#titulo
def riskInteres(i):
    risk=float(input("ingrese el riesgo del cliente:"))
    if risk>=0.5:
        return i+2
    

print("Bienvenido al sistema")
while True:
    
    msg = """
        1.Ingresar usuario
        2.Calcular interes
        3.Calcular interes compuesto
        4.Salir
    """
    print(msg)
    opcion = input("ingrese una opcion: ")

    if opcion.isdigit():
        # que es anidado ?
        # es dentro de una estructura poner otra estructura
        #opcionParseado = int(opcion)
        opcion = int(opcion) # reasignar 
        if opcion==1:
            pass
        elif opcion==2:
            cInteres=calculoInteresv2()
            acepta=input(f"Desea continuar con el prestamo de $/{cInteres}(S/N)")
            if acepta.upper()=="S":
                procesoPrestamo()
            else:
                continue
        elif opcion==3:
            calculoInteresv2()
        elif opcion==4:
            break
        else:
            print("esa opcion no existe")
        
    else:
        print("Ingresa una opcion numerica")



    
