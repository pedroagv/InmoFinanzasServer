from dotenv import load_dotenv
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def get_firestore_client():
    if not firebase_admin._apps:
        # Obtener el contenido del archivo JSON desde la variable de entorno
        firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')

        if firebase_credentials:
            try:
                # Convertir la cadena JSON a un diccionario
                firebase_credentials_dict = json.loads(firebase_credentials)

                # Crear una credencial de Firebase a partir del diccionario
                cred = credentials.Certificate(firebase_credentials_dict)
                
                # Inicializar la aplicación de Firebase
                firebase_admin.initialize_app(cred)
                
                # Retornar el cliente de Firestore
                return firestore.client()
            
            except json.JSONDecodeError as e:
                print(f"Error al decodificar las credenciales JSON: {e}")
                return None
            except ValueError as e:
                print(f"Error al crear las credenciales de Firebase: {e}")
                return None

        else:
            print("Las credenciales de Firebase no se encontraron en las variables de entorno.")
            return None
    
    else:
        # Si la aplicación Firebase ya está inicializada, retornar el cliente de Firestore
        return firestore.client()
    
    
# ############### solo para desarrollo
# import json
# import firebase_admin
# from firebase_admin import credentials, firestore

# def get_firestore_client():
#     if not firebase_admin._apps:
#         # Path to the Firebase credentials JSON file
#         credentials_path = "inmofinanzafb-firebase.json"

#         # Read the Firebase credentials from the JSON file
#         with open(credentials_path) as f:
#             firebase_credentials_dict = json.load(f)

#         # Initialize Firebase using the service account credentials from the JSON file
#         cred = credentials.Certificate(firebase_credentials_dict)
#         firebase_admin.initialize_app(cred)

#     # Return the Firestore client
#     return firestore.client()
