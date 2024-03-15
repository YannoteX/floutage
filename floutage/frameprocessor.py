from floutage.display import Display
from floutage.enhancer import Enhancer
from floutage.facefinder import FaceFinder
from floutage.faceblurring import FaceBlurring
import skimage.io as io


class FrameProcessor:
    def __init__(self, frame, step_ratio, scale_factor, blur_strength):
        self.frame = frame
        self.image = None
        self.gray_image = frame
        self.min_size = None
        self.max_size = None
        self.step_ratio = step_ratio
        self.scale_factor = scale_factor
        self.blur_strength = blur_strength
        self.display = Display()

    def setup(self):
        self.image = io.imread(self.frame)
        shape = self.image.shape
        self.min_size = (100, 100)
        self.max_size = (shape[0]*0.85, shape[1]*0.85)

    def enhance(self):
        enhancer = Enhancer()
        self.gray_img = enhancer.convert2gray(self.image)
        enhancer.enhance(self.gray_img)
        pass

    def blur(self):
        face_finder = FaceFinder(self.gray_img, self.step_ratio, self.scale_factor, self.min_size, self.max_size)
        # Detect faces
        detected_faces = face_finder.get_faces()

        for face in detected_faces:
            rectangle = face_finder.draw_rectangle(self.image, face)
            face_blurring = FaceBlurring(self.image, rectangle, self.blur_strength)
            face_blurring.blur()

        self.display.refresh(self.image)
        pass

    def process_frame(self):
        self.setup()
        self.enhance()
        self.blur()