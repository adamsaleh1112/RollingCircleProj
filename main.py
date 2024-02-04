# IMPORT NUMPY, CV2, AND CIRCLE DETECT
import numpy # importing numpy, an array library that allows video data to be stored in arrays
import cv2 # importing opencv-python, an image processing library that allows functions such as blur, cropping, etc.
from circledetector import circle_detector # importing circle detector function in circledetector.py

# VIDEO = CAN.MP4
vc = cv2.VideoCapture("RC.mp4")  # loads video

# CIRCLE_DETECT():
circle_detector(vc, "Circle Video Detection Test", 260, 1000) # runs circle detector function in circledetector.py