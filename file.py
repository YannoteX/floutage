from floutage.enhancer import Enhancer
from floutage.display import Display
import skimage.io as io
from skimage import data
from floutage.facefinder import *
from floutage.faceblurring import *
from time import sleep
import cv2


display = Display()

for i in range(1000000):
    image = io.imread("Capture3.PNG")
    print(i)
    display.refresh(image)