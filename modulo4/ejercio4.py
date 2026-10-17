class Persona:
    def __init__(self):
        self.name=input("ingrese su name: ")
        self.dni=input("ingrese su dni: ")
        self.email=input("ingrese su email: ")
    def getData(self):
        return f"{self.name},{self.dni},{self.email}\n"
    def __str__(self):
        return f"{self.name},{self.dni},{self.email}"

class Data:
    def __init__(self,ruta):
        self.ruta=ruta
        self.openFile()
    def openFile(self):
        self.file= open(self.ruta,'+a')
    def agregarRegistro(self,persona):
        try:
            self.file.write(persona)
        except Exception as e:
            print("exepction is ",e)
    def closed(self):
        self.file.close()
    

bd=Data("C:\\Users\\User\\Desktop\\courseWorkspace\\workspacepy0926\\modulo4\\bd\\person.csv")

p=Persona()

bd.agregarRegistro(p.getData())

    