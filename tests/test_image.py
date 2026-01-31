#import pytest
import cv2
from ImageObjects import MyImage


def test_image_crop():


    #    image = cv2.imread("/Users/george/oreilly/posture-monitor/images/testimage1_raw.jpeg")
    #     image = cv2.imread(filename)
    #
    #     if image is None:
    #         print("Could not read the image.")
    #         return

    filename="/Users/george/PycharmProjects/posture-monitor/tests/data/posture_0.jpg"
    my_image = MyImage().read_from_file(filename)
    print("sizes:", my_image.height, "\t",my_image.width)
    cv2.imshow('MediaPipe Pose', my_image.image)
    print(my_image)
    k = cv2.waitKey(0)

    xmin = int(my_image.width *0.35)
    xmax = int(my_image.width*0.65)
    ymin = 0
    ymax = int(my_image.height*1.0)

    my_image.crop_image(xmin, ymin, xmax, ymax)
    print(my_image)
    cv2.imshow('MediaPipe Pose', my_image.image)

    # Exit the loop if the 'q' key is pressed.
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     sys.exit()

    k = cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test_image_crop()
