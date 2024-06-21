from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from firebase import get_firestore_client

router = APIRouter()

@router.get('/api/categorias')
def get_categorias():
    try:
        db = get_firestore_client()
        categorias_ref = db.collection('categorias')
        docs = categorias_ref.stream()

        categorias = []
        for doc in docs:
            categoria = doc.to_dict()
            categoria['id'] = doc.id
            categorias.append(categoria)

        return JSONResponse(content=categorias)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))