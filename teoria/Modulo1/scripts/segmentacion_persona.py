"""A partir de la edad de una persona, segmentarla según los siguientes criterios:

0-5 infante
5-12 niño
12-16 pubertad
16-24 adolecente
24-40 adulto
40- adulto mayor
"""


edad = int(input('Ingrese su edad: '))


if edad >= 0 and edad < 5:
    print('Usted es un infante')
elif  edad >= 5 and edad < 12:
    print('Usted es un niño')
elif  edad >=12 and edad < 16:
    print('Usted es un pubertad')
elif  edad >= 16 :
    print('Usted adulto')
# else: # en cualquier otra casuhitica no contemplada
#     print('edad fuera de rango')
