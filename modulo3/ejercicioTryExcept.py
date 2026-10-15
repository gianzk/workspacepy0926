# error 1
elementos=[1,2,3,4]
tuplas = (1,2,3,4)

#print(f"mostrar ultimo elemento {elementos[100]}")
#tuplas[1]=2

try:
    tuplas[1]=2
except  Exception as e:
    print("describir el error",e)
