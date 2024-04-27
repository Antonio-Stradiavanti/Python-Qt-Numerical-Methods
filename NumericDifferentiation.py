from NumericOperation import *
from sympy import symbols, latex, sympify
class NumericDifferentiation(NumericOperation):
    def __init__(self):
        super().__init__()
        self.__M = None

    @property
    def M(self):
        return self.__M

    @M.setter
    def M(self, m):
       self.__M = m