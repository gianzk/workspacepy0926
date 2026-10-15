import requests 

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=1&year=2023'
respuesta = requests.get(url)

respuesta.status_code # 200 = OK 
data = respuesta.json()

for registro in data:
    
    print('='*5, registro['fecha'],'='*5)
    
    print(registro['compra'])