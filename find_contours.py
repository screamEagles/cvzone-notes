import cv2
import cvzone
import numpy as np


img_shapes = cvzone.downloadImageFromUrl(url="https://github.com/cvzone/cvzone/blob/master/Results/shapes.png?raw=true")

img_canny = cv2.Canny(img_shapes, 50, 150)
img_dilated = cv2.dilate(img_canny, np.ones((5, 5), np.uint8), iterations=1)

img_countours, contours_found = cvzone.findContours(img_shapes, img_dilated, minArea=1000, maxArea=100000, sort=True, filter=None, drawCon=True, c=(255, 0, 0), ct=(250, 196, 2), retrType=cv2.RETR_EXTERNAL, approxType=cv2.CHAIN_APPROX_NONE)

# filter in terms of corner point. in this case, shapes with 3 and 4 corner points are detected
img_countours_filtered, contours_found_filtered = cvzone.findContours(img_shapes, img_dilated, minArea=1000, maxArea=100000, sort=True, filter=[3, 4], drawCon=True, c=(255, 0, 0), ct=(250, 196, 2), retrType=cv2.RETR_EXTERNAL, approxType=cv2.CHAIN_APPROX_NONE)

cv2.imshow("Image Contours", img_countours)
cv2.imshow("Image Contours Filtered", img_countours_filtered)

cv2.waitKey(0)