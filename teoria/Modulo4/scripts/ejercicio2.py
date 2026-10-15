"""Calcular la altura de un triangulo del archivo 'trianguloimpreso.txt'"""


with open('trianguloimpreso.txt', mode='r') as f:
    content_list = f.readlines()

altura = len(content_list)
print(f'La altura del triangulo en el archivo es {altura}')