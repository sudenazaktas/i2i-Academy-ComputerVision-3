import cv2

capture= cv2.VideoCapture(0)

while True:
    isRead, frame =capture.read()
    if not isRead:
        break

    cv2.imshow("Webcam Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()