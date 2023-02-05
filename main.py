import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np

width,height=1280,720

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

folderPath='slides'
pathImages=sorted(os.listdir(folderPath),key=len)
print(pathImages)


# Variables
imgNumber=0
factor=1
slideChangeDelay=0.5
gestureThreshold=height
brushThickness=12


hs,ws=int(120*factor),int(213*factor)
buttonPressed=False
pTime=0
anntotations=[]
annotationNumber=-1
annonationStart=False
annotationDict={}

for i in range(len(pathImages)):
    annotationDict[i]=[]

# Hand Detector
detector=HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)

    pathFullImage=os.path.join(folderPath,pathImages[imgNumber])
    imgCurrent=cv2.imread(pathFullImage)

    hands, img=detector.findHands(img)
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)


    if hands and buttonPressed==False:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        lmList=hand['lmList']

        xVal=int(np.interp(lmList[8][0],[width//2,width-70],[0,width]))
        yVal=int(np.interp(lmList[8][1],[150,height-250],[0,height]))
        indexFinger=xVal,yVal

        if cy<=gestureThreshold:
            #Gesture-1
            if fingers==[1,0,0,0,0]:
                print('Left')
                if imgNumber>0:
                    imgNumber-=1

                    
                    annotationNumber=len(annotationDict[imgNumber])-1
                    annonationStart=False

                    buttonPressed=True
                    pTime=time.time()
            elif fingers==[0,0,0,0,1]:
                print('Right')
                if imgNumber<len(pathImages)-1:
                    imgNumber+=1

                    
                    annotationNumber=len(annotationDict[imgNumber])-1
                    annonationStart=False

                    buttonPressed=True
                    pTime=time.time()
        
        if fingers==[0,1,1,0,0]:
            cv2.circle(imgCurrent,indexFinger,brushThickness,(0,0,255),cv2.FILLED)
            annonationStart=False
        
        elif fingers==[0,1,0,0,0]:
            if annonationStart==False:
                annonationStart=True
                annotationNumber+=1
                annotationDict[imgNumber].append([])
            cv2.circle(imgCurrent,indexFinger,brushThickness,(0,0,255),cv2.FILLED)
            annotationDict[imgNumber][annotationNumber].append(indexFinger)
        else:
            annonationStart=False
        
        if fingers==[0,1,1,1,0]:
            if annotationDict[imgNumber]:
                if annotationNumber > -1:
                    annotationDict[imgNumber].pop(-1)
                    annotationNumber-=1
                    
                    buttonPressed=True
                    pTime=time.time()
        
        #print(len(anntotations),annonationStart)
        
    if (time.time()-pTime)>slideChangeDelay:
        buttonPressed=False
    
    for i in range(len(annotationDict[imgNumber])):
        for j in range(len(annotationDict[imgNumber][i])):
            if j!=0:
                cv2.line(imgCurrent,annotationDict[imgNumber][i][j-1],annotationDict[imgNumber][i][j],(0,255,255),brushThickness)

    imgSmall=cv2.resize(img,(ws,hs))
    h,w,c=imgCurrent.shape
    imgCurrent[0:hs,w-ws:w]=imgSmall




    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgCurrent)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
  