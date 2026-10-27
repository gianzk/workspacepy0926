"""
Persistencia en SQLite.

Dos tablas como minimo:
  - la de tu entidad, con su identificador como PRIMARY KEY
  - una tabla de cargas, para saber que dia se cargo que archivo

La segunda es la que impide cargar dos veces el mismo dia.

Advertencia de rendimiento: NO pongas commit() dentro del bucle de
insercion. Con 50 000 filas se vuelve de cientos a miles de veces mas
lento. Usa executemany() y un solo commit al final.
"""

import os
import sqlite3

ESQUEMA = """
-- TODO: define tus tablas aqui
"""


class CargaDuplicada(Exception):
    """Se intento cargar el mismo archivo dos veces el mismo dia."""


class Repositorio:

    def __init__(self, ruta_bd):
        # TODO: crea la carpeta si no existe, conecta y ejecuta el esquema
        raise NotImplementedError

    def guardar(self, registros, forzar=False, archivo=""):
        """TODO: inserta con executemany() y un solo commit."""
        raise NotImplementedError

    def ya_se_cargo_hoy(self, archivo):
        """TODO: consulta la tabla de cargas."""
        raise NotImplementedError

    def registrar_carga(self, archivo, validos, rechazados):
        raise NotImplementedError

    def historial(self, limite=15):
        raise NotImplementedError

    def contar(self):
        raise NotImplementedError

    def listar(self):
        """TODO: devuelve la data como lista de diccionarios."""
        raise NotImplementedError

    def cerrar(self):
        raise NotImplementedError
