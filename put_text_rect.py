import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cvzone.putTextRect(img, "Pyro Vision", (200, 300), scale=3, thickness=3, colorT=(255, 255, 255), colorR=(250, 196, 2), font=cv2.FONT_HERSHEY_PLAIN, offset=10, border=2, colorB=(0, 0, 0))

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break