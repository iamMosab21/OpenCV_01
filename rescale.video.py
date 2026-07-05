import cv2 as cv

def rescaleFrame(frame, scale):
    # Images, videos, Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =  (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/cat.mp4')

while True:
    isTrue, frame = capture.read()
    
    if not isTrue:
        print("video Ended")
        break
    
    #When you pass frame into your rescaling function, 
    #you are passing a NumPy array. 
    # "Image" is simply the conceptual name for what that array represents.

    cv.imshow('Original', frame)

    resized_img = rescaleFrame(frame, scale=0.20)
    cv.imshow('Resized', resized_img)
    cv.waitKey(10)

capture.release()
cv.destroyAllWindows()