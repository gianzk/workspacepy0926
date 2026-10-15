contenido = """indice;nombre;apellido;fecha
1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006"""


with open('data.csv', mode='w', encoding='utf-8') as f:
    f.write(contenido)