import requests

def callPokemons(url):
    resultado = requests.get(url)
    data = resultado.json()
    print(data['previous'])
    print(type(data['previous']))
    pokemones = data['results']
    for i,j in enumerate(pokemones):
        print(i+1,"=>",j['name'])
    if not (data['next'] == None) :
        callPokemons(data['next'])


callPokemons('https://pokeapi.co/api/v2/pokemon/')

