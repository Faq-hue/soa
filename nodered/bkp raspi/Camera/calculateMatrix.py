import sys
import cv2
import base64
import face_recognition
import numpy as np

def detect_face_encodings(image):
    faces_loc = face_recognition.face_locations(image)
    if not faces_loc:
       print("No faces found in the image.")
    else:
       for fl in faces_loc:
          encodings = face_recognition.face_encodings(image, known_face_locations=[fl])
          np.savetxt("matrix",encodings)

def main(image):
    if image is not None:
        # Detecta los rostros y calcula las matrices de codificación
        detect_face_encodings(image)
    else:
        print("La imagen no existe")

if __name__ == "__main__":
     image = cv2.imread('captura_imagen.jpg')
     main(image)
