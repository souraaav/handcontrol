# handcontrol

# ✋ HandControl – Gesture-Based Mouse Controller

HandControl is a Python-based computer vision project that enables users to control their mouse cursor using hand gestures captured via a webcam. By leveraging real-time hand tracking with MediaPipe and OpenCV, this project provides an intuitive, touchless interface for interacting with your computer.

## 🧠 Project Overview

This project transforms your webcam into a virtual mouse controller by detecting hand landmarks and interpreting gestures to move the cursor and perform click actions. It's a fun and practical demonstration of how computer vision and gesture recognition can be used to build interactive systems.

## 📂 File Descriptions

### `HandTrackingModule.py`

This module encapsulates the hand detection and tracking logic using MediaPipe. It provides a reusable class to detect hands and extract landmark positions.

**Key Functions:**

- `findHands(img, draw=True)`: Detects hands in the input image and optionally draws landmarks.
- `findPosition(img, handNo=0, draw=True)`: Returns a list of landmark positions for a specific hand.
- `fingersUp()`: Determines which fingers are raised.
- `findDistance(p1, p2, img, draw=True)`: Calculates the Euclidean distance between two landmarks.

This module abstracts the complexity of MediaPipe and provides a clean interface for gesture-based applications.

---

### `VirtualMouse.py`

This is the main script that uses the `HandTrackingModule` to implement the virtual mouse functionality.

**Key Features:**

- Tracks the index finger to move the mouse cursor.
- Detects pinch gesture (index and middle fingers together) to simulate a mouse click.
- Smoothens cursor movement using interpolation to reduce jitter.
- Maps hand coordinates from the webcam frame to screen coordinates.

**Libraries Used:**

- `cv2` (OpenCV) – for video capture and image processing
- `mediapipe` – for hand landmark detection
- `pyautogui` – to control the mouse
- `numpy` – for numerical operations
- `autopy` – for screen size and mouse control (alternative to pyautogui)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Install dependencies:
  ```bash
  pip install opencv-python mediapipe pyautogui numpy autopy
  ```

### Run the Project

```bash
python VirtualMouse.py
```

Make sure your webcam is connected and your hand is visible in the frame.

---

## 📸 Demo

Demo picture 1
<img width="1920" height="1200" alt="{CB4ED334-0C77-4100-80E3-AEE144627138}" src="https://github.com/user-attachments/assets/54d935e2-e00a-4369-ac22-19cf427ea67b" />

Demo picture 2
<img width="1920" height="1200" alt="{598483EE-0A55-4DD9-AC33-91E8BD423C52}" src="https://github.com/user-attachments/assets/c9217a64-9420-44e7-a253-ceaec3bd5fb6" />

---

## 📄 License

This project is licensed under the [Unlicense](LICENSE), making it free to use, modify, and distribute.
