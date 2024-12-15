# Basic-Facial-Mesh-using-MediaPipe
Beginner Facial Mesh using OpenCV and MediaPipe (Python)
This project demonstrates how to detect and render facial mesh landmarks on a live video feed using OpenCV and MediaPipe in Python. It leverages the MediaPipe FaceMesh solution to draw facial landmarks, offering a simple approach to facial feature detection and mesh rendering.

Requirements:
OpenCV: For handling video capture and display.
MediaPipe: For facial mesh detection.
Code Explanation:
MediaPipe Setup: The mp.solutions.face_mesh.FaceMesh model is used to detect and track facial landmarks. The max_num_faces=2 option tracks up to 2 faces in the frame.
Video Capture: OpenCV's cv2.VideoCapture(0) is used to start a live video feed from the default camera.
Drawing Landmarks: The facial landmarks are drawn using mpdrawing.draw_landmarks with two different drawing styles: tesselation (for a network of mesh lines) and contours (outlining key facial features).
Real-Time Video: The captured video is processed and displayed with the facial mesh overlaid. Press 'q' to exit.
