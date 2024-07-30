import cv2
import face_recognition
cap = cv2.VideoCapture(0)

num=0
color=(50,50,255)
while True:
    ret, frame= cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    face_locs = face_recognition.face_locations(frame)
    #print(face_locs)
    for fl in face_locs:
        cv2.rectangle(frame, (fl[3], fl[0]), (fl[1],fl[2]), color, 2)

    face_rec = face_recognition.face_encodings(frame,known_face_locations=face_locs)
    print(face_rec)

    cv2.imshow('c=capturar q=salir', frame)
    key=cv2.waitKey(1)
    if ord('q')==key:
        break
    if ord('c')==key:
        filename=f'images/image{num}.jpg'
        cv2.imwrite(filename, frame)
        print(f'Se capturó {filename}')

    num+=1

cv2.destroyAllWindows()
