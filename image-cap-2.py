# Source - https://stackoverflow.com/a
# Posted by Ahmet
# Retrieved 2026-01-23, License - CC BY-SA 4.0

import cv2

frameWidth = 640
frameHeight = 480

# camera selection
# if iphone is on and connected to wifi, then 0 goes to the iphone
# and 1 goes to the macbook.
#
# if phone is NOT avail, then 0 goes to macbook camera and 1 does not work

cap = cv2.VideoCapture(0,cv2.CAP_AVFOUNDATION)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while cap.isOpened():
    success, img = cap.read()
    if success:
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
