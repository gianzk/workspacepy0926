"""
Generacion del entregable.

El final del flujo: el archivo que recibe la otra area.
Ponle la fecha en el nombre para que el de hoy no pise el de ayer.
"""

import os
from datetime import date

from app.modelo.indicadores import _nivel, preparar

COLUMNAS_LEGIBLES = {
    "ruc": "RUC",
    "razon_social": "Razón social",
    "sector": "Sector",
    "departamento": "Departamento",
    "monto_otorgado": "Monto otorgado",
    "saldo_actual": "Saldo actual",
    "dias_atraso": "Días de atraso",
    "ventas_anuales": "Ventas anuales",
    "antiguedad_meses": "Antigüedad (meses)",
    "fecha_desembolso": "Fecha de desembolso",
}


def generar(registros, carpeta_output):
    """
    Escribe el archivo y devuelve (ruta, filas_escritas).

    Genera .xlsx; si openpyxl no esta instalado, genera .csv.
    """
    os.makedirs(carpeta_output, exist_ok=True)

    df = preparar(registros)
    df["nivel_riesgo"] = df["dias_atraso"].apply(_nivel)
    df = df.rename(columns=COLUMNAS_LEGIBLES)
    df = df.rename(columns={"nivel_riesgo": "Nivel de riesgo"})

    base = os.path.join(carpeta_output, "cartera_{}".format(date.today().isoformat()))
    try:
        ruta = base + ".xlsx"
        df.to_excel(ruta, index=False)
    except ImportError:
        ruta = base + ".csv"
        df.to_csv(ruta, index=False, encoding="utf-8-sig")  # tildes OK en Excel
    return ruta, len(df)
