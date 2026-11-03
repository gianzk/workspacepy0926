"""
Calculo de indicadores con pandas.

Regla: el DataFrame NO sale de este archivo. Hacia afuera se devuelven
listas y diccionarios, para que la vista no sepa que pandas existe.
"""

import pandas as pd

from app.modelo.entidades import Cliente

NIVELES = ["NORMAL", "Revisando", "Problemas", "Perdido"]
SIN_DATO = "Sin dato"
LIMITE_MORA = 30  # mas de 30 dias de atraso = "Perdido"
TOP = 5


def _nivel(dias_atraso):
    """Reusa la regla de negocio de Cliente.nivel_riesgo()."""
    if pd.isna(dias_atraso):
        return SIN_DATO
    return Cliente(None, None, None, None, None, None, int(dias_atraso),
                   None, None, None).nivel_riesgo()


def preparar(registros):
    """DataFrame con los numericos convertidos; lo ilegible queda en NaN."""
    df = pd.DataFrame(registros)
    for col in ("monto_otorgado", "saldo_actual", "dias_atraso"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _top(df, columna):
    """Saldo por categoria, de mayor a menor, como lista de diccionarios."""
    agrupado = (
        df.groupby(columna)
        .agg(clientes=("ruc", "count"), saldo=("saldo_actual", "sum"))
        .sort_values("saldo", ascending=False)
        .head(TOP)
    )
    return [
        {"nombre": str(nombre), "clientes": int(fila["clientes"]),
         "saldo": float(fila["saldo"])}
        for nombre, fila in agrupado.iterrows()
    ]


def calcular(registros):
    """Devuelve un diccionario con los indicadores de la cartera."""
    if not registros:
        return {
            "total_clientes": 0,
            "monto_otorgado_total": 0.0,
            "saldo_total": 0.0,
            "cartera_en_mora": 0.0,
            "porcentaje_mora": 0.0,
            "sin_dato_riesgo": 0,
            "distribucion_riesgo": [
                {"nivel": n, "clientes": 0, "saldo": 0.0} for n in NIVELES
            ],
            "saldo_por_sector": [],
            "saldo_por_departamento": [],
        }

    df = preparar(registros)
    df["nivel"] = df["dias_atraso"].apply(_nivel)

    saldo_total = float(df["saldo_actual"].sum())
    en_mora = float(df.loc[df["dias_atraso"] > LIMITE_MORA, "saldo_actual"].sum())

    por_nivel = df.groupby("nivel").agg(
        clientes=("ruc", "count"), saldo=("saldo_actual", "sum")
    )
    distribucion = []
    for nivel in NIVELES:
        if nivel in por_nivel.index:
            fila = por_nivel.loc[nivel]
            distribucion.append({"nivel": nivel,
                                 "clientes": int(fila["clientes"]),
                                 "saldo": float(fila["saldo"])})
        else:
            distribucion.append({"nivel": nivel, "clientes": 0, "saldo": 0.0})

    return {
        "total_clientes": int(len(df)),
        "monto_otorgado_total": float(df["monto_otorgado"].sum()),
        "saldo_total": saldo_total,
        "cartera_en_mora": en_mora,
        "porcentaje_mora": round(en_mora / saldo_total * 100, 2) if saldo_total else 0.0,
        "sin_dato_riesgo": int((df["nivel"] == SIN_DATO).sum()),
        "distribucion_riesgo": distribucion,
        "saldo_por_sector": _top(df, "sector"),
        "saldo_por_departamento": _top(df, "departamento"),
    }
