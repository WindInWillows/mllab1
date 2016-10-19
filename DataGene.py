import random
import numpy as np
import math

class DataGene():
    def __init__(self):
        self.X = []
        self.Y = []
        self.points_num = 10
        self._rate = 0.1
        self._start = 0
        self._step = 2 * math.pi / self.points_num
        for i in range(self.points_num):
            x = i*self._step+self._start
            self.X.append(x)
            self.Y.append(math.sin(x) + random.random()*self._rate)
        self.YMat = np.mat(self.Y).T

    def get_van_mat(self, order):
        mat = []
        for x in self.X:
            lst = [1]
            for i in range(order):
                lst.append(lst[i] * x)
            mat.append(lst)
        return np.mat(mat)

if __name__ == '__main__':
    dg = DataGene()
    print dg.X
    print dg.Y
    print dg.get_van_mat(3)
