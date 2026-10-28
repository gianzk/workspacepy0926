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
import pandas as pd
from app.modelo.entidades import Cliente
COLUMNAS_CLIENTE = [
    "ruc","razon_social","sector","departamento","monto_otorgado","saldo_actual","dias_atraso","ventas_anuales","antiguedad_meses","fecha_desembolso"
]

ESQUEMA = """
-- TODO: define tus tablas aqui
CREATE TABLE IF NOT EXISTS clientes(
    ruc TEXT PRIMARY KEY,
    razon_social TEXT NOT NULL,
    sector TEXT,
    departamento TEXT,
    monto_otorgado REAL,
    saldo_actual REAL,
    dias_atraso INTEGER,
    ventas_anuales REAL,
    antiguedad_meses INTEGER,
    fecha_desembolso TEXT
)
"""


class CargaDuplicada(Exception):
    """Se intento cargar el mismo archivo dos veces el mismo dia."""


class Repositorio:

    def __init__(self, ruta_bd):
        # TODO: crea la carpeta si no existe, conecta y ejecuta el esquema
        carpeta_ubicacion = os.path.dirname(ruta_bd)
        if carpeta_ubicacion and not os.path.exists(carpeta_ubicacion):
            os.makedirs(carpeta_ubicacion)
        self.ruta_bd=ruta_bd
        self.conexion = sqlite3.connect(ruta_bd)
        self.cursor = self.conexion.cursor()
        self.conexion.executescript(ESQUEMA)
        self.conexion.commit()


    def mapear_clientes(self,row):
        return Cliente(
            ruc = row["ruc"],
            razon_social=row["razon_social"],
            sector=row["sector"],
            departamento=row["departamento"],
            monto_otorgado=row["monto_otorgado"],
            saldo_actual=row["saldo_actual"],
            dias_atraso=row["dias_atraso"],
            ventas_anuales=row["ventas_anuales"],
            antiguedad_meses=row["antiguedad_meses"],
            fecha_desembolso=row["fecha_desembolso"]
        )


    def guardar_clientes(self,clientes:list):
        try:
            clientes_v2 = [self.mapear_clientes(c) for c in clientes]
            print(type(clientes_v2),clientes_v2[0])
            data = pd.DataFrame(
                [(
                    c.ruc,
                    c.razon_social,
                    c.sector,
                    c.departamento,
                    c.monto_otorgado,
                    c.saldo_actual,
                    c.dias_atraso,
                    c.ventas_anuales,
                    c.antiguedad_meses,
                    c.fecha_desembolso
                ) for c in clientes_v2] ,
                columns=COLUMNAS_CLIENTE)
            data.to_sql("clientes",self.conexion,if_exists="append",index=False)
            cantidad = len(data)
            self.conexion.commit()
            return cantidad
        except Exception as e:
            print("error en guardar cliente",e)

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
        self.conexion.close()
