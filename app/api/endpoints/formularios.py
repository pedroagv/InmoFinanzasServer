from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any
from firebase import get_firestore_client

router = APIRouter()

@router.post('/formulario-contacto-declaracion-renta')
def almacenar_datos(datos: Dict[str, Any]):
    try:
        db = get_firestore_client()
        collection_ref = db.collection('contacto-declaracion-renta')

        # Agregar el documento y obtener la referencia del documento
        doc_ref = collection_ref.add(datos)
                
        return JSONResponse(content={"message": "Datos almacenados correctamente"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
