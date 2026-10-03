#cadenas (str)
#concatenar
msg="Hola"
persona="Alumno"
msgTotal=msg+persona
msgTotalv2="Hola"+"Alumno"
msgTotalv3=msg +"Alumno"
print(msgTotal)
print(msgTotalv2)
print(msgTotalv3)
# errores
msg2="HI"
a=10
#msgTotalError=msg2+a
msgTotalErrorv2=msg2*a#si funciona !!
#print(msgTotalError)
#funcion de las cadenas(str)
# len => obtiene la cantidad de caracteres que tiene mi cadena
size=len(msgTotal)
print(size)
# transformar una variable a cadena
new_str=str(a)
print(type(new_str))
msgTotalFix=msg2+new_str
print(msgTotalFix)

#Numericas
c=2
d=7
#operaciones basicas
suma=c+d
resta=c-d
multiplicacion=c*d
exponencial=c**d
division_normal=d/c
division_entera=d//c
print(suma,resta,multiplicacion,exponencial,division_entera,division_normal)
# operacion modulo (%)
# es el resto de una division
# d%c => 7%2=> 7=2*3+1
# 157%3=157/3=3*52+1
resto=d%c
print(resto)
#convertir a un entero o a un flotante
strnumero='15'
print(type(strnumero))
e=int(strnumero)
print(type(e),e)
# en python se puedo hacer operaciones combinadas
f =(3 + 2 / (2*5))**2
print(f)

#operaciones booleanas

# cualquier número excepto el 0 se interpreta como verdadero
g=bool(20) 
h=bool(msg)
m=bool(0)
n=bool('')
print(type(g),type(h),g,h,m,n)

validMsg=(msgTotal==msgTotalv2)
numeroMayor=c>d
numeroMayorv2=c>=d
diferente= c!=d
print(validMsg)
print(numeroMayor)
print(numeroMayorv2)

#operacion combinada o compuesta
valorDeVerdad=(a>=0 and len(msgTotal)!=5) or(c<10 or msgTotal!="Hola")
print(valorDeVerdad)

#asignacion global
variableX=None







