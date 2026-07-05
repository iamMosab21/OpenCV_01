import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.75):
    width  = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame , dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Billi', resized_img)

cv.waitKey(0)
cv.destroyAllWindows()  


# * cv.resize returns a new NumPy array (ndarray) representing the resized image




# * When OpenCV downscales an image, it uses mathematical interpolation algorithms.
# Since a smaller grid has less space, the algorithm mathematically combines
# the original Blue, Green, and Red (BGR) values of multiple pixels into single, representative BGR values for the smaller output.
# OpenCV relies on different interpolation methods to do this:
       
# *                  1. cv2.INTER_AREA (Best for Downscaling)


#  In Python, almost everything is an object (similar to a struct pointer in C). You access its fields or methods using the dot  .  operator
# *   (e.g.,  object.attribute  instead of  object->attribute ).





# The  shape  attribute on a frame is a tuple (a read-only fixed-size array). In C terms, you can think of it as a struct:                                           
                                                                                                                                                                     
#     struct Shape {                                                                                                                                                   
#         int height;   // index 0                                                                                                                                     
#         int width;    // index 1                                                                                                                                     
#         int channels; // index 2 (usually 3 for BGR color)                                                                                                           
#     };                                                                                                                                                               
                                                                                                                                                                     
#   So:                                                                                                                                                                
                                                                                                                                                                     
# *  •  frame.shape[0]  returns the Height of the frame (number of rows).                                                                                               
# *  •  frame.shape[1]  returns the Width of the frame (number of columns).                                                                                             
#    •  frame.shape[2]  returns the number of Color Channels (typically 3: Blue, Green, Red).




