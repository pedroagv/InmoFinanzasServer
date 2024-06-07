from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# app = Flask(__name__)

@app.get('/')
def hello_world():
    return '¡Hola, mundo desde el servidor! ajaj'

@app.get('/productos')
def get_productos():
    productos = [
        {
            "id": 1,
            "nombre": "Arriendo Apartamento en el centro",
            "ubicacion": "Ciudad A",
            "precio": 120000,
            "descripcion": "Un hermoso apartamento en el corazón de la ciudad.",
            "categoria": "Arriendos",            
            "metros_cuadrados": 80,
            "destacado":True,
            "imagenes":[
                {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
            ]              
        },
        {
            "id": 2,
            "nombre": "Casa en las afueras",
            "ubicacion": "Ciudad B",
            "precio": 250000,
            "descripcion": "Una casa espaciosa con un gran jardín.",
            "categoria": "Venta",
            "metros_cuadrados": 200,
            "imagenes":[
                {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
            ]             
        },
        {
            "id": 3,
            "nombre": "Arriendo Estudio cerca del mar",
            "ubicacion": "Ciudad C",
            "precio": 95000,
            "descripcion": "Un acogedor estudio a pocos metros de la playa.",
            "categoria": "Arriendos",
            "metros_cuadrados": 45,
            "imagenes":[
                   {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },
        {
            "id": 4,
            "nombre": "Hermosa casa Fontibon",
            "ubicacion": "Ciudad Bogota",
            "precio": 100000,
            "descripcion": "una hermosa casa en fontibon muy economica.",
            "categoria": "Ventas",
            "metros_cuadrados": 49,
            "imagenes":[
                    {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },
        {
            "id": 5,
            "nombre": "Arriendo Hermosa casa Frente al lago",
            "ubicacion": "Ciudad Bogota",
            "precio": 100000,
            "descripcion": "una hermosa casa en engativa muy linda y economica.",
            "categoria": "Arriendos",
            "metros_cuadrados": 409,
            "imagenes":[
                    {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },
        {
            "id": 6,
            "nombre": "Hermosa casa verde frente al pasto",
            "ubicacion": "Ciudad Bogota",
            "precio": 50000,
            "descripcion": "Una hermosa casa en engativa muy linda y economica.",
            "categoria": "Permuta",
            "metros_cuadrados": 409,
            "imagenes":[
                    {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },{
            "id": 1,
            "nombre": "Arriendo Apartamento en el centro",
            "ubicacion": "Ciudad A",
            "precio": 120000,
            "descripcion": "Un hermoso apartamento en el corazón de la ciudad.",
            "categoria": "Arriendos",            
            "metros_cuadrados": 80,
            "destacado":True,
            "imagenes":[
                {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
            ]              
        },
        {
            "id": 2,
            "nombre": "Casa en las afueras",
            "ubicacion": "Ciudad B",
            "precio": 250000,
            "descripcion": "Una casa espaciosa con un gran jardín.",
            "categoria": "Venta",
            "metros_cuadrados": 200,
            "imagenes":[
                {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
            ]             
        },
        {
            "id": 3,
            "nombre": "Arriendo Estudio cerca del mar",
            "ubicacion": "Ciudad C",
            "precio": 95000,
            "descripcion": "Un acogedor estudio a pocos metros de la playa.",
            "categoria": "Arriendos",
            "metros_cuadrados": 45,
            "imagenes":[
                   {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },
        {
            "id": 4,
            "nombre": "Hermosa casa Fontibon",
            "ubicacion": "Ciudad Bogota",
            "precio": 100000,
            "descripcion": "una hermosa casa en fontibon muy economica.",
            "categoria": "Ventas",
            "metros_cuadrados": 49,
            "imagenes":[
                    {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },
        {
            "id": 5,
            "nombre": "Arriendo Hermosa casa Frente al lago",
            "ubicacion": "Ciudad Bogota",
            "precio": 100000,
            "descripcion": "una hermosa casa en engativa muy linda y economica.",
            "categoria": "Arriendos",
            "metros_cuadrados": 409,
            "imagenes":[
                    {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        },
        {
            "id": 6,
            "nombre": "Hermosa casa verde frente al pasto",
            "ubicacion": "Ciudad Bogota",
            "precio": 50000,
            "descripcion": "Una hermosa casa en engativa muy linda y economica.",
            "categoria": "Permuta",
            "metros_cuadrados": 409,
            "imagenes":[
                    {
                   "src": "https://picsum.photos/800/400?random=4",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                },
                {
                    "src": "https://picsum.photos/800/400?random=3",
                    "alt": "...",
                    "label": "First slide label",
                    "content": "Some representative placeholder content for the first slide."
                    },
                {
                   "src": "https://picsum.photos/800/400?random=2",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ,
                {
                   "src": "https://picsum.photos/800/400?random=1",
                   "alt": "...",
                   "label": "First slide label",
                   "content": "Some representative placeholder content for the first slide."
                }
                ]               
        }
    ]
    return JSONResponse(content=productos)

@app.get('/categorias')
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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# if __name__ == '__main__':
#     app.run(debug=True)
