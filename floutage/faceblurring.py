from skimage import filters
import numpy as np
import matplotlib.pyplot as plt


class FaceBlurring:
    def __init__(self, image, rectangle, strength) -> None:
        self.__image = image
        self.__rectangle = rectangle
        self.__strength = strength
        
        
    def blur(self) -> np.ndarray:
        x, y, width, height = self.__rectangle
        face = self.__image[x:x+width, y:y+height]
        filtered = filters.gaussian(face, self.__strength, channel_axis=-1)
        filtered = np.round(255 * filtered)
        self.__image[x:x+width, y:y+height] = filtered
        return self.__image