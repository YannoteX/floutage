import skimage
from skimage import io
from skimage.feature import Cascade
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import patches


class FaceFinder:
    def __init__(self, image, step_ratio, scale_factor, min_size, max_size, destination) -> None:

        self.__image = image
        self.__destination = destination
        self.__scale_factor = scale_factor # how much the image size is reduced at each image scale
        self.__step_ratio = step_ratio # ....
        self.__min_size = min_size # Minimum possible object size
        self.__max_size = max_size # Maximum possible object size
        self.__trained_file = skimage.data.lbp_frontal_face_cascade_filename()
        self.__detector = Cascade(self.__trained_file)
        self.__fig = None # unused ?
        self.__axis = any # type to change

    def init_subp(self) -> None:
        self.__fig, self.__axis = plt.subplots()
        plt.set_cmap("gray")

    def get_faces(self) -> list:

        # Load trained file
        trained_file = self.__trained_file

        # Initializing detector
        detector = self.__detector

        detected_faces = detector.detect_multi_scale(
            img=self.__image,
            scale_factor=self.__scale_factor,
            step_ratio=self.__step_ratio,
            min_size=self.__min_size,
            max_size=self.__max_size,
        )

        return detected_faces
    
    def draw_rectangle(self, image, face) -> list:
        # X-Y starting points of the face rectangle
        x, y = face["r"], face["c"]

        # Width-height of the face rectangle
        width, height = (
            face["width"],
            face["height"],
        )

        # Extract the detected face
        face = image[x:width, y:height]

        if False:
        # Draw rectangle
            self.__axis.add_patch(
                patches.Rectangle(
                    (y, x),
                    width,
                    height,
                    fill=False,
                    color="r",
                    linewidth=2,
                )
            )

        return [x, y, width, height]

    def save_img(self) -> None:
        plt.savefig(self.__destination)