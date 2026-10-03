lista_reserva=[]
nombre= input("ingrese su nombre: ")
telefono= input("ingrese su telefono: ")
dni= input("ingrese su dni: ")

ltmp=[nombre,telefono,dni]
lista_reserva.append(ltmp)

blacklist=['79797979','123456']

if lista_reserva[0][2] in blacklist:
    print("este dni esta blockeado")
    lista_reserva[0][2]='dniblockeado'
else: 
    print("no esta en nuestra lista negra")

print(lista_reserva)