import sys,os,numpy as np 
from cv2 import cv2

#creating he directories stracture if they are not exist
if not os.path.exists("data"):
    os.mkdir("data")
    os.mkdir("data/w")
    os.mkdir("data/s")
    os.mkdir("data/a")
    os.mkdir("data/d")


#Creating camra instances
cap = cv2.VideoCapture(0)

#Retrivng continous frame
while True:
    #Reading the camra frame
    _,frame = cap.read()

    #counting the no of images saved
    count = {   "W":len(os.listdir("data/w")),
                "S":len(os.listdir("data/s")),
                "A":len(os.listdir("data/a")),
                "D":len(os.listdir("data/d"))   
            }    
    #Showing the frame
    cv2.imshow("frame",frame)

    interrupt =  cv2.waitKey(10)
    if interrupt & 0xFF == 27:#(esc_key)
        break
    elif interrupt & 0xFF == ord("w"):
        cv2.imwrite("data/w/"+str(count["W"])+".jpg",frame)
    elif interrupt & 0xFF == ord("s"):
        cv2.imwrite("data/s/"+str(count["S"])+".jpg",frame)
    elif interrupt & 0xFF == ord("w"):
        cv2.imwrite("data/a/"+str(count["A"])+".jpg",frame)
    elif interrupt & 0xFF == ord("w"):
        cv2.imwrite("data/d/"+str(count["d"])+".jpg",frame)
    
cap.release()
cv2.destroyAllWindows()







