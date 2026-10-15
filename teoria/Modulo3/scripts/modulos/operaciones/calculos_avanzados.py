def factorial_recursivo(n:int)->int:
    """Calcula el factorial de un número n"""
    assert n>=0, 'NO se admiten números negativos'
    if n==0:
        return 1
    return n *  factorial_recursivo(n-1)
