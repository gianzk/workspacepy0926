"""
Controlador.

Le pide cosas al modelo y se las pasa a la vista.
No calcula ni imprime. Si aqui aparece un print(), algo se hizo mal.
"""

import os

from app.modelo import ingesta
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
        # usar librerias para ver tablas , consola 
        # mostrar datos 
        raise NotImplementedError

    def explorar(self):
        raise NotImplementedError

    def generar_entregable(self):
        #
        raise NotImplementedError

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
