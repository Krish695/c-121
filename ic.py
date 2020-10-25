import cv2
import time
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avt',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)

time.sleep(3)
count=0
background=0

for i in range(60):
    ret,background=cap.read()
background=np.flip(background,axis=1)

while (cap.isOpened()):
    ret.img=cap.read()
    if not ret:
        break
    count+=1
    img=np.flip(img,axis=1)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red=np.array([10,121,50])
    upper_red=np.array([10,252,252])
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    
    lower_red=np.array([170,120,170])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)

    mask1= mask1+mask2
    mask1=cv2.morphologyEX(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEX(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask2 = cv2.bitwise_not(mask1)

    res1=cv2.bitwise_and(img,img,mask=mask2)

    res2=cv2.bitwise_and(background,background,mask=mask1)

    finaloutput=cv2.addWeighted(res1,1,res2,1,0)
    
    out.write(finaloutput)

    cv2.imshow("magic",finaloutput)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
