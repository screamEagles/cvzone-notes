import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation(model=0)

while True:
    success, img = cap.read()

    img_out = segmentor.removeBG(img, imgBg=(250, 196, 2), cutThreshold=0.1)
    img_stacked = cvzone.stackImages([img, img_out], cols=2, scale=1)

    cv2.imshow("Image", img_stacked)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break