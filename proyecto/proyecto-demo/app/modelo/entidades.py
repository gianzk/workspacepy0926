"""
Clases de dominio de TU tematica.

Aqui vive la regla de negocio. Si tu tematica es cobranzas, la clase se
llamara Deuda; si es inventario, Producto. El nombre importa: debe ser
la palabra que usa el area, no "Dato" ni "Registro".
"""


def a_decimal(texto):
    """Convierte texto a decimal. Acepta coma o punto."""
    if texto is None:
        raise ValueError("valor vacio")
    texto = str(texto).strip().replace(",", ".")
    if texto == "":
        raise ValueError("valor vacio")
    return float(texto)


def a_entero(texto):
    """Convierte texto a entero."""
    if texto is None:
        raise ValueError("valor vacio")
    texto = str(texto).strip()
    if texto == "":
        raise ValueError("valor vacio")
    return int(float(texto.replace(",", ".")))


class Cliente:
    """
    TODO: renombra esta clase con el nombre real de tu entidad.

    Sus atributos son las columnas del CSV que generaste.
    """

    def __init__(self,ruc,razon_social,sector,departamento,monto_otorgado,saldo_actual,dias_atraso,ventas_anuales,antiguedad_meses,fecha_desembolso):
        self.ruc=ruc
        self.razon_social=razon_social
        self.sector=sector
        self.departamento=departamento
        self.monto_otorgado=monto_otorgado
        self.saldo_actual=saldo_actual
        self.dias_atraso=dias_atraso
        self.ventas_anuales=ventas_anuales
        self.antiguedad_meses=antiguedad_meses
        self.fecha_desembolso=fecha_desembolso

    def nivel_riesgo(self):

        if self.dias_atraso <=5:
            return "NORMAL"
        elif self.dias_atraso <=15:
            return "Revisando"
        elif self.dias_atraso<=30:
            return "Problemas"
        else:
            return "Perdido"
    
    @classmethod
    def desde_fila(cls, fila):
        """
        TODO: construye el objeto a partir de una fila del CSV.

        Si la fila no sirve, levanta ValueError explicando el motivo.
        Valida al menos: campos obligatorios, tipos y rangos imposibles
        (montos negativos, fechas futuras, etc.).
        """
        raise NotImplementedError

    def clasificar(self):
        """
        TODO: tu regla de negocio.

        Devuelve la categoria o el puntaje que tu area necesita:
        nivel de riesgo, prioridad de llamada, estado de stock...
        """
        raise NotImplementedError

    def como_diccionario(self):
        """
        TODO: devuelve los datos como diccionario.

        La vista NO debe recibir objetos del modelo.
        """
        raise NotImplementedError
