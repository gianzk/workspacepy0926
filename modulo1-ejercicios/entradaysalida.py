# entrada
#edad = input("dime cuantos años tienes ")# input es la funcion y dentro va el mensaje que quiero mostrar en la consola
#edad2 = input("dime cuantos años tienes ")
# el espacio si es un caracter que puedo hacer diferente 2 variables
#print(edad==edad2)
#print(edad,edad2)
# ejemplo 1 : muestra el año de nacimiento de una persona pidiendo su edad por consola ,considerar el año actual 2024
year_actual=2024
edad = input("dime cuantos años tienes ")
edadInt=int(edad)
year_nacimiento=year_actual-edadInt
print(year_nacimiento)
# forma corta
edad = int(input("dime cuantos años tienes "))
year_nacimiento=year_actual-edad
print(year_nacimiento)
