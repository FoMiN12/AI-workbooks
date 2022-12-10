import numpy as np


class Trigonometry:
    def deg2rad(self, deg):
        return np.deg2rad(deg)

    def cos(self, deg):
        return np.cos(np.deg2rad(deg))

    def sin(self, deg):
        return np.sin(np.deg2rad(deg))

    def tg(self, deg):
        return np.tan(np.deg2rad(deg))

    def arcsin(self, deg):
        return np.arcsin(np.deg2rad(deg))

    def arccos(self, deg):
        return np.arccos(np.deg2rad(deg))

    def arctg(self, deg):
        return np.arctan(np.deg2rad(deg))
