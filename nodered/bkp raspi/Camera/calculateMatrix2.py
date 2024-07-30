import sys
import cv2
import json
import os
import face_recognition
import numpy as np

def detect_face_encodings(image, name):
    faces_loc = face_recognition.face_locations(image)
    if not faces_loc:
        print("No faces found in the image.")
        return
    
    encodings = []
    for fl in faces_loc:
        encoding = face_recognition.face_encodings(image, known_face_locations=[fl])[0]
        encodings.append(encoding.tolist())  # Convert ndarray to list
    
    if os.path.exists(name):
        with open(name, 'r') as archivo:
            try:
                contenido = json.load(archivo)
                contenido.extend(encodings)
            except json.JSONDecodeError:
                print("El archivo JSON está corrupto.")
                return
        
        with open(name, 'w') as file:
            json.dump(contenido, file)
    else:
        with open(name, 'w') as file:
            json.dump(encodings, file)

def main(image_path, name):
    image = cv2.imread(image_path)
    if image is not None:
        # Detecta los rostros y calcula las matrices de codificación
        detect_face_encodings(image, name)
    else:
        print("La imagen no existe.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python script.py <imagen> <archivo>")
    else:
        image_path = sys.argv[1]
        name = sys.argv[2]
        main(image_path, name)
