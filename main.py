from cv2 import FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN
from cvzone.HandTrackingModule import HandDetector
import cv2  

cap_cam = cv2.VideoCapture(0)

cap_cam.set(3,1280)
cap_cam.set(4, 720)

detector = HandDetector(maxHands = 2, detectionCon = 1)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B","N", "M", ",", ".", "/"]]

class button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

        x, y = self.pos
        w, h = self.size
        cv2.rectangle(cam_img, self.pos, (x + w, y + h), (255,0,255),cv2.FILLED)
        cv2.putText(cam_img, self.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4) 

buttonList = []

while True:
    sucess, cam_img = cap_cam.read()
    cam_img = detector.findHands(cam_img)
    lm_list, bboxInfo = detector.findPosition(cam_img)

    cam_img = cv2.flip(cam_img, 1)
 
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(button([100 * j + 50, 100 * i + 50], key))
    
    cv2.imshow("image", cam_img)
    if cv2.waitKey(1) == ord('q'): 
        break