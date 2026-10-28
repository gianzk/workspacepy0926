"""
Calculo de indicadores con pandas.

Regla: el DataFrame NO sale de este archivo. Hacia afuera se devuelven
listas y diccionarios, para que la vista no sepa que pandas existe.

Revisa TEMATICAS.md: ahi estan los indicadores minimos de tu tema.
"""

import pandas as pd


def calcular(registros):
    """
    TODO: devuelve un diccionario con los indicadores de tu tematica.

    Pista: pd.DataFrame(registros) y de ahi groupby().agg().
    Devuelve numeros de Python (int(), float()), no tipos de numpy.
    """
    raise NotImplementedError
