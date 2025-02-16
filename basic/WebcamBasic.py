import cv2
import matplotlib.pyplot as plt

# Open the webcam
cap = cv2.VideoCapture(0) # 0 is the default camera, for external cameras use 1, 2, 3, etc.

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    ret, fram = cap.read()
    if not ret:     # ret -> return value, if it is false, then the frame is not read properly
        print("Error: Could not read frame.")
        break
    cv2.imshow("Webcam", fram) # Here "Webcam" is the name of the window

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to exit
        """
            cv2.waitKey(1) -> waits for 1 millisecond for the user to press a key
            0xFF -> 8 bits of 1
            ord('q') -> ASCII value of 'q'

            So, if the user presses 'q', then the loop will break

            actually cv2.waitKey(1) itself gives 113 in today's date, so we can directly compare it with 113
            but older versions of OpenCV may give 32 bit integer, so it is better to use 0xFF
        """
        break

cap.release() # Release the webcam
cv2.destroyAllWindows() # Close the window 