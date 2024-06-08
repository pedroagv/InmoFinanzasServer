from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

# from firebase_admin import firestore
# from ..core.firebase import get_firestore_client

router = APIRouter()

@router.get('/categorias')
def get_categorias():
    categorias = [
        {
            "id": 1,            
            "categoria": "Arriendos"
        },
        {
            "id": 2,            
            "categoria": "Ventas"
        },
        {
            "id": 3,            
            "categoria": "Permutas"
        }
    ]
    
    return JSONResponse(content=categorias)