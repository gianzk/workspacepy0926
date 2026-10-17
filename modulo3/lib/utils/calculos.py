class Acoount:
    monedas=("PEN","USD")
    list_types = ("CA","CC","CLP")
    def __init__(self,dni):
        self.idAccount=None #generado
        self.dni=dni #ingresamos ese valor
        self.getCuestions()
        self.getIdAccount()
    def getCuestions(self):
        self.getType()
        self.getMoneda()
    def getAccount(self):
        if self.type and self.moneda:
            pass
        else:
            print("La cuenta debe tener moneda y tipo")
    def getType(self):
        while True:
            type_choice=input(f"Ingrese el tipo de cuenta {self.list_types}")
            print(type_choice)
            if type_choice in self.list_types:
                self.type= type_choice
                break
            else:
                print(f"Ingrese un tipo de cuenta valida {self.list_types}")
        print(self.type)
    def getMoneda(self):
        while True:
            type_choice=input(f"Ingrese el tipo de cuenta {self.monedas}")
            print(type_choice)
            if type_choice in self.monedas:
                self.moneda= type_choice
                break
            else:
                print(f"Ingrese un tipo de cuenta valida {self.monedas}")        
    def getIdAccount(self):
        moneda=[("194","PEN"),("193","USD")]
        types =[("2050","CA"),("3025","CC")]
        numberId =[""]
        for i in moneda:
            if self.moneda.upper() == moneda[i][1]:
                numberId.append(moneda[i][0])
        numerId= numberId.join("")
        self.idAccount= numerId
        return numerId


acc = Acoount("4679797")

class User:
    def __init__(self,first_name,last_name,edad,telefono,correo,salary,dni):
        self.first_name=first_name
        self.last_name=last_name
        self.edad=edad
        self.telefono=telefono
        self.correo=correo
        self.salary=salary
        self.dni= dni
        self.risk= 0
        self.accounts = []
    def calculateRisk(self):
        try:
            print("Cuestionario de Preguntas para riesgo, para salir presionar R")
            # 0 - 1
            questions = [
                ("tienes propiedades",5),
                ("eres dependiente",3),
                ("cuentas con deudas en otras entidades",2),
                ("cuenta con algun seguro",1)
            ]
            resultados = []
            suma=0
            for i in questions:
                opcion = input(f"{i[0]} (S/N):")
                if opcion.upper()== "S":
                    resultados.append(1)
                else:
                    resultados.append(0)
            for j in resultados:
                suma+=j*questions[j][1]
            self.risk =suma/len(questions)
            return self.risk
        except Exception as e:
            print("Ups ha surgio un error ",e)
    def getRisk(self):
        return self.risk
    def createAccount(self):
        accTmp = Acoount(self.dni)
        self.accounts.append(accTmp)

# 1 usuario => cuentas bancarias ? (n ) 
