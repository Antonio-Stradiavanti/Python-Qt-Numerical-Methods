from NumericOperation import *
from sympy import symbols, latex, sympify
from enum import Enum

import math
class NumericDifferentiation(NumericOperation):
    E = 2**(-32)

    def __init__(self):
        super().__init__()
        self.h_0 = None


    def symbolic_function(self, x0, order, M):
        der = None; runge = None; g_h = None
        if order == 1:
            self.h_0 = math.cbrt(3 * self.E / M)

            der = (self.f_x.subs(self.x, x0 + self.h_0) - self.f_x.subs(self.x, x0 - self.h_0)) / 2 / self.h_0

            h = 2 * self.h_0
            der1 = (self.f_x.subs(self.x, x0 + h) - self.f_x.subs(self.x, x0 - h)) / 2 / h

            g_h = M * self.h_0 ** 2 / 6 + self.E / self.h_0
            runge = abs((der - der1)) / (2 ** order - 1)
        else:
            self.h_0 = 2*(3 * self.E / M) ** .25

            der = (self.f_x.subs(self.x, x0 - self.h_0) - 2*self.f_x.subs(self.x, x0) + self.f_x.subs(self.x, x0 + self.h_0)) / self.h_0 ** 2

            h = 2 * self.h_0
            der1 = (self.f_x.subs(self.x, x0 - h) - 2*self.f_x.subs(self.x, x0) + self.f_x.subs(self.x, x0 + h)) / h ** 2

            g_h = M * self.h_0 ** 2 / 12 + 4 * self.E / self.h_0 ** 2
            runge = abs((der - der1)) / (2 ** order - 1)
        # ---
        return [der, runge, g_h]



    # Гарантируем, что сетка равномерная
    def table_function(self, x0, order):

        # Аналог производной
        # f(x_i, x_j, x_k, ..., x_{n-1}, x_n) = (f(x_i, x_j, x_k, ..., x_{n-1}) - f(x_j, x_k, ..., x_{n-1}, x_n)) / (x_i - x_n)
        def divided_differences(X, Y, k):
            # Производной нулевого порядка не существует, а разделенная разность 0 порядка -- просто значение ф-ции
            if k == 1:
                return Y[0]
            return (divided_differences(X[1:], Y[1:], k-1) - divided_differences(X[:-1], Y[:-1], k-1)) / (X[-1] - X[0])


        der = None; der1 = None; runge = None; g_h = None
        h = 2 * self.h_0

        X = list(self.f_x.keys())
        Y = list(self.f_x.values())

        ind = X.index(x0)

        # Осталось обработать исключительные ситуации

        if order == 1:
            der = (Y[ind + 1] - Y[ind - 1]) / 2 * self.h_0
            der1 = (Y[ind + 2] - Y[ind - 2]) / (2 * 2 * self.h_0)

            # точность метода, рассчитанная на основе оценки остаточного члена формулы численного дифференцирования
            # R_1(f) = - h**2 / 6 * f'''(d)
            g_h = -1 * self.h_0 ** 2 / 6 * (2 * 3 * divided_differences(X[ind-2:ind+3], Y[ind-2:ind+3], 3+1))
            runge = abs((der - der1)) / (2 ** 2 - 1)
        else:
            der = (Y[ind - 1] - 2*Y[ind] + Y[ind + 1]) / self.h_0 ** 2
            der1 = (Y[ind - 2] - 2*Y[ind] + Y[ind + 2]) / h ** 2

            g_h = -1 * self.h_0 ** 2 / 12 * (2 * 3 * 4 * divided_differences(X[ind - 2:ind + 3], Y[ind - 2:ind + 3], 4+1))
            runge = abs((der - der1)) / (2 ** 2 - 1)

        # print(self.h_0, "h = ", h, "; ind = ", ind, "\n\nX = ", X, "\n\nY = ", Y, "der =", der, "\n\n", der1)
        #---
        return [der, runge, g_h]





