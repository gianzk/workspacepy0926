# Proyecto final del curso

Herramienta de consola que toma data cruda, la valida, la guarda, calcula
indicadores y entrega un archivo procesado para otra area de la empresa.

## Por donde empezar

1. Lee **`DEFINICION_PROYECTO.md`** — que se construye, por que, y como generar tu data
2. Elige tu tema en **`TEMATICAS.md`**
3. Genera tu data con **`generador-datos/`**
4. Copia **`plantilla/`** y empieza a trabajar

## Generar tu data

La data del proyecto es ficticia y la generas tu mismo.

```
pip install faker

cd generador-datos
python generar_datos.py --listar
python generar_datos.py mipe --filas 50000
```

Opciones:

| Opcion | Para que sirve |
|---|---|
| `--filas N` | Cuantas filas generar (por defecto 50 000) |
| `--output archivo.csv` | Nombre del archivo de output |
| `--semilla N` | Con la misma semilla sale exactamente la misma data |
| `--limpio` | Genera data sin errores |

El archivo sale **con errores a proposito**: campos vacios, fechas en dos
formatos, numeros con coma decimal, espacios de mas y filas duplicadas.
No uses `--limpio` para tu entrega: tu herramienta tiene que saber
defenderse de esa data.

## Contenido

```
proyecto/
├── DEFINICION_PROYECTO.md    Proposito, flujo y requisitos
├── TEMATICAS.md              Temas entre los que elegir
├── generador-datos/          Script que genera tu CSV
└── plantilla/                Estructura vacia para tu proyecto
```
