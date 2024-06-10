import firebase_admin
from firebase_admin import credentials, firestore

def get_firestore_client():
    if not firebase_admin._apps:
        cred = credentials.Certificate('inmofinanzafb-firebase.json')
        firebase_admin.initialize_app(cred)
    return firestore.client()
        