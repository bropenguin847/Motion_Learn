"""
Motion Learn

Reference:
https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker/python
https://www.youtube.com/watch?v=06TE_U21FK4
"""

import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Video Feed setup
webcam = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    # Look up on config options for confidence, can try to play around with confidence number
    while webcam.isOpened():
        ret, frame = webcam.read()
        flip_frame = cv2.flip(frame, 1)

        # Detect posture and do calculations in the future
        # Recolor image from opencv (BGR) -> RGB
        image = cv2.cvtColor(flip_frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Detection of pose here
        results = pose.process(image)
        image.flags.writeable = True

        # Change back image color back to BGR for opencv
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Render out detections
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
            # ignore the blue color, the actual output is red
        )

        cv2.imshow("Live Feed, press 'q' to quit", image)

        # Exit the video feed by pressing 'q'
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    webcam.release()
    cv2.destroyAllWindows()

    print("This is the pose landmarks: ", results.pose_landmarks)
    print("These are the connections: ", mp_pose.POSE_CONNECTIONS)
