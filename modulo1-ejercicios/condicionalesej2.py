# crea una calculadora de impuestos
print("calculadora de impuestos de renta")
nombre=input("ingrese su nombre")
salario=float(input("ingrese su salario"))
tax=0
if salario>=0 and salario<=10000:
    tax=5
elif salario>10000 and salario<=25000:
    tax=8
elif salario<=40000:
    tax=10
else:
    tax=15
# calculadora
impuesto_pagar=(salario*tax)/100
print(f"estimado {nombre} usted debe pagar en el año el impuesto de {impuesto_pagar}")