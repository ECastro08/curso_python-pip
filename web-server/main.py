import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Soy Eduardo Castro</h1>
        <h2>Soy ingeniero mecatronico</h2>
        <P> este parrafo nos dice que la fastapi ademas de mostrar datos como listas, json, tambien permite contenido HTML</p>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()