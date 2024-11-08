import store
from fastapi import FastAPI
# Para obtener una respuesta en HTML haremos lo siguiente
from fastapi.responses import HTMLResponse

# Creamos una instancia de la aplicación de la siguiente forma
app = FastAPI()

#Creamos un decorador:
@app.get('/') # Creamos un ruta por la cual desde la web van a poder ingresar

def getList():
    return [1, 2, 3]

#Creamos un decorador:
@app.get('/contact', response_class = HTMLResponse) # Creamos un ruta por la cual desde la web van a poder ingresar

def getList():
    return """
        <h1> Hola soy una página </h1>
        <p> Soy un párrafo </p>
        """


def run():
    store.getCategories()
    
if __name__ == '__main__':
    run()