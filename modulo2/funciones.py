# primero se define 
def saludar():
    print("Hola como estas")

# call , llama 
saludar()

def saludo():
    pass
    pass
    return "Hola saludando"

saludo()
variable = saludo()
print(variable)

def saludarPersona(nombre):
    print(f"Hola como estas , {nombre}")
""" 
name = input("ingrese un nombre")
saludarPersona(name) """

a=int(input("ingrese primer numer"))
b=int(input("ingrese segundo numer"))

def sumarNumero(numero1,numero2):
    return numero1+numero2

suma=sumarNumero(a,b)
print("la suma es ",suma)


