from fastapi import FastAPI, File, UploadFile
# from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from fastapi.responses import JSONResponse
from app.api.endpoints import productos, categorias
from typing import List
import os


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


UPLOAD_FOLDER = 'uploads/'

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run(app, host="127.0.0.1", port=8000)

# if __name__ == '__main__':
#     app.run(debug=True)
