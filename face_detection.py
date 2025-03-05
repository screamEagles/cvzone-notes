import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)

detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

while True:
    success, img = cap.read()

    img, bounding_boxes = detector.findFaces(img, draw=False)

    if bounding_boxes:
        for bounding_box in bounding_boxes:
            centre = bounding_box["center"]
            x, y, width, height = bounding_box["bbox"]
            score = int(bounding_box["score"][0] * 100)

            cv2.circle(img, centre, 5, (250, 196, 2), cv2.FILLED)
            cvzone.putTextRect(img, f"{score}%", (x, y - 10), colorR=(250, 196, 2))
            cvzone.cornerRect(img, (x, y, width, height), colorR=(250, 196, 2))

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break