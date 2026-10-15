class Customer:
    def __init__(self,name,dni,age,salary):
        self.namev2=name
        self.dniv2=dni
        self.agev2=age
        self.salaryv2=salary
        self.typecv2= 1
        pass

    def mostrarNombre(self):
        print(f"el nombre del cliente es {self.namev2},y  {self.parserTypeCustomer()}")

    def parserTypeCustomer(self):
        if self.typecv2==0:
            return 'cliente Normal'
        elif self.typecv2==1:
            return 'cliente Vip'
        else:
            return 'No es cliente'
    def __str__(self):
        return f"datos: {self.namev2} {self.agev2} con {self.dniv2} y {self.salaryv2}"

    
name=input("ingrese su name: ")
dni=input("ingrese su dni: ")
age=int(input("ingrese su age: "))
salary=float(input("ingrese su salary: "))
CustomerOne= Customer(name=name,dni=dni,age=age,salary=salary)
CustomerOne.mostrarNombre()

print(CustomerOne)