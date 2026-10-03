# determine si un usuario puede ingresar al evento

usuario=input("ingrese su nombre")
edad = int(input("ingrese su edad"))
print("Bienvenido al evento, valide su informacion: ")

if edad >=18:
    print(usuario,"Puedes ingresar")
else:
    print(usuario,"no puedes ingresar al evento")

print("Fin de validacion")



