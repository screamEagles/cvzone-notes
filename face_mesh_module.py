import cv2
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0)

detector = FaceMeshDetector(staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5)

while True:
    success, img = cap.read()

    img, faces = detector.findFaceMesh(img, draw=True)
    if faces:
        for face in faces:
            left_eye_up_point = face[159]
            left_eye_down_point = face[23]

            left_eye_vertical_distance, info = detector.findDistance(left_eye_up_point, left_eye_down_point)

            print(left_eye_vertical_distance)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break