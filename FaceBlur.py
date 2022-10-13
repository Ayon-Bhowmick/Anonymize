import cv2
from sys import argv

if __name__ == "__main__":

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
            nx, ny, nw, nh = face[0]
            if abs(nx - x) > 20:
                x = nx
            if abs(ny - y) > 20:
                y = ny
            if abs(nw - w) > 20:
                w = nw
            if abs(nh - h) > 20:
                h = nh
        frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w], (99, 99), 30)
        cv2.imshow("FaceBlur", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
