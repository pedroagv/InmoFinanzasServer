from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import productos, categorias,archivos
from fastapi.responses import FileResponse
from typing import List
from pathlib import Path
from datetime import datetime
import os

UPLOAD_FOLDER = 'uploads/'

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
app.include_router(archivos.router)

# app = Flask(__name__)

@app.get('/')
def hello_world():
    # Obtener la hora actual
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Formato HH:MM:SS    
    # Saludo que quieres retornar
    greeting = '¡Api InmofinanzasAGV en Python! '    
    # Concatenar el saludo con la hora actual
    message = greeting + 'La hora actual es ' + current_time    
    return message

if __name__ == '__main__': 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)