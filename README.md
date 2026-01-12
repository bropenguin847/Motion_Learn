# Motion_Learn
Motion Learn is a visual based learning tool by detecting posture and then outputs a detailed information about body parts to enhance learning

📝 Project Abstract
This project is a real-time interactive tool designed to enhance student learning of human anatomy. Utilizing a webcam and the MediaPipe Pose Landmarker (Lite model), the system detects when a user intentionally touches a specific body part (e.g., nose, elbow, shoulder). By calculating the  distance between the Index Finger landmark and the target body part landmark, the system approximates touch. Upon successful detection, it triggers an immediate audio and visual output confirming the body part's name and its basic function. This approach leverages kinesthetic learning to create a responsive, engaging, and accessible educational experience without requiring specialized hardware.


Reference and inspirations:
[Google Developers Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker/python)
[Pose Landmarker notebook](https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/pose_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Pose_Landmarker.ipynb)
[Nicholas Renotte's Gym Tracker project YT](https://www.youtube.com/watch?v=06TE_U21FK4)
