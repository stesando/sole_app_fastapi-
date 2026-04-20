from fastapi import FastAPI

app = FastAPI(title="mi primera API", version="1.0")


# Metodos : GET, POST, PUT, DELETE
@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.get("/saludo/{nombre}")
async def saludo_custom(nombre: str):
	return {"hola": nombre}
