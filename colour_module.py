import cv2
import cvzone
from cvzone.ColorModule import ColorFinder


colour_finder = ColorFinder(trackBar=True)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

hsv_values = {
    "hmin": 10, "smin": 55, "vmin": 215,
    "hmax": 42, "smax": 255, "vmax": 255,
}

while True:
    success, img = cap.read()
    
    img_orange, mask = colour_finder.update(img, hsv_values)
    img_stack = cvzone.stackImages([img, img_orange, mask], 3, 1)

    cv2.imshow("Image Stack", img_stack)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
