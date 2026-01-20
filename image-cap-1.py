import cv2


def capture_image_from_camera():
    # Create a VideoCapture object. 0 represents the default laptop camera.
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a single frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully (ret is True)
    if ret:
        # Define the path and filename for the saved image
        image_path = 'images/captured_image.png'

        # Save the captured frame as an image file
        cv2.imwrite(image_path, frame)
        print(f"Image successfully saved as {image_path}")

        # Display the captured image for a moment (optional)
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(0)  # Wait for any key press to close the image window
        cv2.destroyAllWindows()  # Close all OpenCV windows

    else:
        print("Error: Could not read a frame from the camera.")

    # Release the camera capture object
    cap.release()


if __name__ == "__main__":
    capture_image_from_camera()
