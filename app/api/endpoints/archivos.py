from fastapi import FastAPI, File, UploadFile
from fastapi import APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import productos, categorias
from fastapi.responses import FileResponse
from typing import List
from pathlib import Path
import os
from firebase import get_firestore_client
from google.cloud import firestore  # Importa la clase firestore desde google.cloud
from dotenv import load_dotenv


load_dotenv()

UPLOAD_FOLDER = 'uploads/'

router = APIRouter()

@router.get("/uploads/{folder}/{filename}")
async def get_image(folder: str, filename: str):
    try:
        UPLOADS_DIR = Path("uploads")
        # Construir la ruta completa de la imagen
        file_path = UPLOADS_DIR / folder / filename
        # Verificar si el archivo existe
        if not file_path.is_file():
            return "Imagen no encontrada", 404
        # Devolver la imagen
        return FileResponse(file_path)
    except Exception as e:
        return str(e), 500

@router.post("/upload")
async def upload_files(folder: str, files: List[UploadFile] = File(...)):

    base_url_api = os.getenv('BASE_URL_API')

    # Verificar si el documento existe en Firestore
    db = get_firestore_client()
    Producto_ref = db.collection('Productos').document(folder)
    Producto = Producto_ref.get()

    if not Producto.exists:
        raise HTTPException(status_code=404, detail="El prodcuto no existe")
    
    folder_path = os.path.join(UPLOAD_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    imagenes = [] 
    for file in files:
        file_path = os.path.join(folder_path, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            imagenes.append({
                'src': base_url_api + file_path
            })
          # Actualizar el documento en Firestore con los file_paths
    Producto_ref.update({
        'imagenes': imagenes
    })
    
    return JSONResponse(content={"message": "Files uploaded successfully", "file_paths": imagenes})