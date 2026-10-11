msg_welcome="""
    BIENVENIDO AL SISTEMA DATUX 2026
"""
print(msg_welcome)
sistema={
    'alumnos':[],
    'profesores':[],
    'cursos':[]
}
while True:
    print("Ingrese opciones")
    print("1.Registrar nuevo alumno")
    print("2.Registrar profesor")
    print("3.Registrar Curso")
    print("4.Eliminar elemento")
    print("5.Salir")
    # en python antes no se podia hacer switch case , 3.11 en adelante se puede 
    opcion = input("ingrese la opcion:")
    if opcion == '1':
        nombre=input("ingrese nombre de alumno")
        fdn=input("ingrese fdn de alumno")
        dni=input("ingrese dni de alumno")
        dic_alumno={
            'name':nombre,
            'fdn':fdn,
            'dni':dni
        }
        sistema['alumnos'].append(dic_alumno)
        print(sistema)
    elif opcion == '2':
        nombre=input("ingrese nombre de profesor: ") 
        dni=input("ingrese dni de profesor: ")
        # cuantos cursos usted maneja 
        cantidad_cursos = int(input("ingrese la cantidad de cursos: "))
        cursos_profesor= []
        for i in range(cantidad_cursos):
            cursos_temp=input(f"ingrese el curso {i+1}: ")
            cursos_profesor.append(cursos_temp)
        dic_profesor= {
            'name':nombre,
            'dni':dni,
            'cursos':cursos_profesor
        }
        sistema['profesores'].append(dic_profesor)
        print(sistema)
    elif opcion == '3':
        nombre = input("ingrese el nombre del curso:")
        vacantes = int(input("ingrese la cantidad de vacantes"))
        nota = input("ingrese la nota minima")
        dict_curso = {
            'name':nombre,
            'vacantes':vacantes,
            'nota_min': nota
        }
        sistema['cursos'].append(dict_curso)
    elif opcion == '4':
        dni=input("ingrese el dni") # un identificador
        lista_alumnos = sistema['alumnos']
        key_alumno = -1
        for i,value in enumerate(lista_alumnos):
            print(lista_alumnos) #  dic_alumno={'name':nombre,'fdn':fdn,'dni':dni}
            if dni == value['dni']:
                print("dni encontrado", dni)
                key_alumno = i
        if key_alumno == -1:
            print("dni no encontrado")
            continue
        #
        alumno_elimar = lista_alumnos[key_alumno]
        sistema['alumnos'].remove(alumno_elimar)
        print(sistema)
    elif opcion == '5':
        print("Hasta luego , gracias")
        break
    else:
        print("opcion no valida")
