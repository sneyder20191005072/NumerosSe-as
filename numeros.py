import cv2
import time
import os
import Manos2 as mn
wCam, hCam = 640, 480

cap= cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "C:\\Users\\giset\\Downloads\\proyecto\\manos"
myList = os.listdir(folderPath)
#print (myList)

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
   # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print( len(overlayList))

pTime =0

detector = mn.handDetector(detectionCon= 0.75)
   
tipIds = [4, 8, 12, 16, 20]

while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)
    dedos=[]
    if len(lmList) !=0:
        
        #Para el pulgar
        if lmList[tipIds[0]][1] > lmList[tipIds[0]- 1][1]:
                dedos.append(1)
        else:
                dedos.append(0)
        #para el resto de dedos

        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                dedos.append(1)
            else:
                dedos.append(0)
        print(dedos)
# para el 1
    if dedos==[0,1,0,0,0]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[0]
       #para el 0
    if dedos==[0,0,0,0,0]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[1]
       # para el 2
    if dedos==[0,1,1,0,0]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[2]
       # para el 3
    if dedos==[1,1,1,0,0]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[3]
       # para el 4
    if dedos==[0,1,1,1,1]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[4]
       # para el 5
    if dedos==[1,1,1,1,1]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[5]
       # para el 6
    if dedos==[0,1,1,1,0]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[6]
       # para el 7
    if dedos==[0,1,1,0,1]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[7]
       # para el 8
    if dedos==[0,1,0,1,1]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[8]
    if dedos==[0,0,1,1,1]:
       h, w, c = overlayList[0].shape
       img[0:h, 0:w] =overlayList[9]








    #h, w, c = overlayList[0].shape
    #img[0:h, 0:w] =overlayList[9]


    cTime = time.time()
    fps = 1/ (cTime-pTime) 
    pTime= cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


