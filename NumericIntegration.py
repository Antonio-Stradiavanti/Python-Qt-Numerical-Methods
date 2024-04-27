from NumericOperation import *
from enum import Enum
from sympy import symbols, latex, sympify
class NumericIntegration(NumericOperation):
    class NewCotQuads(Enum):
        TRAPEZOID = 1
        SIMPSON = 2
        NEWTON = 3
    def __init__(self):
        super().__init__()
        self.__a = None; self.__b = None

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, la):
        self.__a = la

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, lb):
        self.__b = lb

    def trapRule(self, n):
        h = (self.b - self.a) / n
        i_r = 0;
        i_t = (self.f_x.subs(self.__x, self.a) + self.f_x.subs(self.__x, self.b)) / 2
        for i in range(1, n):
            i_r += self.f_x.subs(self.__x, self.a + i * h)

        return h * (i_t + i_r)

    def simpRule(self, n):
        h = (self.b - self.a) / n
        s = 0
        for i in range(n):
            s += (1 / 6) * self.f_x.subs(self.__x, self.a + i * h) + (2 / 3) * self.f_x.subs(self.__x, self.a + (
                        i + .5) * h) + (1 / 6) * self.f_x.subs(self.__x, self.a + (i + 1) * h)
        return s * h

    def newtonRule(self, n):
        h = (self.b - self.a) / n;
        s = 0
        for i in range(n):
            s += ((1 / 8) * self.f_x.subs(self.__x, self.a + i * h) + (3 / 8) * self.f_x.subs(self.__x, self.a + (
                        i + 1 / 3) * h) + (3 / 8) * self.f_x.subs(self.__x, self.a + (i + 2 / 3) * h) + (
                              1 / 8) * self.f_x.subs(self.__x, self.a + (i + 1) * h))
        return s * h

    def runge(self, quad_type, old_res, n):
        n *= 2; fact = 1; delta = 1
        match quad_type:
            case self.NewCotQuads.TRAPEZOID:
                new_res = self.trapRule(n)
                fact = 3
            case self.NewCotQuads.SIMPSON:
                new_res = self.simpRule(n)
                fact = 15
            case self.NewCotQuads.NEWTON:
                new_res = self.newtonRule(n)
                fact = 15
        delta = abs(new_res - old_res) / fact
        if delta < self.eps:
            return [new_res, delta]
        else:
            return self.runge(quad_type, new_res, n)