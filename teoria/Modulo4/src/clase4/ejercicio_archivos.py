"""
Escribir un archivo que imprima el factorial de un número el cual debe tener el siguiente formato

nombre_archivo :  fact-n.txt > donde n es un número
contenido archivo: 5!= 120
"""


def factorial(n:int):

    fact = 1
    for i in range(1,n+1):
        fact = fact *i

    return fact


n = 5
x = factorial(n)

with open(f'fact-{n}.txt', 'w') as f:
    f.write(f'{n}! = {x}')



# Leer archivo

with open(f'fact-{n}.txt') as f:
    data = f.read()

print(data)