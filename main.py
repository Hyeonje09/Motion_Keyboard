from cv2 import FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN
from cvzone.HandTrackingModule import HandDetector
import cv2  
from time import sleep

cap_cam = cv2.VideoCapture(0)

cap_cam.set(3,1280)
cap_cam.set(4, 720)

detector = HandDetector(maxHands = 2, detectionCon = 1)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B","N", "M", ",", ".", "/"]]

finalText = ""

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(cam_img, button.pos, (x + w, y + h), (255,0,255),cv2.FILLED)
        cv2.putText(cam_img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4) 
    return img

class button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(button([100 * j + 50, 100 * i + 50], key))

while True:
    sucess, cam_img = cap_cam.read()
    cam_img = detector.findHands(cam_img)
    lm_list, bboxInfo = detector.findPosition(cam_img)
    #cam_img = cv2.flip(cam_img, 1)
    cam_img = drawAll(cam_img, buttonList)

    if lm_list:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lm_list[8][0] < x + w and y < lm_list[8][1] < y + h:
                cv2.rectangle(cam_img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
                cv2.putText(cam_img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4) 
                
                l,_,_ = detector.findDistance(8, 12, cam_img, draw = False)
                print(l)

                if l < 30:
                    cv2.rectangle(cam_img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(cam_img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                    finalText += button.text
                    sleep(0.15)

    cv2.rectangle(cam_img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(cam_img, finalText, (60, 430), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5) 

    cv2.imshow("image", cam_img)
    if cv2.waitKey(1) == ord('q'): 
        break