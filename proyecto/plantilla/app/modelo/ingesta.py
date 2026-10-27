"""
Lectura y validacion del archivo del dia.

Regla que no se negocia: una fila mala nunca tumba la carga.
Se rechaza, se anota el motivo y se sigue con la siguiente.
"""

import csv


def leer_csv(ruta):
    """
    TODO: devuelve (registros_validos, errores).

    Cada error debe decir en que fila ocurrio y por que.

    Pista de la estructura:

        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for numero, fila in enumerate(lector, start=2):
                try:
                    ...
                except ValueError as error:
                    errores.append({"fila": numero, "motivo": str(error)})
    """
    raise NotImplementedError


def quitar_duplicados(registros):
    """
    TODO: el CSV trae filas repetidas. Deja una sola por identificador.

    Devuelve (unicos, cantidad_descartada).
    """
    raise NotImplementedError
