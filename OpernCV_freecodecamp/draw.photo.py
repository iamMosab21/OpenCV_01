import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #uint8 is the datatype of image.
cv.imshow('Blank', blank)

# #1.Paint the image a certain colour
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green', blank)

# # 2.Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=1 )
# cv.imshow('Rectangle', blank)

# # Draw a FILLED rectangle
# cv.rectangle(blank, (0,0), (255,500), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Filled Rectangle', blank);

# # Draw filled rectangle differently
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,255), thickness=-1)
# # For a 500x500 image, blank.shape[1] simply means 500
# # thickness=-1 means the shape will be completely filled in with color
# # the built-in OpenCV constant cv2.FILLED, which has a value of -1 behind the scenes
# # The double slash // represents floor division (or integer division) in Python.
# cv.imshow('Diff Rec', blank)

# # 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,255), thickness=2)
cv.imshow('Circle', blank)

# # 4. Draw a line
cv.line(blank, (250,0), (250,500), (255,0,0), thickness=2)
cv.imshow('line', blank)


# 5. writing TEXT on the image
cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,255,255), thickness=2)
cv.imshow('Text', blank)


# In Python, np.zeros is a function in the NumPy library 
# used to create a new array filled entirely with zeros
# *The function's signature is np.zeros(shape, dtype=float)


cv.waitKey(0)









