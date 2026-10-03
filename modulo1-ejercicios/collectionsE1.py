# registro de alumnos
dictAlumnos={
    'nombre':'',
    'dni':'',
    'cursos':[]
}

listaAlumnos=[]
print("bienvenido a Datux")

nombre= input("ingrese su nombre")
dni= input("ingrese su dni")
cursos= int(input("ingrese cantidad de cursos"))

dictAlumnos['nombre']=nombre
dictAlumnos['dni']=dni
dictAlumnos['cursos']=cursos

listaAlumnos.append(dictAlumnos)

print(listaAlumnos,len(listaAlumnos))

nombre= input("ingrese su nombre")
dni= input("ingrese su dni")
cursos= int(input("ingrese cantidad de cursos"))

dictAlumnos['nombre']=nombre
dictAlumnos['dni']=dni
dictAlumnos['cursos']=cursos

listaAlumnos.append(dictAlumnos)

print(listaAlumnos,len(listaAlumnos))