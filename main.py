from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import qrcode
from io import BytesIO
from PIL import Image
import base64
from app.api.endpoints import productos, categorias,archivos, formularios

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
app.include_router(formularios.router)

class QRData(BaseModel):
    data: str

#Incluyendo los routers de los diferentes módulos de endpoints
# app.include_router(productos.router)
# app.include_router(categorias.router)
# app.include_router(archivos.router)

@app.get('/')
def hello_world():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    greeting = '¡Api InmofinanzasAGV en Python! '
    message = greeting + 'La hora actual es ' + current_time
    return message

@app.post("/generate_qr/")
async def generate_qr(qrdata: QRData):
    try:
        # Obtener los datos de entrada
        data = qrdata.data

        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Crear la imagen del código QR en BytesIO
        img = qr.make_image(fill_color="black", back_color="white")
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Convertir la imagen a base64
        base64_img = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

        return {"image_base64": base64_img}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__': 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
