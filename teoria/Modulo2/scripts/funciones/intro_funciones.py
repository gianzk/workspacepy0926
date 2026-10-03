"""
A partir de un número solicitado, validar si es primo o no lo es

Numero primo: Aquel número que es divisible entre el 1 y el mismo número

si un número tiene más de 2 divisores entonces no es primo
si un número tiene un divisor entre 1<x<n  no es primo
"""

# numero = int(input('Ingrese un número: '))

# es_primo = True
# for i in range(2,numero):
#     if numero % i ==0:
#         es_primo=False
#         break

# if es_primo:
#     print('El número ingresado es primo')
# else:
#     print('El número ingresado NO primo')



# Evaluar los números del 1 al 100 e indicar cuales son primos




# listado_numeros = [*range(1,101)]
# # Para cada número, evaluo si es primo o no
# for numero in listado_numeros:
#     # evaluo si es primo
#     es_primo = True
#     for i in range(2,numero):
#         if numero % i ==0:
#             es_primo=False
#             break
    
#     if es_primo:
#         print(numero)
#     pass


# Las funciones me ayudan a almacenar una lógica que es posible reutilizar

def evaluar_primo(x):
    es_primo = True
    for i in range(2,x):
        if x % i ==0:
            es_primo=False
            break
    return es_primo

listado_numeros = [*range(1,101)]
# Para cada número, evaluo si es primo o no
listado_primos = []

for numero in listado_numeros:
    # evaluo si es primo
    if evaluar_primo(numero):
        listado_primos.append(numero)
    pass

print(sorted(listado_primos, reverse=False))



