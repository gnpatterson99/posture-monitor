import datetime
import time
from pathlib import Path

import cv2
import os
import sys

project_path="/Users/george/PycharmProjects/posture-monitor/"

def capture_image_from_camera(camera_id=0, filename="captured_image.png",wait_after_show=False):
    # Create a VideoCapture object. 0 represents the default laptop camera.
    # cap = cv2.VideoCapture(camera_id)

    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

    # i found these suggeted in a forum post.
    # frameWidth = 640
    # frameHeight = 480
    # cap.set(3, frameWidth)
    # cap.set(4, frameHeight)
    # cap.set(10, 150)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    for i in range(10):
        cap.read()

    # Read a single frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully (ret is True)
    if ret:
        # Define the path and filename for the saved image
        image_path = filename

        # Save the captured frame as an image file
        cv2.imwrite(image_path, frame)
        print(f"Image successfully saved as {image_path}")

        # Display the captured image for a moment (optional)
        cv2.imshow("Captured Image", frame)

        if wait_after_show==True:
            cv2.waitKey(0)  # Wait for any key press to close the image window

        cv2.destroyAllWindows()  # Close all OpenCV windows

    else:
        print("Error: Could not read a frame from the camera.")

    # Release the camera capture object
    cap.release()


if __name__ == "__main__":

    date_string = datetime.datetime.today().strftime("%Y%m%d")
    path=Path("/Users/george/egoscue/"+date_string)

    if path.exists() == False:
        path.mkdir(parents=True, exist_ok=True)

    if path.exists() == False:
        print("Error: Could not create directory.")
        sys.exit(1)


    for pose_cnt in range(4):
        print(f"Pose {pose_cnt}")

        # need as_posix() to get a string
        fname=path.joinpath(f"posture_{pose_cnt}.jpg").as_posix()

        for i in range(2):
            print(f"delay loop {i}")
            # os.system('afplay /System/Library/Sounds/Ping.aiff')
            os.system('afplay ' + project_path + 'sounds/audacity_move.wav')

            # sys.stdout.write('\a')
            # sys.stdout.flush()
            # time.sleep(1)
        print("Taking Photo....")
        # os.system('afplay /System/Library/Sounds/Glass.aiff')
        os.system('afplay ' + project_path + 'sounds/audacity_hold.wav')
        capture_image_from_camera(filename=fname,wait_after_show=False,camera_id=0)
        os.system('afplay ' + project_path + 'sounds/audacity_donephoto.wav')

    print("Done")

#    capture_image_from_camera()
