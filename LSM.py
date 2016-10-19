from DataGene import DataGene
import numpy as np

class LSM():
    def __init__(self, order=3, reg=False):
        self.coes = None
        self.W = None
        self.dg = DataGene()
        self.order = order
        self.reg = reg
        self.X = self.dg.get_van_mat(self.order)
        self.XT = self.X.T
        self.XTX = self.XT * self.X
        self.Y = self.dg.YMat
        self._lambda = 0.1

    def fit(self):
        if self.reg:
            self.coes = (self.XTX + self._lambda * np.mat(np.eye(self.order + 1)))**-1 * self.XT * self.Y
        else:
            self.coes = (self.XTX)**-1 * self.XT * self.Y
