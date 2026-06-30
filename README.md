# i2i-Academy-ComputerVision-3

This is a hand detection and finger counting application that is created with Python programming language, OpenCV, and MediaPipe. This project was designed to apply computer vision concepts through the use of a webcam and an existing hand tracking algorithm.

In the process, OpenCV is used to open the webcam, capture frames, and show the output on the screen. MediaPipe is used to detect the presence of hands and extract landmarks on fingertips and finger joints.

Each finger's landmarks are checked to find out whether a finger is opened or closed. When the tip of a finger is above the lower finger joint, then the finger is considered to be opened. After that, the number of opened fingers is displayed on the webcam window.

The reason I choose MediaPipe is that it has a pre-trained hand detection model, which means you don't have to train your own neural network from scratch, and the project would fit better into a beginner level computer vision project.

To run the project, the required libraries should be installed:

python -m pip install opencv-python mediapipe

Then, the Python file can be run. The webcam window opens, and the user can press “q” to close the application.

Sometimes the finger count can be incorrect, depending on the angle of the hand, lighting, the position of the camera, or finger visibility. Sometimes it is hard to track the thumb since it moves in a different way than other fingers.
