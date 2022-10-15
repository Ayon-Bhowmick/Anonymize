import cv2
import numpy

def gaussian(frame, x, y, w, h) -> numpy.ndarray:
    W = w // 3
    H = h // 3
    if W % 2 == 0:
        W += 1
    if H % 2 == 0:
        H += 1
    frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w], (W, H), 30)
    return frame

def pixelate(frame, x, y, w, h) -> numpy.ndarray:
    pixelated = cv2.resize(frame[y:y+h, x:x+w], (w//10, h//10), interpolation=cv2.INTER_NEAREST)
    pixelated = cv2.resize(pixelated, (w, h), interpolation=cv2.INTER_NEAREST)
    frame[y:y+h, x:x+w] = pixelated
    return frame

def blackout(frame, x, y, w, h):
    frame[y:y+h, x:x+w] = 0
    return frame
