import re

def validar_email(email):
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(patron, email):
        return True
    return False

# Pruebas
#print(validar_email("ejemplo@correo.com"))  # True
#print(validar_email("correo-invalido"))       # False

email= input("ingrese un email: ")

if validar_email(email):
    print("es un email",email)
else:
    print("no es email")