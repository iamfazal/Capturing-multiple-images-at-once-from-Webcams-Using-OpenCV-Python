import os
import cv2
import threading
from datetime import datetime

class camThread(threading.Thread):
    def __init__(self, previewName, webcamNumber):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.webcamNumber = webcamNumber
    def run(self):
        capture(self.previewName, self.webcamNumber)

def capture(previewName, webcamNumber):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(webcamNumber)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    path = "img/"+str(datetime.now())+str(webcamNumber)+".jpg"
    cv2.imwrite(filename=path, img=frame)
    cam.release()
    cv2.destroyAllWindows()
    print(previewName+" Image saved!")

# Create threads 
thread1 = camThread("Webcam 1", 0)
thread2 = camThread("Webcam 2", 1)
thread3 = camThread("Webcam 3", 2)

path ="./img"

# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)

thread1.start()
thread2.start()
thread3.start()