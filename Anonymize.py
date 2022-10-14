import cv2
from sys import argv
from modules import *

if __name__ == "__main__":
    args = cli(argv)
    if args[0] == -1:
        exit(1)
    if args[0] == 0:
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    elif args[0] == 1:
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    video = cv2.VideoCapture(0)
    x, y, w, h = 0, 0, 0, 0
    while True:
        ret, frame = video.read()
        if not ret:
            print("Camera not found")
            break
        if args[0] == 0:
            x, y, w, h = detection.face(cascade, frame, x, y, w, h)
        elif args[0] == 1:
            x, y, w, h = detection.eyes(cascade, frame, x, y, w, h)
        if (x, y, w, h) != (0, 0, 0, 0):
            if args[1] == 0:
                frame = filters.gaussian(frame, x, y, w, h)
            elif args[1] == 1:
                frame = filters.pixelate(frame, x, y, w, h)
            elif args[1] == 2:
                frame = filters.blackout(frame, x, y, w, h)
        else:
            find = "Face" if args[0] == 0 else "Eyes"
            frame = cv2.putText(frame, f"{find} not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        if args[2] == 0:
            cv2.imshow("Anonymize", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
