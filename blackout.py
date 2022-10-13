import cv2
from sys import modules

def blackout(frame, x, y, w, h):
    frame[y:y+h, x:x+w] = 0
    return frame

modules[__name__] = blackout
