import cv2
from sys import argv
import cli
import filters

if __name__ == "__main__":
    args = cli(argv)
    if args[0] == -1:
        exit(1)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    video = cv2.VideoCapture(0)
    x, y, w, h = 0, 0, 0, 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        if len(face) != 0:
            fin = [x, y, w, h]
            for i in range(4):
                if abs(fin[i] - face[0][i]) > 20:
                    fin[i] = face[0][i]
            x, y, w, h = fin
        if args[0] == 0:
            frame = filters.gaussian(frame, x, y, w, h)
        elif args[0] == 1:
            frame = filters.pixelate(frame, x, y, w, h)
        elif args[0] == 2:
            frame = filters.blackout(frame, x, y, w, h)
        cv2.imshow("Anonymize", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
