"""
Controlador.

Le pide cosas al modelo y se las pasa a la vista.
No calcula ni imprime. Si aqui aparece un print(), algo se hizo mal.
"""

import os

from app.modelo import ingesta, indicadores, exportador
from app.vista import consola
from app.modelo.repositorio import Repositorio

class Aplicacion:

    def __init__(self, ruta_csv, ruta_bd, carpeta_output):
        self.ruta_csv = ruta_csv
        self.carpeta_output = carpeta_output
        self.repositorio = Repositorio(ruta_bd)
        # TODO: crea el repositorio

    def cargar(self):
        """TODO: leer, validar, quitar duplicados, guardar, informar."""
        if not os.path.exists(self.ruta_csv): # false 
            print("el archivo ",self.ruta_csv,"no existe")
        else:
            print("el archivo existe",self.ruta_csv)
        print("Leyendo archivo .....")
        try:
            clientes,errores=ingesta.leer_csv(self.ruta_csv) # destruccturacion de funcion
        except Exception as e:
            print("error al procesar el archivo")
            return  

        #print(clientes[0],"muestra")

        clientes_unicos,duplicados = ingesta.quitar_duplicados(clientes)
        print(clientes_unicos[0], duplicados)

        cantidad=self.repositorio.guardar_clientes(clientes_unicos)
        print("se han registrado",cantidad)

    def ver_indicadores(self):
        registros = self.repositorio.listar()
        if not registros:
            print("no hay data cargada, usa la opcion 1")
            return
        try:
            ind = indicadores.calcular(registros)
        except Exception as e:
            print("error al calcular los indicadores", e)
            return

        print("=== INDICADORES DE CARTERA ===")
        print("Total de clientes:      {:>15,}".format(ind["total_clientes"]))
        print("Monto otorgado total:   {:>15,.2f}".format(ind["monto_otorgado_total"]))
        print("Saldo total:            {:>15,.2f}".format(ind["saldo_total"]))
        print("Cartera en mora (>30d): {:>15,.2f}".format(ind["cartera_en_mora"]))
        print("% de mora:              {:>14.2f}%".format(ind["porcentaje_mora"]))

        print()
        print("Distribucion por nivel de riesgo")
        print("{:<12}{:>10}{:>18}".format("Nivel", "Clientes", "Saldo"))
        for fila in ind["distribucion_riesgo"]:
            print("{:<12}{:>10,}{:>18,.2f}".format(
                fila["nivel"], fila["clientes"], fila["saldo"]))
        if ind["sin_dato_riesgo"]:
            print("{:,} clientes sin dias de atraso valido (no clasificados)".format(
                ind["sin_dato_riesgo"]))

        for titulo, clave in (("Top sectores por saldo", "saldo_por_sector"),
                              ("Top departamentos por saldo", "saldo_por_departamento")):
            print()
            print(titulo)
            print("{:<20}{:>10}{:>18}".format("Nombre", "Clientes", "Saldo"))
            for fila in ind[clave]:
                print("{:<20}{:>10,}{:>18,.2f}".format(
                    fila["nombre"], fila["clientes"], fila["saldo"]))

    def explorar(self):
        raise NotImplementedError

    def generar_entregable(self):
        registros = self.repositorio.listar()
        if not registros:
            print("no hay data cargada, usa la opcion 1")
            return
        try:
            ruta, filas = exportador.generar(registros, self.carpeta_output)
        except Exception as e:
            print("error al generar el entregable", e)
            return
        print("entregable generado:", ruta, "-", filas, "filas")

    def ver_historial(self):
        raise NotImplementedError

    def ejecutar(self):
        acciones = {
            "1": self.cargar,
            "2": self.ver_indicadores,
            "3": self.explorar,
            "4": self.generar_entregable,
            "5": self.ver_historial,
        }
        while True:
            consola.mostrar_menu()
            opcion = consola.pedir_opcion()
            if opcion == "6":
                consola.mensaje("Fin del proceso.")
                return
            accion = acciones.get(opcion)
            if accion is None:
                consola.advertencia("Esa opcion no existe.")
            else:
                accion()
