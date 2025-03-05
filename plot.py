import cv2
import cvzone
from cvzone.PlotModule import LivePlot
from cvzone.FaceDetectionModule import FaceDetector
import math


cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85, modelSelection=0)

x_plot = LivePlot(w=1200, yLimit=[0, 500], interval=0.01)
sin_plot = LivePlot(w=1200, yLimit=[-100, 100], interval=0.01)
x_sin = 0


while True:
    success, img = cap.read()

    img, bounding_boxes = detector.findFaces(img, draw=False)
    val = 0

    if bounding_boxes:
        for bounding_box in bounding_boxes:
            centre = bounding_box["center"]
            x, y, w, h = bounding_box["bbox"]
            score = int(bounding_box["score"][0] * 100)
            val = centre[0]

            cv2.circle(img, centre, 5, (250, 195, 2), cv2.FILLED)
            cvzone.putTextRect(img, f"{score}%", (x, y - 10))
            cvzone.cornerRect(img, (x, y, w, h))

    x_sin += 1
    if x_sin == 360:
        x_sin = 0
    img_plot_sin = sin_plot.update(int(math.sin(math.radians(x_sin)) * 100))
    img_plot = x_plot.update(val)

    cv2.imshow("Image Plot", img_plot)
    cv2.imshow("Image Sin Plot", img_plot_sin)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break