import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img_resized = rescaleFrame(img)
cv.imshow('cat_resized', img_resized)

cv.waitKey(0)
