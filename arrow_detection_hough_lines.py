import cv2, numpy as np, argparse

import serial
ser = serial.Serial('COM5', baudrate = 9600, timeout = 1)

r1 = 0
l1 = 0

cap = cv2.VideoCapture(0)
while (True):
    _, img = cap.read()

    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", help = "IMG_3776.jpg")
    # args = vars(ap.parse_args())
    #convert the image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #apply canny edge detection to the image
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    #show what the image looks like after the application of previous functions
    cv2.imshow("canny'd image", edges) 
    if cv2.waitKey(1) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
    #perform HoughLines on the image
    lines = cv2.HoughLines(edges,1,np.pi/180,20)
    #create an array for each direction, where array[0] indicates one of the lines and array[1] indicates the other, which if both > 0 will tell us the orientation
    left = [0, 0]
    right = [0, 0]
 
    #iterate through the lines that the houghlines function returned
    for object in lines:
        theta = object[0][1]
        rho = object[0][0]
        #cases for right/left arrows
        if ((np.round(theta, 2)) >= 1.0 and (np.round(theta, 2)) <= 1.1) or ((np.round(theta,2)) >= 2.0 and (np.round(theta,2)) <= 2.1):
            if (rho >= 20 and rho <=  30):
                left[0] += 1
            elif (rho >= 60 and rho <= 65):
                left[1] +=1
            elif (rho >= -73 and rho <= -57):
                right[0] +=1
            elif (rho >=148 and rho <= 176):
                right[1] +=1

    if left[0] >= 1 and left[1] >= 1:
        print("left")
        r1 = 0
        l1 += 1
        if l1 > 10 :
            break
        
    elif right[0] >= 1 and right[1] >= 1:
        print("right")
        r1 += 1
        l1 = 0
        if r1 > 10 :
            break
        

if r1>l1:
    i = 'r'
    ser.write(i.encode())  

else:
    i = 'l'
    ser.write(i.encode())    


