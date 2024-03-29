import matplotlib.pyplot as plt


class Display:

    def __init__(self) -> None:

        plt.ion()
        self.__fig = plt.figure()
        self.__graph = self.__fig.add_subplot()

    def refresh(self, rgba_image) -> None:
        plt.cla()
        self.__graph.imshow(rgba_image)
        self.__fig.canvas.draw()
        self.__fig.canvas.flush_events()
