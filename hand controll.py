import cv2
import mediapipe as mp
import screen_brightness_control as sbc  # Add this import
import time  # Add this import

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

# Add brightness control variables
last_brightness_change = 0
brightness_cooldown = 0.5  # Seconds between brightness changes

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands, mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.5) as face_detection:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_height, image_width = image.shape[:2]
        image.flags.writeable = False

        face_results = face_detection.process(image)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if face_results and face_results.detections:
            for detection in face_results.detections:
                bbox = detection.location_data.relative_bounding_box
                x_min = int(bbox.xmin * image_width)
                y_min = int(bbox.ymin * image_height)
                box_w = int(bbox.width * image_width)
                box_h = int(bbox.height * image_height)

                x1 = max(0, x_min)
                y1 = max(0, y_min)
                x2 = min(image_width, x1 + max(1, box_w))
                y2 = min(image_height, y1 + max(1, box_h))

                if x2 <= x1 or y2 <= y1:
                    continue

                face_roi = image[y1:y2, x1:x2]
                min_side = max(1, min(box_w, box_h))
                k = (min_side // 2) | 1
                k = max(15, k)
                k = min(k, 101)
                blurred = cv2.GaussianBlur(face_roi, (k, k), 0)
                blurred = cv2.GaussianBlur(blurred, (k, k), 0)
                image[y1:y2, x1:x2] = blurred

        hand_states = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                lm = hand_landmarks.landmark
                tips = [8, 12, 16, 20]
                pips = [6, 10, 14, 18]
                extended_count = 0
                for tip_idx, pip_idx in zip(tips, pips):
                    try:
                        if lm[tip_idx].y < lm[pip_idx].y:
                            extended_count += 1
                    except Exception:
                        pass

                state = "Opened" if extended_count >= 3 else "Closed"
                
                # Add brightness control logic
                current_time = time.time()
                if current_time - last_brightness_change >= brightness_cooldown:
                    current_brightness = sbc.get_brightness()[0]
                    if state == "Opened" and current_brightness < 100:
                        sbc.set_brightness(min(current_brightness + 5, 100))
                        last_brightness_change = current_time
                    elif state == "Closed" and current_brightness > 0:
                        sbc.set_brightness(max(current_brightness - 5, 0))
                        last_brightness_change = current_time

                wrist_x = lm[0].x
                wrist_y = lm[0].y
                hand_states.append((state, wrist_x, wrist_y))
        else:
            hand_states = []

        image = cv2.flip(image, 1)

        for idx, (state, wrist_x_norm, wrist_y_norm) in enumerate(hand_states):
            wrist_x = int(wrist_x_norm * image_width)
            wrist_y = int(wrist_y_norm * image_height)
            wrist_x_flipped = image_width - wrist_x
            text_pos = (wrist_x_flipped - 20, max(30, wrist_y - 30 - 30 * idx))
            color = (0, 255, 0) if state == "Opened" else (0, 0, 255)
            cv2.putText(image, state, text_pos, cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2, cv2.LINE_AA)

        cv2.imshow('Hand Tracking (faces blurred)', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()