from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import productos, categorias
from fastapi.responses import FileResponse
from typing import List
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

# app = Flask(__name__)

@app.get('/')
def hello_world():
    return '¡Primera deploy en Python'

@app.get("/uploads/{filename}")
async def get_image(filename: str):
    try:
        # La ruta completa de la imagen
        file_path = f"uploads/{filename}"
        # Devolver la imagen
        return FileResponse(file_path)
    except Exception as e:
        return str(e), 404


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    file_paths = []
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        file_paths.append(file_path)
    return JSONResponse(content={"message": "Files uploaded successfully", "file_paths": file_paths})

if __name__ == '__main__': 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)