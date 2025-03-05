import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_small = cv2.resize(img, (0, 0), None, 0.1, 0.1)
    img_big = cv2.resize(img, (0, 0), None, 3, 3)
    img_canny = cv2.Canny(img_grey, 50, 150)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img_list = [img, img_grey, img_small, img_big, img_canny, img_hsv]

    stacked_img = cvzone.stackImages(img_list, cols=3, scale=0.7)

    cv2.imshow("Stacked Images", stacked_img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break