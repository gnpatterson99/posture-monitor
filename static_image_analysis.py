# Ref: https://learnopencv.com/building-a-body-posture-analysis-system-using-mediapipe/
from pathlib import Path

import cv2
import time
import math as m
import mediapipe as mp
import argparse
import sys
import os
import ssl

# This bypasses the SSL certificate verification issue common on macOS
# when downloading MediaPipe model files.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose

class BodyPoint:
    def __init__(self, pose_landmark):
        self.pose_landmark = pose_landmark
        self.x=0
        self.y=0


    def update(self,kp):
        self.x = float(kp.pose_landmarks.landmark[self.pose_landmark].x)
        self.y = float(kp.pose_landmarks.landmark[self.pose_landmark].y)
        return self

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return "BP: %d, x=%f,x=%f" % (self.pose_landmark, self.x, self.y)


class MyImage:
    def __init__(self, image):
        self.image = image
        self.height, self.width = image.shape[:2]
        print("Image. height=",self.height, "\twidth=",self.width)

    def draw_landmarks(self, bp, color):
        cv2.circle(self.image, (int(bp.x * self.width), int(bp.y*self.height)), 7, color, 2)

    def draw_line(self, bp1, bp2, color):
        cv2.line(self.image, (int(bp1.x * self.width), int(bp1.y*self.height)),
                 (int(bp2.x * self.width), int(bp2.y*self.height)), color, 2)

    def cvt_brg_to_rgb(self):
        self.image= cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def cvt_rgb_to_brg(self):
        self.image= cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)


def findDistance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points.

    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.

    Returns:
        Distance between the two points.
    """
    dist = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def findAngle(x1, y1, x2, y2):
    """
    Calculate the angle between two points with respect to the y-axis.

    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.

    Returns:
        Angle in degrees.
    """
    theta = m.acos((y2 - y1) * (-y1) / (m.sqrt((x2 - x1)**2 + (y2 - y1)**2) * y1))
    degree = int(180/m.pi) * theta
    return degree

def sendWarning(x):
    """
    Placeholder function for sending a warning.
    """
    pass

def parse_arguments():
    parser = argparse.ArgumentParser(description='Posture Monitor with MediaPipe')
    parser.add_argument('--video', type=str, default=0, help='Path to the input video file. If not provided, the webcam will be used.')
    parser.add_argument('--offset-threshold', type=int, default=100, help='Threshold value for shoulder alignment.')
    parser.add_argument('--neck-angle-threshold', type=int, default=25, help='Threshold value for neck inclination angle.')
    parser.add_argument('--torso-angle-threshold', type=int, default=10, help='Threshold value for torso inclination angle.')
    parser.add_argument('--time-threshold', type=int, default=180, help='Time threshold for triggering a posture alert.')
    return parser.parse_args()

def main(filename):

    # Font type.
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Colors.
    blue = (255, 127, 0)
    red = (50, 50, 255)
    green = (127, 255, 0)
    dark_blue = (127, 20, 0)
    light_green = (127, 233, 100)
    yellow = (0, 255, 255)
    pink = (255, 0, 255)
    white = (255, 255, 255)

    # Initialize mediapipe pose class.
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(  static_image_mode=True,
               model_complexity=2,)
    # need some additional code to upgrade to 2

    # For file input, replace file name with <path>.
    # cap = cv2.VideoCapture(video_path) if video_path else cv2.VideoCapture(0)

    # Meta.
    # fps = int(cap.get(cv2.CAP_PROP_FPS))

#    image = cv2.imread("/Users/george/oreilly/posture-monitor/images/testimage1_raw.jpeg")
    image = cv2.imread(filename)

    if image is None:
        print("Could not read the image.")
        return

    my_image = MyImage(image)

    # # Convert the BGR image to RGB.
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #
    # # Process the image.
    # keypoints = pose.process(image)
    #
    # # Convert the image back to BGR.
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Convert the BGR image to RGB.
    my_image.cvt_brg_to_rgb()
    # Process the image.
    keypoints = pose.process(my_image.image)
    # print(keypoints)

    # Convert the image back to BGR.
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    my_image.cvt_rgb_to_brg()

    # Use lm and lmPose as representative of the following methods.
    lm = keypoints.pose_landmarks
    lmPose = mp_pose.PoseLandmark

    if lm is None:
        print("LM is None")

    # Left shoulder.

    left_shoulder = BodyPoint(lmPose.LEFT_SHOULDER).update(keypoints)
    right_shoulder = BodyPoint(lmPose.RIGHT_SHOULDER).update(keypoints)

    right_hip = BodyPoint(lmPose.RIGHT_HIP).update(keypoints)
    left_hip = BodyPoint(lmPose.LEFT_HIP).update(keypoints)

    right_knee = BodyPoint(lmPose.RIGHT_KNEE).update(keypoints)
    left_knee = BodyPoint(lmPose.LEFT_KNEE).update(keypoints)

    left_ankle = BodyPoint(lmPose.LEFT_ANKLE).update(keypoints)
    right_ankle = BodyPoint(lmPose.RIGHT_ANKLE).update(keypoints)

    left_wrist = BodyPoint(lmPose.LEFT_WRIST).update(keypoints)
    right_wrist = BodyPoint(lmPose.RIGHT_WRIST).update(keypoints)

    left_elbow = BodyPoint(lmPose.LEFT_ELBOW).update(keypoints)
    right_elbow = BodyPoint(lmPose.RIGHT_ELBOW).update(keypoints)

    left_heel=BodyPoint(lmPose.LEFT_HEEL).update(keypoints)
    right_heel=BodyPoint(lmPose.RIGHT_HEEL).update(keypoints)
    left_foot_index=BodyPoint(lmPose.LEFT_FOOT_INDEX).update(keypoints)
    right_foot_index=BodyPoint(lmPose.RIGHT_FOOT_INDEX).update(keypoints)

    # print(left_shoulder)
    # print(right_shoulder)
    # print(right_hip)
    # print(left_hip)

    # Calculate distance between left shoulder and right shoulder points.
    # offset = findDistance(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)

    # Assist to align the camera to point at the side view of the person.
    # Offset threshold 30 is based on results obtained from analysis over 100 samples.
    # if offset < offset_threshold:
    #     cv2.putText(image, str(int(offset)) + ' Shoulders aligned', (w - 280, 30), font, 0.6, green, 2)
    # else:
    #     cv2.putText(image, str(int(offset)) + ' Shoulders not aligned', (w - 280, 30), font, 0.6, red, 2)

    # Calculate angles.
    # neck_inclination = findAngle(l_shldr_x, l_shldr_y, l_ear_x, l_ear_y)
    # torso_inclination = findAngle(l_hip_x, l_hip_y, l_shldr_x, l_shldr_y)

    # Draw landmarks.
    my_image.draw_landmarks(left_shoulder, white)
    my_image.draw_landmarks(right_shoulder, white)
    my_image.draw_landmarks(right_hip, yellow)
    my_image.draw_landmarks(left_hip, yellow)
    my_image.draw_landmarks(right_knee, pink)
    my_image.draw_landmarks(left_knee, pink)
    my_image.draw_landmarks(left_ankle, white)
    my_image.draw_landmarks(right_ankle, white)
    my_image.draw_landmarks(left_wrist, white)
    my_image.draw_landmarks(right_wrist, white)
    my_image.draw_landmarks(left_elbow, white)
    my_image.draw_landmarks(right_elbow, white)

    my_image.draw_line(left_shoulder, right_shoulder, green)
    my_image.draw_line(left_shoulder, left_elbow, green)
    my_image.draw_line(left_elbow, left_wrist, green)

    my_image.draw_line(right_shoulder, right_elbow, green)
    my_image.draw_line(right_elbow, right_wrist, green)

    my_image.draw_line(left_hip, right_hip, green)
    my_image.draw_line(left_hip, left_knee, green)
    my_image.draw_line(left_knee, left_ankle, green)

    my_image.draw_line(right_hip, right_knee, green)
    my_image.draw_line(right_knee, right_ankle, green)

    my_image.draw_line(left_heel, left_foot_index, green)
    my_image.draw_line(right_heel, right_foot_index, green)

    # cv2.circle(image, (l_shldr_x, l_shldr_y), 7, white, 2)
    # cv2.circle(image, (l_ear_x, l_ear_y), 7, white, 2)

    # Let's take y - coordinate of P3 100px above x1,  for display elegance.
    # Although we are taking y = 0 while calculating angle between P1,P2,P3.
#        cv2.circle(image, (l_shldr_x, l_shldr_y - 100), 7, white, 2)
#     cv2.circle(image, (r_shldr_x, r_shldr_y), 7, pink, -1)
#     cv2.circle(image, (l_hip_x, l_hip_y), 7, yellow, -1)
#     cv2.circle(image, (r_hip_x, r_hip_y), 7, yellow, -1)

    # print(r_shldr_y- l_shldr_y,"\t",r_hip_y - l_hip_y)

    # Similarly, here we are taking y - coordinate 100px above x1. Note that
    # you can take any value for y, not necessarily 100 or 200 pixels.
    # cv2.circle(image, (l_hip_x, l_hip_y - 100), 7, yellow, -1)

    # Put text, Posture and angle inclination.
    # Text string for display.
    # angle_text_string_neck = 'Neck inclination: ' + str(int(neck_inclination))
    # angle_text_string_torso = 'Torso inclination: ' + str(int(torso_inclination))

    # Determine whether good posture or bad posture.
    # The threshold angles have been set based on intuition.


    # cv2.putText(image, angle_text_string_neck, (10, 30), font, 0.6, light_green, 2)
    # cv2.putText(image, angle_text_string_torso, (10, 60), font, 0.6, light_green, 2)
    # cv2.putText(image, str(int(neck_inclination)), (l_shldr_x + 10, l_shldr_y), font, 0.9, light_green, 2)
    # cv2.putText(image, str(int(torso_inclination)), (l_hip_x + 10, l_hip_y), font, 0.9, light_green, 2)

    # Join landmarks.
    # cv2.line(image, (l_shldr_x, l_shldr_y), (l_ear_x, l_ear_y), green, 2)
    # cv2.line(image, (l_shldr_x, l_shldr_y), (l_shldr_x, l_shldr_y - 100), green, 2)
    # cv2.line(image, (l_hip_x, l_hip_y), (l_shldr_x, l_shldr_y), green, 2)
    # cv2.line(image, (l_hip_x, l_hip_y), (l_hip_x, l_hip_y - 100), green, 2)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', my_image.image)

    # Exit the loop if the 'q' key is pressed.
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     sys.exit()

    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

# if k == ord("s"):
    #     cv.imwrite("starry_night.png", img)


if __name__ == "__main__":
    args = parse_arguments()
    
    # print("Arguments:")
    # print(f"Video: {args.video}")
    # print(f"Offset Threshold: {args.offset_threshold}")
    # print(f"Neck Angle Threshold: {args.neck_angle_threshold}")
    # print(f"Torso Angle Threshold: {args.torso_angle_threshold}")
    # print(f"Time Threshold: {args.time_threshold}")

    path = Path("/Users/george/egoscue/20260124")
    fnames = path.glob("*.jpeg")
    for fname in fnames:
        print(fname.as_posix())
        main(fname.as_posix())

#    main(args.video)
