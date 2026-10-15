"""Genere un archivo el cual tenga como contenido la figura de un triangulo de altura h"""

altura=int(input('Ingresar la altura del triangulo: '))


content = ''
for i in range(1,altura+1):
    imprimir_triangulo="#"*i
    content += "{}\n".format(imprimir_triangulo)
content = content.strip()

print(content)

with open('trianguloimpreso.txt',mode='w') as file:
    file.write(content)


