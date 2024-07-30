import sys
import cv2
import json
import os
import face_recognition
import numpy as np

def compare_matriz(name):
    # Leer el contenido del primer archivo (matriz grande)
    with open(name, 'r') as file:
        caras_conocidas = json.load(file)

    # Leer el contenido del segundo archivo (submatriz)
    with open('matrix', 'r') as file:
        cara_a_comparar = file.read().strip()

    for matrix in caras_conocidas:
        for element in cara_a_comparar:
           res = face_recognition.compare_faces(matrix, element)
           if res:
              print("acierto")
           else:
              print("pucha")


def main(name):
   compare_matriz(name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <name>")
    else:
        name = sys.argv[1]
    main(name)

