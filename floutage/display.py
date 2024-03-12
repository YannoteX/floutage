import matplotlib.pyplot as plt


class Display:

    def __init__(self) -> None:

        plt.ion()
        self.__fig = plt.figure()
        self.__graph = self.__fig.add_subplot()

    def refresh(self, image) -> None:

        self.__graph.imshow(image)
        self.__fig.canvas.draw()
        self.__fig.canvas.flush_events()