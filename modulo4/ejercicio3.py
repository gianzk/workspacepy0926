import requests

url = 'https://pokeapi.co/api/v2/pokemon/1/'

respuesta = requests.get(url)

print(respuesta)
datos = respuesta.json()
print(type(datos))

class Pokemon:
    def __init__(self,name,base_experience,abilities):
        self.name=name
        self.base_experience=base_experience
        self.abilities= abilities


class Podekex:
    def __init__(self):
        self.pokemons=[]
    def agregar_pokemon(self,p:Pokemon):
        self.pokemons.append(p)


pok1 = Pokemon()