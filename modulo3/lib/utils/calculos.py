class User:
    def __init__(self,first_name,last_name,edad,telefono,correo,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.edad=edad
        self.telefono=telefono
        self.correo=correo
        self.salary=salary
        self.risk= 0
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
