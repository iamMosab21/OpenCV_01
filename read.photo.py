import cv2 as cv

img = cv.imread('Photos/cat.jpg')

if img is None:
    print("Error: Could not read the img. Please check the file path")
else:
    cv.imshow('cat', img)

    key = cv.waitKey(0) & 0xFF
    if key == ord('q'):
        print("Closing window.")
    elif key == ord('s'):
        print("Saving copy of the image.")
        cv.imwrite('Photos/cat_copy.jpg', img)
    else:
        print(f"Key with ASCII code {key} was pressed.")

    cv.destroyAllWindows()


#  What  cv.waitKey()  Does  ..................................................................................................................                                                                                                                                                                                                                                                                                                    
#  The  cv.waitKey(delay)  function serves two main purposes in OpenCV:                                                                                                                                                                                                                                                                  
#   1. Waits for Keyboard Input: It pauses execution and waits for a keyboard event for the specified  delay  in milliseconds.                                            
#       • If  delay  is  0  (like in your  read_photo.py  script) or negative, it waits infinitely until any key is pressed.                                              
#       • If  delay  is greater than  0  (e.g.,  30 ), it waits for that many milliseconds. If no key is pressed within that time, execution continues. This is commonly  
#       used in video playback loops.                                                                                                                                     
#   2. Updates the GUI: It handles high-level GUI window events, such as redrawing the window, updating the image display, and handling window resizing. Without calling  
#   cv.waitKey() , OpenCV windows will not display images properly and may freeze.                                                                                        
#   ──────                                                                                                                                                                
#   ### Handling Specific Keys and Actions                                                                                                                                
                                                                                                                                                                        
#   The function returns the integer ASCII value of the key that was pressed. If the delay time expires without any keypress, it returns  -1 .                            
                                                                                                                                                                        
#   To define actions for specific keys, you capture the returned value and compare it using Python's built-in  ord()  function or specific ASCII integer codes.          
                                                                                                                                                                        
#   #### Cross-Platform Compatibility Recommendation                                                                                                                      
                                                                                                                                                                        
#   On some 64-bit systems, the return value of  cv.waitKey()  may contain bits outside the 8-bit ASCII range. To ensure compatibility across different operating systems,
#   use a bitwise AND operator with hexadecimal  0xFF :                                                                                                                   
                                                                                                                                                                        
#   key = cv.waitKey(0) & 0xFF 
# 0xFF filters out system noise from cv.waitKey() to leave only the clean ASCII value