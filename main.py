from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import productos, categorias

app = FastAPI()

## Permitir cualquier origen (*), cualquier método y cualquier header en desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluyendo los routers de los diferentes módulos de endpoints
app.include_router(productos.router)
app.include_router(categorias.router)

# app = Flask(__name__)

@app.get('/')
def hello_world():
    return '¡Primera deploy en Python'




if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run(app, host="127.0.0.1", port=8000)

# if __name__ == '__main__':
#     app.run(debug=True)
