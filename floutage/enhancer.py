from numpy import array
from skimage.exposure import rescale_intensity
from skimage.restoration import denoise_bilateral
from skimage.color import rgba2rgb, rgb2gray
from scipy.signal import convolve2d


class Enhancer:

    def __init__(self) -> None:

        self.__sharpen = array(
            [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    def enhance(self, gray_image):
        gray_image = rescale_intensity(gray_image)
        gray_image = convolve2d(gray_image, self.__sharpen, mode="same")
        gray_image = denoise_bilateral(
            gray_image, sigma_color=0.1, sigma_spatial=2)

    def convert2gray(self, rgba_image):
        return rgb2gray(rgba2rgb(rgba_image))
