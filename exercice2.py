import numpy as np
import matplotlib.pyplot as plt


class Curve():
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def tracer_courbe(self):
        list_x = np.linspace(self.start, self.stop, 100)
        list_y = [self.__fx(x) + 0.5 for x in list_x]
        plt.plot(list_x, list_y, color='red')
        plt.xlim(0, 1)
        plt.ylim(0, 1.6)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        plt.show()

    def position_point(self):
        pass

    def genere_nbre_points(self):
        list_x = np.random.uniform(self.start, self.stop, self.nbr_points)
        list_y = np.random.uniform(0, self.__fx(self.stop), self.nbr_points)

        for x, y in zip(list_x, list_y):
            if y > self.__fx(x) + 0.5:
                plt.plot(x, y, 'b+', markersize=3)
            else:
                plt.plot(x, y, 'go', markersize=3)

        self.tracer_courbe()

    def caluler_surface(self):
        pass

    def __fx(self, x):
        return x ** 5


if __name__ == '__main__':
    curve = Curve(0, 1)
    curve.genere_nbre_points()
