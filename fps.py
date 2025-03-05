import cv2
from cvzone.FPS import FPS

fps_reader = FPS(avgCount=30)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    success, img = cap.read()

    fps, img = fps_reader.update(img, pos=(20, 50), bgColor=(250, 196, 2), textColor=(255, 255, 255), scale=3, thickness=3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
