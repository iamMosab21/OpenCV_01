import cv2 as cv

capture = cv.VideoCapture(0)

# 3 is the property ID for width, 4 is for height
capture.set(3, 1920) # Set width to 1920
capture.set(4, 1080) # Set height to 1080

while True:
    ret, frame = capture.read()
    if not ret:
        break
        
    cv.imshow('Live Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# Whether you are upscaling or downscaling,
# depends entirely on your webcam's hardware-native resolution.
# Here is exactly how OpenCV handles this under the hood:
# 
# 1. No Interpolation is Happening in Python
# You do not need an interpolation algorithm (like cv.INTER_AREA or cv.INTER_LINEAR) 
# because OpenCV is not resizing the frames.
# Instead, capture.set(3, 1920) talks directly to your webcam hardware driver.
#  It tells the camera: "Please switch your internal sensor stream mode to 1920x1080.
# "The webcam sensor itself changes how it captures the light.
# The frames arriving at capture.read() are already natively that size.