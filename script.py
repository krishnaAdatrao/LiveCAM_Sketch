# pip install tk
# pip install opencv-python
import cv2
import numpy as np
import tkinter as tk

# Our sketch generating function
def sketch(image):
    if image is None:
        return None
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 20, 50)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

def start_camera():
    # Initialize webcam, cap is the object provided by VideoCapture
    # It contains a boolean indicating if it was sucessful (ret)
    # It also contains the images collected from the webcam (frame)
    global cap
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Our Live Sketcher', sketch(frame))
        if cv2.waitKey(1) == ord('q'): # Press 'q' to quit
            break
        
    # Release camera and close windows
    cap.release()
    cv2.destroyAllWindows() 
        
def stop_camera():
    # Release camera and close windows
    cap.release()
    cv2.destroyAllWindows()

# Create tkinter window
root = tk.Tk()
root.title("Live Sketching")
root.geometry("500x500")

# Create start and stop buttons
start_button = tk.Button(root, text="Start", command=start_camera)
stop_button = tk.Button(root, text="Stop", command=stop_camera)

# Add buttons to window
start_button.pack(side="left", padx=20, pady=20)
stop_button.pack(side="right", padx=20, pady=20)

# Show window
root.mainloop()
