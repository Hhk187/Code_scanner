from webcam import Webcam
import cv2

# Define a simple webcam object that will get video stream from webcam (src=0),
#  with a frame width of 640 (auto setting heigth to keep original aspect ratio)
webcam = Webcam(src=0, w=640)
print(f"Frame size: {webcam.w} x {webcam.h}")


for frame in webcam:
    # Show the frames in a cv2 window
    cv2.imshow('Webcam Frame', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break