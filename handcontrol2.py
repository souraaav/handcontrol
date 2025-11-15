import cv2
import mediapipe as mp
import pyautogui

# Initialize
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
hand_detector = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip for mirror view
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand_detector.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get index finger tip (landmark 8)
            index_x = int(hand_landmarks.landmark[8].x * w)
            index_y = int(hand_landmarks.landmark[8].y * h)

            # Get thumb tip (landmark 4)
            thumb_x = int(hand_landmarks.landmark[4].x * w)
            thumb_y = int(hand_landmarks.landmark[4].y * h)

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Move mouse
            mouse_x = int(screen_width / w * index_x)
            mouse_y = int(screen_height / h * index_y)
            pyautogui.moveTo(mouse_x, mouse_y)

            # Detect click
            distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
            if distance < 30:
                pyautogui.click()
                pyautogui.sleep(0.2)

    cv2.imshow("Hand Mouse Controller", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
