

def ingreso_numero_entero(msg:str = 'Ingrese un número entero: ')->int:
    """Solicita al usuario el ingreso de un número entero"""

    try:
        numero = int(input(msg))
    except:
        print('No se ingreso un número entero')
        return ingreso_numero_entero(msg)
    return numero

def ingreso_numero_decimal(msg:str = 'Ingrese un número decimal: ')->float:
    """Solicita al usuario el ingreso de un número decimal"""

    try:
        numero = float(input(msg))
    except:
        print('No se ingreso un número entero')
        return ingreso_numero_decimal(msg)
    return numero


if __name__ == '__main__':
    ingreso_numero_entero()