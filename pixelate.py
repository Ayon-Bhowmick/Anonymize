import cv2
from sys import modules

def pixelate(frame, x, y, w, h):
    pixelated = cv2.resize(frame[y:y+h, x:x+w], (w//10, h//10), interpolation=cv2.INTER_NEAREST)
    pixelated = cv2.resize(pixelated, (w, h), interpolation=cv2.INTER_NEAREST)
    frame[y:y+h, x:x+w] = pixelated
    return frame

modules[__name__] = pixelate
