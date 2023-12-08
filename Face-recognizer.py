import face_recognition
import numpy as np
import cv2
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from gpiozero import Button

btn = Button(23)

btn.wait_for_press()

video_captuer = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
Albert_image = face_recognition.load_image_file("Dataset/Albert Einstein.jpg")
Albert_face_encoding = face_recognition.face_encodings(Albert_image)[0]

# Load a second sample picture and learn how to recognize it.
Steven_image = face_recognition.load_image_file("Dataset/Steven Hawking.jpg")
Steven_face_encoding = face_recognition.face_encodings(Steven_image)[0]

Elon_image = face_recognition.load_image_file("Dataset/Elon Musk.jpg")
Elon_face_encoding = face_recognition.face_encodings(Elon_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    Albert_face_encoding,
    Steven_face_encoding,
    Elon_face_encoding,
]
known_face_names = [
    "Albert Einstein",
    "Steven Hawking",
    "Elon Musk"
]

while True:        
    ret, frame = video_captuer.read()    
    rgb_frame = frame[:, :, ::-1]    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown person"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
        cv2.rectangle(frame, (left,bottom - 35), (right, bottom), (0,0,255),cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255,255,255), 1)
        if (name != "Unknown person"):
            print(name, " was here")
        
        
    cv2.imshow('Video',frame)
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
video_captuer.release()
cv2.destroyAllWindows()

