# Registro notas
infoCurso1 = ("Datux Py","Gianmarco",2026)
print(infoCurso1)
print("Ingresa alumno")
listaAlumnos = []
alumno_name = input("Ingrese el nombre del alumno: ")
alumno_nota1 = input("Ingrese la nota1: ")
alumno_nota2 = input("Ingrese la nota2: ")
alumno_nota3 = input("Ingrese la nota3: ")

dict_alumno = {
    "name":alumno_name,
    "notas":[float(alumno_nota1),float(alumno_nota2),float(alumno_nota3)]
}
print(dict_alumno)
#pide otro alumno
listaAlumnos.append(dict_alumno)
print(listaAlumnos)
alumno_name = input("Ingrese el nombre del alumno: ")
alumno_nota1 = input("Ingrese la nota1: ")
alumno_nota2 = input("Ingrese la nota2: ")
alumno_nota3 = input("Ingrese la nota3: ")

dict_alumno = {
    "name":alumno_name,
    "notas":[float(alumno_nota1),float(alumno_nota2),float(alumno_nota3)]
}
print(dict_alumno)
listaAlumnos.append(dict_alumno)
print(listaAlumnos)

listaNotas=list(listaAlumnos[0]["notas"])
listaNotas.sort()
print(listaNotas)
