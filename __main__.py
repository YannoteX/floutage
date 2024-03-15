from floutage.enhancer import Enhancer
from floutage.display import Display
from time import sleep

enhancer = Enhancer()
display = Display()


enhancer.set_image('Capture.png')
display.refresh(enhancer.get_image())
sleep(1)
enhancer.enhance()
display.refresh(enhancer.get_image())
sleep(1)

enhancer.set_image('Capture1.png')
display.refresh(enhancer.get_image())
sleep(1)
enhancer.enhance()
display.refresh(enhancer.get_image())
sleep(1)

enhancer.set_image('Capture3.png')
display.refresh(enhancer.get_image())
sleep(1)
enhancer.enhance()
display.refresh(enhancer.get_image())
sleep(1)

enhancer.set_image('Capture4.png')
display.refresh(enhancer.get_image())
sleep(1)
enhancer.enhance()
display.refresh(enhancer.get_image())
sleep(1)

enhancer.set_image('Capture5.png')
display.refresh(enhancer.get_image())
sleep(1)
enhancer.enhance()
display.refresh(enhancer.get_image())
sleep(1)

enhancer.set_image('Capture6.png')
display.refresh(enhancer.get_image())
sleep(1)
enhancer.enhance()
display.refresh(enhancer.get_image())
sleep(1)
