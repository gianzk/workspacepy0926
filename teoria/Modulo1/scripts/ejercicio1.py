"""
Calcular el área de un circulo. A partir de un radio 'r'
"""

import math

PI = 3.1416
radio = int(input('Ingresar radio del circulo: '))

# area_circulo = PI * radio ** 2

area_circulo = PI * math.pow(radio, 2)


# print(area_circulo)
print('El áre del circulo es' + str(area_circulo)) # no es eficiente
print('El áre del circulo es', area_circulo) # no es tan práctico

print(f'El área del circulo a partir de un radio {radio} es {area_circulo}')
print('El área del circulo a partir de un radio {} es {}'.format(radio, area_circulo))


