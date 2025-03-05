import cv2
from cvzone.PoseModule import PoseDetector


cap = cv2.VideoCapture(0)

detector = PoseDetector(staticMode=False, modelComplexity=1, smoothLandmarks=True, enableSegmentation=False, smoothSegmentation=True, detectionCon=0.5, trackCon=0.5)


while True:
    success, img = cap.read()

    img = detector.findPose(img)
    
    landmark_list, bounding_box_info = detector.findPosition(img, draw=True, bboxWithHands=False)
    if landmark_list:
        centre = bounding_box_info["center"]
        cv2.circle(img, centre, 5, (250, 196, 2), cv2.FILLED)
        length, img, info = detector.findDistance(landmark_list[11][0:2], landmark_list[15][0:2], img=img, color=(255, 0, 0), scale=10)

        angle, img = detector.findAngle(landmark_list[11][0:2], landmark_list[13][0:2], landmark_list[15][0:2], img=img, color=(0, 0, 255), scale=10)

        is_close_angle_50 = detector.angleCheck(myAngle=angle, targetAngle=50, offset=10)
        print(is_close_angle_50)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break