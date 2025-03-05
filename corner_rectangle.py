import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    cvzone.cornerRect(img, (200, 200, 300, 200), l=30, t=5, rt=2,
               colorR=(250, 196, 2), colorC=(98, 245, 98))

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break