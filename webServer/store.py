import requests

def getCategories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    # Para transformar el texto obtenido en un archivo python, haremos lo siguiente:
    categories = r.json()
    for category in categories:
        print(category['name'])