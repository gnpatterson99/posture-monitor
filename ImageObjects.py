import cv2


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
    def __init__(self):
        self.image = None
        self.height=None
        self.width=None



    def read_from_file(self, filename):
        image = cv2.imread(filename)

        if image is None:
            print("Could not read the image. Result is None")

        self.image = image
        self.height, self.width = image.shape[:2]
        return self

    def write_to_file(self, filename):
        cv2.imwrite(filename, cv2.cvtColor(self.image, cv2.COLOR_RGB2BGRA))


    def crop_image(self, xmin, ymin, xmax, ymax):
        self.image = self.image[ymin:ymax, xmin:xmax].copy()
        # TODO what to do with
        self.height, self.width = self.image.shape[:2]
        return self


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

    def __str__(self):
        return "Image: foo, width=%f,height=%f" % (self.width, self.height)
