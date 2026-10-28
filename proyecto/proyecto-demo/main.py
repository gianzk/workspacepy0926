"""Punto de entrada. Arma la aplicacion y la arranca."""

import os

from app.controlador.app import Aplicacion
from app.vista.consola import SalidaSolicitada

CARPETA = os.path.dirname(os.path.abspath(__file__))

# TODO: cambia el nombre por el de tu archivo generado
RUTA_CSV = os.path.join(CARPETA, "data", "data_mipe.csv")
RUTA_BD = os.path.join(CARPETA, "data", "proyecto.db")
CARPETA_OUTPUT = os.path.join(CARPETA, "output")


def main():
    aplicacion = Aplicacion(RUTA_CSV, RUTA_BD, CARPETA_OUTPUT)
    try:
        aplicacion.ejecutar()
    except (KeyboardInterrupt, SalidaSolicitada):
        print("\n\n  Proceso interrumpido por el usuario.\n")


if __name__ == "__main__":
    main()
