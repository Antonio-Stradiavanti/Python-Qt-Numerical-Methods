from NumericOperation import *
from sympy import symbols, latex, sympify
from enum import Enum

import math
class NumericDifferentiation(NumericOperation):
    def __init__(self):
        super().__init__()
        self.__E = 2**(-32)
        self.__M = None
        self.__h_0 = None



    def symbolic_function(self, M, order, x0):
        self.__M = M
        if order == 1:
            self.__h_0 = math.cbrt(3 * self.__E / self.__M)

            der1 = (self.f_x.subs(self.x, x0 + self.__h_0) - self.f_x.f.subs(self.x, x0 - self.__h_0)) / 2 / self.__h_0

            h = 2 * self.__h_0
            der2 = (self.f_x.subs(self.x, x0 + h) - self.f_x.f.subs(self.x, x0 - h)) / 2 / h

            runge = abs((der1 - der2) / (2 ** 1 - 1))
            g_h = self.__M * h ** 2 / 6 + self.__E / h

            return [ latex(der1), latex(runge), latex(g_h) ]

        else:
            self.__h_0 = 2*(3 * self.__E / self.__M) ** .25



    def table_function(self):
        ...




