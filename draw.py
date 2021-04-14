import cv2 as cv
import numpy as np

#creating a blank image
blankImg = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank Image', blankImg)

#putting the color in blank img
blankImg[:] = 56,25,100
cv.imshow('Colored Blank Image', blankImg)

#putting the color to certain range of pixels in blank img
blankImg[100:200, 300:400] = 56,25,100
cv.imshow('Colored Blank Image', blankImg)

#create a rectangle box in blank img
cv.rectangle(blankImg, (1,4),(20,20,20),thickness=2, lineType=cv.LINE_AA)
cv.imshow('Rectangle', blankImg)

img = cv.imread('Photos/b1.jpg')
cv.imshow('Baby Girl', img)

cv.waitKey(0)