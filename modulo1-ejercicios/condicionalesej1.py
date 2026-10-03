# ejercicio1 : mediante una entrada de teclado determina si una persona puede ser un sufragante
# agregar cuantos años le falta para votar
edad = int(input("dime cuantos años tienes "))
if edad>=18:
    print("la persona puede votar")
else:
    print("la persona aun no puede votar")
    restante=18-edad
    print(f"te faltan {restante} años para poder votar")
