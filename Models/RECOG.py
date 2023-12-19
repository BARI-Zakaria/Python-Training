import face_recognition
import cv2
import numpy
import os
from datetime import datetime

path = "C:\\Users\hp\\Desktop\\statique\\persons"
images = []
classname = []
personlist = os.listdir(path)

for person in personlist:
    curperson = cv2.imread(f"{path}\{person}")
    images.append(curperson)
    classname.append(os.path.splitext(person)[0] )

def findincoding(image):
    incoding = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        incoding.append(encode)
    return incoding

encodelist = findincoding(images)
print(encodelist)

cap = cv2.VideoCapture(0)

# Create a directory to store the screenshots
screenshot_directory = "C:\\Users\hp\\Desktop\\statique\\screenshots"
if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)

while True:
    good, img = cap.read()
    imgs = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    facecurentfarme = face_recognition.face_locations(imgs)
    encodecurentframe = face_recognition.face_encodings(imgs, facecurentfarme)
    
    for encodeface, faceloc in zip(encodecurentframe, facecurentfarme):
        matches = face_recognition.compare_faces(encodelist, encodeface)
        facedis = face_recognition.face_distance(encodelist, encodeface)
        matchindex = numpy.argmin(facedis)
        
        if matches[matchindex]:
            # Recognized face code...
            name = classname[matchindex].upper()
            print(name)
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        else:
            # Unrecognized face code...
            name = "Anonymous"
            print(name)
            
            # Capture screenshot
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_path = os.path.join(screenshot_directory, f"{name}_{timestamp}.jpg")
            cv2.imwrite(screenshot_path, img)
            
            # Draw rectangle and text on the image
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imshow("face recognition", img)
    cv2.waitKey(1)
