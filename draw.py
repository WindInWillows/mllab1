import matplotlib.pyplot as plt
import numpy as np
from LSM import LSM
from cg import CG
from gd import GD
import math

class draw():
    def __init__(self):
        self.obj = None
        self._range = 2 * math.pi

    def show(self):
        self.obj.fit()
        plt.plot(self.obj.dg.X, self.obj.dg.Y,"or")
        xs = np.linspace(0, self._range, 100)
        f = lambda x:self._f(x);
        plt.plot(xs, [math.sin(x) for x in xs])
        plt.plot(xs, [f(x) for x in xs])
        # plt.plot()
        plt.show()

    def _f(self,x):
        coes = self.obj.coes.T.tolist()[0]
        sum = 0
        xx = 1
        for coe in coes:
            sum += xx * coe
            xx *= x
        return sum

if __name__ == '__main__':
    draw = draw()
    draw.obj = CG()
    draw.show()


