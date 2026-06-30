import cv2
import mediapipe as mp

# MediaPipe setup
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)

while True:
    isRead, frame = capture.read()
    if not isRead:
        break

    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frameRGB)

    if result.multi_hand_landmarks:
        for handLandmarks in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()