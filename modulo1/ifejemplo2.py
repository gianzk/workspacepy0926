# determine si un usuario puede ingresar al evento

usuario=input("ingrese su nombre")
edad = int(input("ingrese su edad"))
conAdulto = int(input("viene con adulto(1/0)"))
print("Bienvenido al evento, valide su informacion: ")

if edad >=18:
    print(usuario,"Puedes ingresar")
elif conAdulto:
    print("ingresa con adulto")
else:
    print(usuario,"no puedes ingresar al evento")

print("Fin de validacion")



