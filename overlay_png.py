import cv2
import cvzone

cap = cv2.VideoCapture(0)

img_png = cvzone.downloadImageFromUrl(
    url="https://github.com/cvzone/cvzone/blob/master/Results/cvzoneLogo.png?raw=true",
    keepTransparency=True
)

while True:
    success, img = cap.read()
    img_overlay = cvzone.overlayPNG(img, img_png, pos=[200, 300])

    cv2.imshow("Image Overlay", img_overlay)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break