from sympy import symbols, latex, sympify
from enum import Enum
class NumericMethod(Enum):
    INTEGRATION = 1
    DIFFERENTIATION = 2
class NumericOperation:
    def __init__(self):
        self.__eps = None
        self.__f_x = None
        self.x = symbols('x')

    @property
    def f_x(self):
        return self.__f_x

    @f_x.setter
    def f_x(self, f_x):
        self.__f_x = f_x

    @property
    def eps(self):
        return self.__eps

    @eps.setter
    def eps(self, eps):
        self.__eps = eps
