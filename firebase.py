# import os
# import json
# from dotenv import load_dotenv
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Cargar las variables de entorno desde el archivo .env
# load_dotenv()

# def get_firestore_client():
#     if not firebase_admin._apps:
#         # Obtener el contenido del archivo JSON desde la variable de entorno
#         firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')
#         #firebase_credentials = os.getenv('inmofinanzafb-firebase.json')

#         if firebase_credentials:
#             # Convertir la cadena JSON a un diccionario
#             firebase_credentials_dict = json.loads(firebase_credentials)

#             # Crear una credencial de Firebase a partir del diccionario
#             cred = credentials.Certificate(firebase_credentials_dict)
            
#             # Inicializar la aplicación de Firebase
#             firebase_admin.initialize_app(cred)
#         else:
#             print("Las credenciales de Firebase no se encontraron en las variables de entorno.")
#             return None
    
#     return firestore.client()

import json
import firebase_admin
from firebase_admin import credentials, firestore

def get_firestore_client():
    if not firebase_admin._apps:
        # Path to the Firebase credentials JSON file
        credentials_path = "inmofinanzafb-firebase.json"

        # Read the Firebase credentials from the JSON file
        with open(credentials_path) as f:
            firebase_credentials_dict = json.load(f)

        # Initialize Firebase using the service account credentials from the JSON file
        cred = credentials.Certificate(firebase_credentials_dict)
        firebase_admin.initialize_app(cred)

    # Return the Firestore client
    return firestore.client()
