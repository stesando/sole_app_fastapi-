from fastapi import FastAPI

app = FastAPI(title="Mi primer proyecto con FastAPI", version="1.0")

# GET
@app.get("/")
def inicio():
    return {"mensaje": "GET funcionando"}

# GET con parámetro
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"hola": nombre}

# POST
@app.post("/crear")
def crear():
    return {"mensaje": "POST funcionando"}

# PUT
@app.put("/actualizar")
def actualizar():
    return {"mensaje": "PUT funcionando"}

# DELETE
@app.delete("/eliminar")
def eliminar():
    return {"mensaje": "DELETE funcionando"}



