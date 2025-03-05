import cv2
import cvzone

img_normal = cvzone.downloadImageFromUrl(url="https://github.com/cvzone/cvzone/blob/master/Results/shapes.png?raw=true")

img_png = cvzone.downloadImageFromUrl(url="https://github.com/cvzone/cvzone/blob/master/Results/cvzoneLogo.png?raw=true", keepTransparency=True)

img_png = cv2.resize(img_png, (0, 0), None, 3, 3)

cv2.imshow("Image Normal", img_normal)
cv2.imshow("Image PNG", img_png)
cv2.waitKey(0)