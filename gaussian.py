from cv2 import GaussianBlur
from sys import modules

def gaussian(frame, x, y, w, h):
    W = w // 3
    H = h // 3
    if W % 2 == 0:
        W += 1
    if H % 2 == 0:
        H += 1
    frame[y:y+h, x:x+w] = GaussianBlur(frame[y:y+h, x:x+w], (W, H), 30)
    return frame

modules[__name__] = gaussian
