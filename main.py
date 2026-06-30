import cv2
import mediapipe as mp

# MediaPipe setup
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Fingertip landmark IDs: thumb=4, index=8, middle=12, ring=16, pinky=20
TIP_IDS = [4, 8, 12, 16, 20]

capture = cv2.VideoCapture(0)

while True:
    isRead, frame = capture.read()
    if not isRead:
        break

    # Flip frame to remove mirror effect
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB for MediaPipe
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frameRGB)

    fingerCount = 0

    if result.multi_hand_landmarks:
        for handLandmarks in result.multi_hand_landmarks:
            # Draw hand skeleton
            mpDraw.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)

            lm = handLandmarks.landmark
            fingers = []

            # All 5 fingers: open if tip is above its lower joint
            for i in range(5):
                if lm[TIP_IDS[i]].y < lm[TIP_IDS[i] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            fingerCount += fingers.count(1)

    # Display finger count on screen
    cv2.putText(frame, f"Fingers: {fingerCount}", (30, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()