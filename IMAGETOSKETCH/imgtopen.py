import cv2

image=cv2.imread("INTERNSHIPS/LGM/messi.jpg")
# cv2.imshow("GOAT" ,image)
# cv2.waitKey(0)

gimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("GOAT" ,gimg)
# cv2.waitKey(0)

invimg=255-gimg
# cv2.imshow("GOAT" ,invimg)
# cv2.waitKey(0)

blurimg=cv2.GaussianBlur(invimg,(21,21),0)
# cv2.imshow("GOAT" ,blurimg)
# cv2.waitKey(0)

invblur=255-blurimg
sketch=cv2.divide(gimg,invblur,scale=256)
cv2.convertScaleAbs(sketch,10,0)
cv2.imshow("GOAT" ,sketch)
cv2.waitKey(0)