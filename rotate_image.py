import cv2
from cvzone.Utils import rotateImage

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    img_rotate_60 = rotateImage(img, 60, scale=1, keepSize=False)
    img_rotate_60_keep_size = rotateImage(img, 60, scale=1, keepSize=True)

    cv2.imshow("Image Rotated", img_rotate_60)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break