"""
Generador de data sintetica para el proyecto final del curso.

Crea archivos CSV de gran volumen para cualquiera de las tematicas
disponibles. La data es completamente ficticia: ninguna empresa, cliente
u operacion aqui generada corresponde a la realidad.

Por defecto el archivo sale "sucio" a proposito (campos vacios, fechas en
formatos distintos, numeros con coma, filas duplicadas). Eso es
intencional: el proyecto debe validar la data, no confiar en ella.

Uso:
    python generar_datos.py --listar
    python generar_datos.py mipe
    python generar_datos.py mipe --filas 100000 --output cartera.csv
    python generar_datos.py hipotecas --limpio

Requiere:  pip install faker
"""

import argparse
import csv
import random
import sys
from datetime import date, timedelta

try:
    from faker import Faker
except ImportError:
    print("Falta la libreria faker.")
    print("Instalala con:  pip install faker")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Catalogos
# ---------------------------------------------------------------------------

SECTORES = ["Comercio", "Servicios", "Manufactura", "Construccion",
            "Transporte", "Agropecuario", "Restaurantes", "Textil"]

DEPARTAMENTOS = ["Lima", "Arequipa", "La Libertad", "Piura", "Cusco",
                 "Lambayeque", "Junin", "Ancash", "Ica", "Loreto"]

ZONAS = ["Norte", "Sur", "Centro", "Este", "Oeste"]

CATEGORIAS = ["Abarrotes", "Bebidas", "Limpieza", "Cuidado personal",
              "Lacteos", "Snacks", "Congelados", "Bazar"]

PLANES = ["Basico", "Estandar", "Premium", "Corporativo"]

CONTRATOS = ["Indefinido", "Plazo fijo", "Independiente", "Recibo por honorarios"]

AREAS = ["Ventas", "Operaciones", "Logistica", "Administracion",
         "Sistemas", "Atencion al cliente", "Almacen"]

TIPOS_SEGURO = ["Vehicular", "Hogar", "Salud", "Vida", "Accidentes"]

CANALES = ["Telefono", "Correo", "Mensajeria", "Visita"]


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def ruc(rng):
    """RUC ficticio de persona juridica."""
    return "20" + "".join(str(rng.randint(0, 9)) for _ in range(9))


def dni(rng):
    """DNI ficticio."""
    return "".join(str(rng.randint(0, 9)) for _ in range(8))


def placa(rng):
    letras = "".join(rng.choice("ABCDEFGHIJKLMNPQRSTUVWXYZ") for _ in range(3))
    return letras + "-" + str(rng.randint(100, 999))


def fecha_entre(rng, dias_atras_max, dias_atras_min=0):
    """Fecha aleatoria dentro de una ventana hacia atras desde hoy."""
    dias = rng.randint(dias_atras_min, dias_atras_max)
    return date.today() - timedelta(days=dias)


def fecha_txt(f, rng, sucio):
    """Convierte una fecha a texto. Si hay suciedad, a veces cambia el formato."""
    if sucio and rng.random() < 0.05:
        return f.strftime("%d/%m/%Y")
    return f.strftime("%Y-%m-%d")


def num_txt(valor, rng, sucio, decimales=2):
    """Convierte un numero a texto. Si hay suciedad, a veces usa coma decimal."""
    texto = "{:.{d}f}".format(valor, d=decimales)
    if sucio and rng.random() < 0.04:
        return texto.replace(".", ",")
    return texto


def ensuciar(fila, rng):
    """Vacia un campo al azar o altera el formato de un texto."""
    claves = list(fila.keys())
    azar = rng.random()
    if azar < 0.03:
        fila[rng.choice(claves)] = ""
    elif azar < 0.05:
        clave = rng.choice(claves)
        valor = fila[clave]
        if isinstance(valor, str) and valor:
            fila[clave] = valor.upper() if rng.random() < 0.5 else "  " + valor + " "
    return fila


# ---------------------------------------------------------------------------
# Generadores por tematica
# ---------------------------------------------------------------------------

def tema_mipe(fake, rng, i, sucio):
    """1. Riesgo crediticio de cartera MIPE."""
    monto = rng.uniform(3000, 150000)
    saldo = monto * rng.uniform(0.15, 1.0)
    atraso = rng.choices([0, rng.randint(1, 8), rng.randint(9, 30),
                          rng.randint(31, 60), rng.randint(61, 120),
                          rng.randint(121, 400)],
                         weights=[55, 15, 12, 8, 6, 4])[0]
    return {
        "ruc": ruc(rng),
        "razon_social": fake.company(),
        "sector": rng.choice(SECTORES),
        "departamento": rng.choice(DEPARTAMENTOS),
        "monto_otorgado": num_txt(monto, rng, sucio),
        "saldo_actual": num_txt(saldo, rng, sucio),
        "dias_atraso": str(atraso),
        "ventas_anuales": num_txt(rng.uniform(20000, 2500000), rng, sucio),
        "antiguedad_meses": str(rng.randint(3, 240)),
        "fecha_desembolso": fecha_txt(fecha_entre(rng, 1095, 30), rng, sucio),
    }


def tema_hipotecas(fake, rng, i, sucio):
    """2. Evaluacion de solicitudes hipotecarias."""
    ingreso = rng.uniform(1500, 25000)
    valor = rng.uniform(80000, 900000)
    inicial = valor * rng.uniform(0.05, 0.45)
    return {
        "id_solicitud": "SOL-{:07d}".format(i),
        "dni": dni(rng),
        "solicitante": fake.name(),
        "ingreso_mensual": num_txt(ingreso, rng, sucio),
        "deudas_mensuales": num_txt(ingreso * rng.uniform(0.0, 0.6), rng, sucio),
        "valor_inmueble": num_txt(valor, rng, sucio),
        "cuota_inicial": num_txt(inicial, rng, sucio),
        "plazo_anios": str(rng.choice([5, 10, 15, 20, 25, 30])),
        "tipo_contrato": rng.choice(CONTRATOS),
        "dependientes": str(rng.randint(0, 5)),
        "fecha_solicitud": fecha_txt(fecha_entre(rng, 365), rng, sucio),
    }


def tema_cobranzas(fake, rng, i, sucio):
    """3. Gestion de mora y cobranzas."""
    vencimiento = fecha_entre(rng, 180, 1)
    pagada = rng.random() < 0.35
    fecha_pago = ""
    if pagada:
        dias = rng.randint(0, 45)
        pago = vencimiento + timedelta(days=dias)
        if pago <= date.today():
            fecha_pago = fecha_txt(pago, rng, sucio)
    return {
        "id_operacion": "OP-{:08d}".format(i),
        "documento_cliente": dni(rng),
        "cliente": fake.name(),
        "monto_cuota": num_txt(rng.uniform(80, 4500), rng, sucio),
        "fecha_vencimiento": fecha_txt(vencimiento, rng, sucio),
        "fecha_pago": fecha_pago,
        "canal_preferido": rng.choice(CANALES),
        "gestiones_previas": str(rng.randint(0, 12)),
        "promesa_incumplida": rng.choice(["SI", "NO", "NO", "NO"]),
    }


def tema_inventario(fake, rng, i, sucio):
    """4. Rotacion y quiebre de stock."""
    costo = rng.uniform(1.5, 180)
    minimo = rng.randint(5, 80)
    return {
        "codigo_producto": "P{:06d}".format(rng.randint(1, 4000)),
        "categoria": rng.choice(CATEGORIAS),
        "local": "Local {:02d}".format(rng.randint(1, 25)),
        "stock_actual": str(rng.randint(0, 400)),
        "stock_minimo": str(minimo),
        "unidades_vendidas_mes": str(rng.randint(0, 600)),
        "costo_unitario": num_txt(costo, rng, sucio),
        "precio_venta": num_txt(costo * rng.uniform(1.1, 2.4), rng, sucio),
        "fecha_ultimo_ingreso": fecha_txt(fecha_entre(rng, 240), rng, sucio),
    }


def tema_suscripciones(fake, rng, i, sucio):
    """5. Fuga de clientes en servicios por suscripcion."""
    promedio = rng.uniform(5, 300)
    return {
        "id_cliente": "C{:08d}".format(i),
        "plan": rng.choice(PLANES),
        "meses_permanencia": str(rng.randint(1, 96)),
        "consumo_ultimo_mes": num_txt(promedio * rng.uniform(0.0, 1.6), rng, sucio),
        "consumo_promedio": num_txt(promedio, rng, sucio),
        "reclamos": str(rng.choices([0, 1, 2, 3, 5, 8],
                                    weights=[55, 20, 12, 7, 4, 2])[0]),
        "pagos_atrasados": str(rng.choices([0, 1, 2, 4],
                                           weights=[62, 22, 11, 5])[0]),
        "monto_mensual": num_txt(rng.uniform(25, 450), rng, sucio),
        "fecha_alta": fecha_txt(fecha_entre(rng, 2900, 30), rng, sucio),
    }


def tema_flota(fake, rng, i, sucio):
    """6. Costos y eficiencia de flota de reparto."""
    km = rng.uniform(20, 420)
    rendimiento = rng.uniform(5, 14)
    programadas = rng.randint(8, 60)
    salida = rng.randint(5, 10)
    return {
        "id_viaje": "V-{:08d}".format(i),
        "placa": placa(rng),
        "ruta": "Ruta {:02d}".format(rng.randint(1, 40)),
        "zona": rng.choice(ZONAS),
        "kilometros": num_txt(km, rng, sucio, 1),
        "combustible_galones": num_txt(km / rendimiento, rng, sucio, 2),
        "entregas_programadas": str(programadas),
        "entregas_efectivas": str(max(0, programadas - rng.randint(0, 12))),
        "hora_salida": "{:02d}:{:02d}".format(salida, rng.randint(0, 59)),
        "hora_retorno": "{:02d}:{:02d}".format(min(23, salida + rng.randint(4, 12)),
                                               rng.randint(0, 59)),
        "peajes": num_txt(rng.uniform(0, 85), rng, sucio),
        "fecha_viaje": fecha_txt(fecha_entre(rng, 365), rng, sucio),
    }


def tema_personal(fake, rng, i, sucio):
    """7. Productividad y ausentismo de personal."""
    programadas = rng.choice([160, 176, 184, 192])
    faltas = rng.choices([0, 1, 2, 3, 6], weights=[60, 20, 10, 6, 4])[0]
    return {
        "codigo_colaborador": "E{:06d}".format(rng.randint(1, 9000)),
        "area": rng.choice(AREAS),
        "tipo_contrato": rng.choice(CONTRATOS),
        "horas_programadas": str(programadas),
        "horas_trabajadas": str(max(0, programadas - faltas * 8 - rng.randint(0, 10))),
        "faltas": str(faltas),
        "tardanzas": str(rng.choices([0, 1, 2, 4, 9],
                                     weights=[45, 25, 15, 10, 5])[0]),
        "horas_extra": str(rng.choices([0, 4, 8, 16, 30],
                                       weights=[50, 22, 15, 9, 4])[0]),
        "fecha_ingreso_empresa": fecha_txt(fecha_entre(rng, 4000, 30), rng, sucio),
        "periodo": fecha_entre(rng, 365).strftime("%Y-%m"),
    }


def tema_seguros(fake, rng, i, sucio):
    """8. Siniestralidad de polizas."""
    prima = rng.uniform(300, 9000)
    siniestros = rng.choices([0, 1, 2, 3, 5], weights=[62, 20, 10, 5, 3])[0]
    pagado = 0.0
    if siniestros:
        pagado = prima * rng.uniform(0.1, 3.2)
    return {
        "id_poliza": "POL-{:08d}".format(i),
        "tipo_seguro": rng.choice(TIPOS_SEGURO),
        "asegurado": fake.name(),
        "prima_anual": num_txt(prima, rng, sucio),
        "suma_asegurada": num_txt(prima * rng.uniform(15, 90), rng, sucio),
        "siniestros_reportados": str(siniestros),
        "monto_pagado": num_txt(pagado, rng, sucio),
        "edad_asegurado": str(rng.randint(18, 78)),
        "zona": rng.choice(ZONAS),
        "fecha_emision": fecha_txt(fecha_entre(rng, 1460, 15), rng, sucio),
    }


TEMAS = {
    "mipe": ("Riesgo crediticio de cartera MIPE", tema_mipe),
    "hipotecas": ("Evaluacion de solicitudes hipotecarias", tema_hipotecas),
    "cobranzas": ("Gestion de mora y cobranzas", tema_cobranzas),
    "inventario": ("Rotacion y quiebre de stock", tema_inventario),
    "suscripciones": ("Fuga de clientes en servicios por suscripcion", tema_suscripciones),
    "flota": ("Costos y eficiencia de flota de reparto", tema_flota),
    "personal": ("Productividad y ausentismo de personal", tema_personal),
    "seguros": ("Siniestralidad de polizas", tema_seguros),
}


# ---------------------------------------------------------------------------
# Generacion
# ---------------------------------------------------------------------------

def generar(tema, filas, output, semilla, sucio):
    descripcion, funcion = TEMAS[tema]

    rng = random.Random(semilla)
    fake = Faker("es_ES")
    Faker.seed(semilla)

    print("Tematica : {} ({})".format(descripcion, tema))
    print("Filas    : {:,}".format(filas).replace(",", " "))
    print("Output   : {}".format(output))
    print("Data     : {}".format("limpia" if not sucio else "con errores a proposito"))
    print("Generando...")

    primera = funcion(fake, rng, 1, sucio)
    columnas = list(primera.keys())

    duplicadas = 0
    invalidas = 0
    anterior = None

    with open(output, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        escritas = 0
        i = 1
        while escritas < filas:
            # Duplicar la fila anterior de vez en cuando
            if sucio and anterior is not None and rng.random() < 0.01:
                escritor.writerow(anterior)
                escritas += 1
                duplicadas += 1
                continue

            fila = funcion(fake, rng, i, sucio)
            if sucio:
                antes = dict(fila)
                fila = ensuciar(fila, rng)
                if fila != antes:
                    invalidas += 1

            escritor.writerow(fila)
            anterior = fila
            escritas += 1
            i += 1

            if escritas % 25000 == 0:
                print("  {} filas...".format(escritas))

    print("Listo.")
    print("  Total de filas    : {}".format(filas))
    if sucio:
        print("  Filas duplicadas  : {}".format(duplicadas))
        print("  Filas con defecto : {}".format(invalidas))
        print("  Tu proyecto debe detectar estas filas, no caerse con ellas.")


def listar_temas():
    print("Tematicas disponibles:")
    print()
    for clave in TEMAS:
        print("  {:<15} {}".format(clave, TEMAS[clave][0]))
    print()
    print("Ejemplo:  python generar_datos.py mipe --filas 50000")


def main():
    parser = argparse.ArgumentParser(
        description="Genera data sintetica para el proyecto final del curso.")
    parser.add_argument("tema", nargs="?", help="Clave de la tematica")
    parser.add_argument("--listar", action="store_true",
                        help="Muestra las tematicas disponibles")
    parser.add_argument("--filas", type=int, default=50000,
                        help="Cantidad de filas a generar (por defecto 50000)")
    parser.add_argument("--output", help="Nombre del archivo CSV de output")
    parser.add_argument("--semilla", type=int, default=2026,
                        help="Semilla: con la misma semilla sale la misma data")
    parser.add_argument("--limpio", action="store_true",
                        help="Genera data sin errores (no recomendado)")

    args = parser.parse_args()

    if args.listar or not args.tema:
        listar_temas()
        return

    if args.tema not in TEMAS:
        print("La tematica '{}' no existe.".format(args.tema))
        print()
        listar_temas()
        sys.exit(1)

    if args.filas < 1:
        print("La cantidad de filas debe ser mayor a cero.")
        sys.exit(1)

    output = args.output or "data_{}.csv".format(args.tema)

    try:
        generar(args.tema, args.filas, output, args.semilla, not args.limpio)
    except PermissionError:
        print("No se pudo escribir '{}'. Cierralo si lo tienes abierto.".format(output))
        sys.exit(1)
    except OSError as error:
        print("Error al escribir el archivo: {}".format(error))
        sys.exit(1)


if __name__ == "__main__":
    main()
