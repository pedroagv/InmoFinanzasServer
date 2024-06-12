from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
from firebase import get_firestore_client

router = APIRouter()

@router.get('/productos')
def get_productos():
    try:
        db = get_firestore_client()
        productos_ref = db.collection('Productos')
        docs = productos_ref.stream()

        productos = []
        for doc in docs:
            producto = doc.to_dict()
            producto['id'] = doc.id
            productos.append(producto)

        return JSONResponse(content=productos)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/productos')
def add_producto(productos: List[Dict[str, Any]]):
    try:
        db = get_firestore_client()
        productos_ref = db.collection('Productos')

        for producto in productos:
            productos_ref.add(producto)

        return JSONResponse(content={"message": "Products added successfully!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/productos/{producto_id}')
def update_producto(producto_id: str, producto: Dict[str, Any]):
    try:
        db = get_firestore_client()
        producto_ref = db.collection('Productos').document(producto_id)

        # Verificar si el documento existe antes de intentar actualizarlo
        if not producto_ref.get().exists:
            raise HTTPException(status_code=404, detail="Product not found")

        producto_ref.update(producto)
        return JSONResponse(content={"message": "Product updated successfully!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete('/productos/{producto_id}')
def delete_producto(producto_id: str):
    try:
        db = get_firestore_client()
        producto_ref = db.collection('Productos').document(producto_id)

        # Verificar si el documento existe antes de intentar eliminarlo
        if not producto_ref.get().exists:
            raise HTTPException(status_code=404, detail="Product not found")

        producto_ref.delete()
        return JSONResponse(content={"message": "Product deleted successfully!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
