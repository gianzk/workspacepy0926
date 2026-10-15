class Celular:

    def __init__(self):
        self.imei=input("ingrese el imei: ")
        self.brandDetail = self.getBrand()

    def getBrand(self):
        listBrands = """
        Determine la marca
                1. Samsung
                2. Motorola
                3. Iphone
            """
        print(listBrands)
        brand = int(input("Determina el brand: "))
        brandChoice = None
        if brand== 1:
            brandChoice = "Samsung"
        elif brand == 2:
            brandChoice = "Motorola"
        elif brand ==3:
            brandChoice = "Iphone"
        else:
            brandChoice = "No brand"
        return (brand,brandChoice)
    def __str__(self):
        return f"el celular de imei: {self.imei} de {self.brandDetail}"

class Catalogo:
    def __init__(self):
        self.celulares=[]
        self.register()

    def register(self):
        cantidad = int(input("ingrese la cantidad de celulares a registrar: "))
        for i in range(cantidad):
            print(f"REGISTRO CELULAR {i+1}")
            celularTemporal = Celular()
            self.celulares.append(celularTemporal)
    def mostrar(self):
        for c in self.celulares:
            print(c)
c1 = Catalogo()
c1.mostrar()
