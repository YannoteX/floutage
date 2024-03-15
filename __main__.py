from floutage.enhancer import Enhancer
from floutage.display import Display
import skimage.io as io
from skimage import data
from floutage.facefinder import *
from floutage.faceblurring import *
from time import sleep
import cv2

# Sample parameters
step_ratio = 1
scale_factor = 1.1
display = Display()

class Capture:
    def __init__(self, video_source):
        self.video_source = video_source
        self.cap = cv2.VideoCapture(0) 

    def main_method(self, frame):
        # Placeholder for the main method to process the frame
        image = io.imread("frame.jpg")
        # plt.imshow(image)
        # plt.savefig("image.png")
        shape = image.shape
        min_size = (100, 100)
        max_size = (shape[0], shape[1])

        enhancer = Enhancer()
        gray_img = enhancer.convert2gray(image)
        enhancer.enhance(gray_img)

        # Instantiate FaceFinder
        face_finder = FaceFinder(gray_img, step_ratio, scale_factor, min_size, max_size, "image.png")

        # face_finder.init_subp() # Red rectangle

        # Detect faces
        detected_faces = face_finder.get_faces()

        for face in detected_faces:
            rectangle = face_finder.draw_rectangle(image, face)
            face_blurring = FaceBlurring(image, rectangle, 70)
            face_blurring.blur()

        # plt.imshow(image) # Red rectangle
        display.refresh(image)
        pass

    def export_frames(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                cv2.imwrite('frame.jpg', frame)
                self.main_method(frame)
            else:
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Load an image
image_path = 'Capture3.png'

capture = Capture('zoo.mp4')
capture.export_frames()
# face_finder.save_img() # save to file