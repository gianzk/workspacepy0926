# sumar n numeros


# n = 100 => 100 +99 +98 .. .=> n*n+1/2

def sumar(n):
    if n != 1:
        return n+sumar(n-1)
    else :
        return 1

print(sumar(100))