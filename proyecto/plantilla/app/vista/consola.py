"""
Capa de vista.

Este es el UNICO archivo donde pueden aparecer print(), input() y la
libreria de consola. Si aparecen en otra capa, el MVC esta roto.

La vista no calcula nada: recibe datos listos y los muestra.
"""


class SalidaSolicitada(Exception):
    """El usuario cerro la entrada con Ctrl+D (o Ctrl+Z en Windows)."""


def pedir_opcion():
    try:
        return input("  Opcion: ").strip()
    except EOFError:
        raise SalidaSolicitada()


def mostrar_menu():
    """TODO: el panel de control de tu herramienta."""
    print()
    print("  1. Cargar data del dia")
    print("  2. Ver indicadores")
    print("  3. Explorar la data")
    print("  4. Generar entregable")
    print("  5. Historial de cargas")
    print("  6. Salir")


def mensaje(texto):
    print("\n  {}".format(texto))


def advertencia(texto):
    print("\n  [!] {}".format(texto))


def error(texto):
    print("\n  [ERROR] {}".format(texto))


def mostrar_resultado_carga(resultado):
    """TODO: cuantas filas entraron, cuantas se rechazaron y por que."""
    raise NotImplementedError


def mostrar_indicadores(indicadores):
    """TODO: los indicadores de tu tematica."""
    raise NotImplementedError
