

# HandControl – Real-Time Hand Gesture Recognition with Python

## Project Status & Metadata

[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/souraaav/handcontrol)  
[![Made with Python | OpenCV | MediaPipe](https://img.shields.io/badge/Made%20with-Python%20%7C%20OpenCV%20%7C%20MediaPipe-blue)](https://github.com/souraaav/handcontrol)  
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-red)](LICENSE)  
<img src="https://tenor.com/eyddOsShsCt.gif" alt="Girl in a jacket" width="500" height="600">
---

## Summary

HandControl is a Python-based computer vision project that uses MediaPipe and OpenCV to detect and track hand gestures in real time. It enables gesture-based interaction with applications, making it ideal for touchless control systems, accessibility tools, and interactive demos. The project showcases how lightweight models and efficient pipelines can be used to build responsive gesture recognition systems.

---

## Project Overview

- Detects hands and landmarks using MediaPipe  
- Tracks finger positions and gestures in real time  
- Uses OpenCV for video capture and rendering  
- Modular design for easy extension and integration  
- Can be adapted for gesture-controlled interfaces or games  

---

## File Descriptions

<details>
<summary><code>main.py</code></summary>

The main execution script. It:

- Initializes the webcam feed  
- Loads the hand tracking module  
- Displays the live annotated video stream  
- Handles gesture detection logic  

</details>

<details>
<summary><code>handmodule.py</code></summary>

Custom module for hand detection and tracking. It:

- Wraps MediaPipe’s hand detection API  
- Extracts landmark positions  
- Provides utility functions for gesture analysis  

</details>

---

## Tech Used

- Python – Core programming language  
- OpenCV – Real-time video processing  
- MediaPipe – Hand tracking and landmark detection  
- NumPy – Array manipulation and math utilities  

---


### Prerequisites

- Python 3.7 or higher  
- pip (Python package manager)  

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/souraaav/handcontrol.git
cd handcontrol

# Install dependencies
pip install opencv-python mediapipe numpy

# Run the project
python main.py
```

---

## Demo

[![Live Demo](https://img.shields.io/badge/DEMO-ONLINE-blue?style=for-the-badge)](https://your-handcontrol-demo-link.com)

Screenshot<img width="1612" height="953" alt="{2A701D35-7DC8-4522-94DB-DAD808ED32FE}" src="https://github.com/user-attachments/assets/6c815920-09d9-43e9-b7a2-dbd38b5db7c5" />


---

## Future Enhancements

- Add gesture classification for specific commands  
- Integrate with GUI applications or games  
- Support multi-hand tracking  
- Add voice feedback or sound effects  
- Deploy as a web app using WebRTC and TensorFlow.js  

---

## License

This project is released under the [Unlicense](LICENSE), placing it in the public domain.

