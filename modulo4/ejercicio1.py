import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

respuesta = requests.get(url)

print(respuesta)
datos = respuesta.json()
print(type(datos))

print(datos['count'],datos['next'])
try:
    pokemones = datos['results']
    #print(pokemones)
    for i,j in enumerate(pokemones):
        print(i+1,"=>",j['name'])
    
except Exception as e:
    print("el error es ", e)

