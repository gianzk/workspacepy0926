# Temáticas disponibles

Todas las temáticas de esta lista resuelven **el mismo problema de fondo**, solo cambia el sector:

> Un área de la empresa recibe data cruda en volumen, no tiene forma de procesarla y necesita una herramienta que la cargue, la valide, calcule indicadores y entregue un archivo limpio para que otro equipo lo use.

Elige una. El esfuerzo es equivalente en todas; escoge la que te resulte más fácil de explicar en tu sustentación.

La data de todas las temáticas es **generada** con el script `generador-datos/generar_datos.py`. No se usa data de ninguna empresa real ni se trabaja con nombres comerciales: los clientes, productos y operaciones son ficticios.

Cada alumno genera **solo la data de su temática**, una ejecución por archivo. Cada temática tiene una *clave* (indicada abajo en "Clave del generador") que se pasa al script:

```
cd generador-datos
python generar_datos.py --listar                 # muestra las 8 claves
python generar_datos.py cobranzas                # data_cobranzas.csv, 50 000 filas
python generar_datos.py cobranzas --filas 80000 --output mi_data.csv
```

Deja el archivo dentro de la carpeta `data/` de tu proyecto. Requiere `pip install faker`.
El paso a paso completo, con lo que debes esperar dentro del archivo y qué hacer si
algo falla, está en `DEFINICION_PROYECTO.md`, sección *Cómo generar tu data*.

---

## 1. Riesgo crediticio de cartera MIPE
**Área usuaria:** Créditos y Riesgos
**Clave del generador:** `mipe`
**Pregunta de negocio:** ¿Cuánto dinero tenemos expuesto y en qué clientes se concentra el riesgo?

- **Entidad principal:** cliente con un crédito vigente
- **Campos del CSV:** ruc, razón social, sector, departamento, monto otorgado, saldo actual, días de atraso, ventas anuales declaradas, antigüedad del negocio, fecha de desembolso
- **Indicadores mínimos:** distribución de clientes por nivel de riesgo, monto expuesto total y por nivel, saldo promedio por sector, top 10 de mayor exposición
- **Regla de negocio propia:** clasificar cada cliente en Normal / Con Problemas / Deficiente / Dudoso / Pérdida según días de atraso y nivel de endeudamiento
- **Entregable:** cartera clasificada con su nivel de riesgo asignado

## 2. Evaluación de solicitudes hipotecarias
**Área usuaria:** Banca Hipotecaria
**Clave del generador:** `hipotecas`
**Pregunta de negocio:** ¿Qué solicitudes pasan el filtro y cuánto financiamiento representan?

- **Entidad principal:** solicitud de crédito hipotecario
- **Campos del CSV:** id solicitud, dni, ingreso mensual, deudas mensuales, valor del inmueble, cuota inicial, plazo en años, tipo de contrato laboral, dependientes, fecha de solicitud
- **Indicadores mínimos:** tasa de aprobación, cuota promedio, ratio cuota/ingreso promedio, monto a financiar por rango de plazo
- **Regla de negocio propia:** calcular la cuota mensual, el ratio cuota/ingreso y el ratio préstamo/valor; aprobar, observar o rechazar según umbrales
- **Entregable:** solicitudes con su dictamen y el motivo del rechazo cuando aplique

## 3. Gestión de mora y cobranzas
**Área usuaria:** Cobranzas
**Clave del generador:** `cobranzas`
**Pregunta de negocio:** ¿A quién llamamos primero mañana?

- **Entidad principal:** cuota vencida
- **Campos del CSV:** id operación, documento del cliente, monto de la cuota, fecha de vencimiento, fecha de pago, canal de contacto preferido, gestiones previas, promesa de pago incumplida
- **Indicadores mínimos:** monto total vencido por tramo de atraso, efectividad de las gestiones previas, recuperación del mes, concentración de deuda por tramo
- **Regla de negocio propia:** puntuar cada caso por monto, días vencidos y comportamiento previo para ordenar la cola de llamadas
- **Entregable:** cola de cobranza priorizada para el día siguiente

## 4. Rotación y quiebre de stock
**Área usuaria:** Logística y Compras
**Clave del generador:** `inventario`
**Pregunta de negocio:** ¿Qué compramos esta semana y qué dejamos de comprar?

- **Entidad principal:** movimiento de inventario por producto y local
- **Campos del CSV:** código de producto, categoría, local, stock actual, stock mínimo, unidades vendidas en el mes, costo unitario, precio de venta, fecha del último ingreso
- **Indicadores mínimos:** productos en quiebre y en sobrestock, rotación por categoría, capital inmovilizado, margen por categoría
- **Regla de negocio propia:** calcular días de cobertura y clasificar cada producto en Reponer urgente / Normal / Exceso
- **Entregable:** orden de reposición sugerida por local

## 5. Fuga de clientes en servicios por suscripción
**Área usuaria:** Retención y Comercial
**Clave del generador:** `suscripciones`
**Pregunta de negocio:** ¿Qué clientes están por irse y cuánto ingreso se va con ellos?

- **Entidad principal:** cliente con plan activo
- **Campos del CSV:** id cliente, plan contratado, meses de permanencia, consumo del último mes, consumo promedio histórico, reclamos registrados, pagos atrasados, fecha de alta
- **Indicadores mínimos:** clientes en riesgo de fuga, ingreso mensual en riesgo, permanencia promedio por plan, relación entre reclamos y fuga
- **Regla de negocio propia:** puntuar riesgo de fuga según caída de consumo, reclamos y atrasos
- **Entregable:** lista de clientes a contactar con su nivel de riesgo

## 6. Costos y eficiencia de flota de reparto
**Área usuaria:** Operaciones y Distribución
**Clave del generador:** `flota`
**Pregunta de negocio:** ¿Qué rutas nos están costando más de lo que deberían?

- **Entidad principal:** viaje realizado
- **Campos del CSV:** id viaje, placa, ruta, kilómetros recorridos, combustible consumido, entregas programadas, entregas efectivas, hora de salida, hora de retorno, peajes
- **Indicadores mínimos:** costo por entrega, rendimiento de combustible por vehículo, cumplimiento de entregas por ruta, horas improductivas
- **Regla de negocio propia:** detectar viajes fuera de rango de consumo o de cumplimiento y marcarlos para revisión
- **Entregable:** reporte de rutas con desviación de costo

## 7. Productividad y ausentismo de personal
**Área usuaria:** Recursos Humanos
**Clave del generador:** `personal`
**Pregunta de negocio:** ¿Dónde se nos está yendo la hora-hombre?

- **Entidad principal:** registro de asistencia mensual por colaborador
- **Campos del CSV:** código de colaborador, área, tipo de contrato, horas programadas, horas trabajadas, faltas, tardanzas, horas extra, fecha de ingreso a la empresa
- **Indicadores mínimos:** tasa de ausentismo por área, horas extra pagadas, rotación del período, correlación entre antigüedad y ausentismo
- **Regla de negocio propia:** calcular el índice de ausentismo y marcar las áreas que superan el umbral aceptable
- **Entregable:** reporte de ausentismo por área con sus casos críticos

## 8. Siniestralidad de pólizas
**Área usuaria:** Suscripción de Seguros
**Clave del generador:** `seguros`
**Pregunta de negocio:** ¿Qué segmentos nos están costando más de lo que nos pagan?

- **Entidad principal:** póliza con sus siniestros del período
- **Campos del CSV:** id póliza, tipo de seguro, prima anual, suma asegurada, siniestros reportados, monto pagado en siniestros, antigüedad del asegurado, zona, fecha de emisión
- **Indicadores mínimos:** índice de siniestralidad por tipo y zona, prima promedio, pólizas con siniestralidad sobre el 100%, resultado técnico del período
- **Regla de negocio propia:** calcular siniestralidad por póliza y segmento, y marcar los segmentos a reevaluar
- **Entregable:** reporte de siniestralidad con recomendación por segmento

---

## Lo que toda temática debe cumplir

Sea cual sea la que elijas, tu herramienta tiene que:

1. Cargar un CSV de al menos **50 000 filas** generado con el script del curso
2. **Rechazar y registrar** las filas inválidas en lugar de caerse
3. Guardar la data válida en **SQLite** sin duplicar si se carga dos veces el mismo día
4. Calcular los **indicadores mínimos** de tu temática con pandas
5. Aplicar tu **regla de negocio** para clasificar o priorizar cada registro
6. Exportar el **entregable** en un archivo que otra área pueda abrir

Si quieres trabajar un sector que no está en la lista, propónlo: debe cumplir los mismos seis puntos.
