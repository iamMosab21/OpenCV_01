import cv2 as cv
capture = cv.VideoCapture('Videos/cat.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow('kutti vdo', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()                                            
cv.destroyAllWindows()


#this was my idea.....................................

# cv.VideoCapture('Videos/cat.mp4') returns a pointer, 
# a memroy address of ram where the cpp engine of cv stays. 
# so when we write capture = cv.VideoCapture(vdo address) , 
# we actually fetch the vdo file to the cpp engine and returns the pointer. 
# and later using this pointer , we say go to capture(in the address) 
# and give me the numpy array of the current frame


## AI told me this.........................................................................
# Let's bridge what you already understand with the programming terms so it makes complete sense without needing a full OOP course. 
# In Python, when we say "object," you can think of it exactly like that pointer. 
# The variable capture is just a handle holding the memory address where the C++ engine is running your video.
# The "Go to address and do X" is the Method: In programming, a method is just a function that requires that specific address to work.
#  When you write capture.read(), you are telling Python: "Go to the address stored in capture, find the C++ engine there, and tell it to give me the next frame.
# "Why We Call cv.VideoCapture a Class:
# Think of a Class as a blueprint or a factory.cv.VideoCapture is the factory.
# When you run capture = cv.VideoCapture("video.mp4"), 
# you tell the factory: "Hey, build a new video-reading engine in the RAM for this specific file, and give me its address (capture).
# "A Simple AnalogyImagine a housing developer (the Class):
# You call the developer and say: "Build me a house at 123 Main Street" (capture = cv.VideoCapture("video.mp4")).
# The developer builds it and gives you the keys/address (capture).
# Now, if you want to open the door, you must use that specific address: capture.open_door() (this is the method). 
# You can't just say open_door() into thin air; Python needs to know which house address you are talking about.
# So, your understanding is 100% correct. 
# capture holds the remote control (pointer) to the C++ video engine, and .read() is the button you press on that remote to get your NumPy array.