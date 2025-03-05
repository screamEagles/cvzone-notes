import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)

detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

while True:
    success, img = cap.read()

    hands, img = detector.findHands(img, draw=True, flipType=True)
    if hands:
        hand1 = hands[0]
        landmark_list1 = hand1["lmList"]
        bounding_box1 = hand1["bbox"]
        centre1 = hand1["center"]
        hand_type1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)
        print(f"H1 = {fingers1.count(1)}", end=" ")
        length, info, img = detector.findDistance(landmark_list1[8][0:2], landmark_list1[12][0:2], img, color=(250, 196, 2), scale=10)

        if len(hands) == 2:
            hand2 = hands[1]
            landmark_list2 = hand2["lmList"]
            bounding_box2 = hand2["bbox"]
            centre2 = hand2["center"]
            hand_type2 = hand2["type"]

            fingers2 = detector.fingersUp(hand2)
            print(f"H2 = {fingers2.count(1)}", end=" ")
            length, info, img = detector.findDistance(landmark_list2[8][0:2], landmark_list2[12][0:2], img, color=(250, 196, 2), scale=10)
        
        print(" ")
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break