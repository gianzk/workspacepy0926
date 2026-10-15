

# Una clase es una plantilla de atributos y métodos que me permite generar objetos

class Customer:
    def __init__(self, nombre, correo, telefono):

        # atributos de mi clase cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # metodos
    def place_order(self):
        print('Realizar un pedido')
    
    def cancel_order(self):
        print('Cancelo un pedido')


# Las clases me ayudan a construir objetos

cliente_jorge = Customer('Jorge', 'jorge@gmail.com', '4655131')
cliente_maria = Customer('Maria', 'maria@gmail.com', '465513541')

# Manipulando el objeto jorge
print(cliente_jorge.correo)
cliente_jorge.place_order()


print(cliente_maria.nombre)
cliente_maria.cancel_order()





