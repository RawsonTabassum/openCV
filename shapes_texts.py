import cv2 as cv
import numpy as np

black = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', black)

# create green image
# black[:] = 0, 255, 0
# cv.imshow('green', black)


# for red, 0, 0, 255
# for blue 255, 0, 0
# so the channels are blue green red

# draw a blue square in the black image
# black[200:300, 200:300] = 255, 0, 0
# cv.imshow('blue', black)

# draw a rectangle using cv.rectangle
# cv.rectangle(black, (10, 10), (200, 100), (0, 255, 0), thickness=cv.FILLED)
# (200, 100) means width, height
# thickness = positive int value = just a line with lineWidth
# thickness = -1 or cv.FILLED = fills in the shape
# cv.imshow('rect', black)


# draw a circle
# function arguments = image, center, radius, color, lineWIdth/fill
cv.circle(black, (black.shape[0]//2, black.shape[1]//2),
          40, (0, 0, 255), thickness=cv.FILLED)

# draw a line
# arguments = image, start point, end point, color, thickness
cv.line(black, (100, 100), (100, 500), (255, 0, 0), thickness=2)

# display text on image
# function arguments = image, text, start point, font, scaling value, color, thickness
cv.putText(black, "Yuki", (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0,
           (255, 255, 255), 2)
cv.imshow('circle', black)
cv.waitKey(0)
