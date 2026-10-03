#formas de imprimir mensajes
a=10
b=12
msg="Hola mundo"
# 1: imprimir varias variables en una sola linea
print(a,b,msg)
#2 : mensaje compuesto
msgTotal="el numero es "+ str(a)+"y el mensaje es "+ msg
print("el numero es "+ str(a)+"y el mensaje es "+ msg)
#3: poner variables de forma explicita
print(f"el numero es {a} y tiene el valor de {b}")
#4: usar el format
print("el valor es {} con el mensaje {} y valor final {}".format(a,msg,b))

# ejemplo : imprima si un numero es mayor y la suma
print(f"{a} es mayor que {b}")
print(f"la suma de {a} y {b} es {a+b}")
