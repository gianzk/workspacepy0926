# Proyecto final — Definición

## Propósito

Construir una **herramienta de consola que un área de una empresa podría usar todos los días**.

No es un sistema de registro. Nadie va a sentarse a tipear mil clientes a mano. El punto de partida es el opuesto: el área ya tiene la data, la recibe en volumen, y no tiene cómo convertirla en algo útil. Tu herramienta cubre ese tramo completo:

```
data cruda  →  validación  →  almacenamiento  →  indicadores  →  entregable
```

El entregable final es un archivo procesado que **otro equipo recibe y usa**. Esa es la frase que define si el proyecto está bien hecho: si alguien de otra área abre tu archivo de output y puede tomar una decisión con él, funcionó.

## El flujo end-to-end

| Etapa | Qué pasa | Dónde vive |
|---|---|---|
| **Ingesta** | Se lee el CSV del día (decenas de miles de filas) | `modelo/ingesta.py` |
| **Validación** | Se separan filas válidas de inválidas; nada tumba el programa | `modelo/ingesta.py` |
| **Persistencia** | La data válida se guarda en SQLite, sin duplicar | `modelo/repositorio.py` |
| **Cálculo** | Se calculan indicadores y se aplica la regla de negocio | `modelo/indicadores.py` |
| **Entrega** | Se exporta el archivo para la otra área | `modelo/exportador.py` |
| **Control** | El usuario dispara todo esto desde un menú | `vista/` + `controlador/` |

## El menú no es un CRUD

La vista es el panel de control del flujo, no un formulario de registro:

```
1. Cargar data del día
2. Ver indicadores
3. Explorar la data
4. Generar entregable
5. Historial de cargas
6. Salir
```

Detalle importante de la opción 1: **si se corre dos veces el mismo día, no debe duplicar la data**. Eso te obliga a llevar un registro de cargas, que es justo lo que hace cualquier proceso real.

## Arquitectura: MVC

El proyecto se organiza en tres capas, cada una en su propio paquete:

```
main.py
app/
├── modelo/        Qué hace el negocio. No imprime nada.
├── vista/         Cómo se ve. No calcula nada.
└── controlador/   Quién coordina a los otros dos.
```

Tres reglas que se verifican leyendo los imports:

1. `vista/` es el **único** lugar donde pueden aparecer `print()`, `input()` y la librería de consola
2. `modelo/` **nunca** importa nada de `vista/`
3. `modelo/` no devuelve DataFrames hacia afuera: entrega listas y diccionarios

La prueba de que respetaste el MVC: si mañana hubiera que cambiar la consola por una página web, solo se reescribe `vista/`. Nada más.

## Requisitos técnicos

Cada módulo del curso tiene que aparecer en el proyecto:

| Módulo | Dónde se ve |
|---|---|
| 1 — Tipos y colecciones | Estructuras de datos del modelo |
| 2 — Bucles y funciones | Menú, validaciones, funciones del negocio |
| 3 — POO, errores y paquetes | Clases de dominio, `try/except`, los tres paquetes |
| 4 — Ficheros y SQLite | Lectura del CSV, base de datos, exportación |
| 5 — pandas | Indicadores y transformaciones |

Además:

- La herramienta **no puede caerse** con data sucia: campos vacíos, fechas mal escritas, números con formato distinto, filas duplicadas. El generador de datos los incluye a propósito.
- Los errores se muestran al usuario en español y de forma legible. Un `Traceback` en pantalla es un error del proyecto.
- El volumen mínimo es de **50 000 filas**. A ese tamaño recorrer la data con un `for` se nota lento: por eso se usa pandas.

## Entregables

1. El código fuente completo, con la estructura MVC
2. El CSV de entrada usado y el archivo de output generado
3. La base de datos SQLite con la data cargada
4. Un `README.md` que explique: qué área usa esto, qué problema resuelve, cómo se ejecuta y qué significa cada indicador
5. Sustentación: correr la herramienta en vivo, de principio a fin

## Punto de partida

- `TEMATICAS.md` — las temáticas entre las que puedes elegir
- `generador-datos/` — el script que genera tu CSV
- `plantilla/` — la estructura de carpetas vacía, lista para copiar
- `ejemplo-guiado/` — el mismo proyecto resuelto para otra temática, explicado paso a paso
