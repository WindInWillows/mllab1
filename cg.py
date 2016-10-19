from DataGene import DataGene
import numpy as np


class CG():
    def __init__(self, order=3, reg=False):
        self.dg = DataGene()
        self.order = order
        self.reg = reg
        self.X = self.dg.get_van_mat(self.order)
        self.XT = self.X.T
        self.XTX = self.XT * self.X

        self.Y = self.dg.YMat
        self.XTY = self.XT * self.Y
        self._lambda = 0.01
        self.step = 0.00001
        self._exit = 0.01
        self._w = 0.0001
        self.coes = np.mat([1 for i in range(order + 1)]).T

    def fit(self):
        g = self._dJ()
        d = - g
        j_old = self._J()
        self.coes = self.coes + self.step * d
        j_new = self._J()

        while abs(j_new - j_old) > self._exit:
            g_plus = self._dJ()
            beta = self._get_num((g_plus.T * g_plus) / (g.T*g))
            d = -g_plus + beta * d
            self.coes = self.coes - self.step * d
            g = g_plus
            j_old = j_new
            j_new = self._J()
            if j_new > j_old :
                self.step *= 0.5


    def _J(self):
        mat = (self.X * self.coes - self.Y)
        mat = mat.T * mat
        mat = mat + self._lambda * (self._get_num(self.coes.T * self.coes) ** 0.5)
        return mat.tolist()[0][0]

    def _get_num(self,mat):
        return mat.tolist()[0][0]

    def _dJ(self):
        mat = 2 * self.XTX * self.coes - 2 * self.XTY + self._lambda * self._get_num(self.coes.T * self.coes)**-0.5*self.coes
        return mat