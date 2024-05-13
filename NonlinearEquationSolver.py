from NumericOperation import *
import time
from sympy import diff, evalf
class NonlinearEquationSolver(NumericOperation):
    def __init__(self):
        super().__init__()
        # c -> Предполагаемый корень
        self.a = None; self.b = None; c = None
        self.delta = None

        self.met_dict()

    @classmethod
    def met_dict(cls, met_keys=None):
        if met_keys is None:
            met_keys = ["Метод дихотомии", "Метод хорд", "Метод Ньютона", "Метод секущих", "Гибридный метод Ньютона-половинного деления"]
        met_vals = [cls.dichotomy_method, cls.chord_method, cls.newton_method, cls.secant_method, cls.hybrid_method]
        cls.mets = dict(zip(met_keys, met_vals))

    def solve(self, met):
        return self.mets[met](self)

    # метод половинного деления
    def dichotomy_method(self):
        # eps -> допустимая погрешность, delta -> допуск, связанный с точностью вычисления зр ф-ции
        count = 0
        c = 1
        start = time.time()
        while True:
            count += 1
            c = (self.a + self.b) / 2
            # Если b-a < 2*eps ИЛИ если |f(c)| < delta
            if self.b - self.a < 2 * self.eps or abs(self.f_x.subs(self.x, c)) < 2 * self.delta:
                end = time.time()
                break

            # Если f(a) * f(b) < 0, то b = c, иначе a = c;
            if self.f_x.subs(self.x, self.a) * self.f_x.subs(self.x, c) < 0:
                self.b = c
            else:
                self.a = c

        # Возвращаем корень, время работы и количество итераций
        return [c, end - start, count]

    def chord_method(self):
        count = 0
        c = 1
        start = time.time()
        while True:
            count += 1

            # c = a - f(a) * (b - a) / (f(b) - f(a))
            c = self.a - self.f_x.subs(self.x, self.a) * ((self.b - self.a) / (self.f_x.subs(self.x, self.b) - self.f_x.subs(self.x, self.a)))

            if self.b - self.a < 2 * self.eps or abs(self.f_x.subs(self.x, c)) < 2 * self.delta:
                end = time.time()
                break

            if self.f_x.subs(self.x, self.a) * self.f_x.subs(self.x, c) < 0:
                self.b = c
            else:
                self.a = c

        return [c, end - start, count]


    def newton_method(self):
        count = 0
        start = time.time()
        c = self.b
        while True:
            count += 1
            c_prev = c
            c = c - self.f_x.subs(self.x, c) / diff(self.f_x, self.x).doit().subs(self.x, c).evalf(6)
            if abs(c - c_prev) < self.eps or self.f_x.subs(self.x, c) < self.delta:
                end = time.time()
                break

        return [c, end - start, count]


    def secant_method(self):
        count = 0
        start = time.time()
        c = self.b
        h = (self.b - self.a) / 100
        while True:
            count += 1
            c_prev = c
            c = c_prev - self.f_x.subs(self.x, c_prev) * h / (self.f_x.subs(self.x, c_prev + h) - self.f_x.subs(self.x, c_prev))
            h = c_prev - c
            if abs(c - c_prev) < self.eps or self.f_x.subs(self.x, c) < self.delta:
                end = time.time()
                break

        return [c, end - start, count]


    def hybrid_method(self):
        count = 0
        start = time.time()
        c = (self.a + self.b) / 2
        c_prev = c
        while True:
            count += 1
            # Если производная в точке c == 0, то применить метод дихотомии.
            # x_k = c_prev, ~x_k = c;
            if diff(self.f_x, self.x, 1).doit().subs(self.x, c).evalf() == 0:
                if self.f_x.subs(self.x, self.a) * self.f_x.subs(self.x, c) < 0:
                    self.b = c
                else:
                    self.a = c

                c = self.a - self.f_x.subs(self.x, self.a) * (self.b - self.a) / (self.f_x.subs(self.x, self.b) - self.f_x.subs(self.x, self.a))
            else:
                c = c_prev
                c = c_prev - self.f_x.subs(self.x, c_prev) / diff(self.f_x, self.x, 1).doit().subs(self.x, c).evalf()

                if abs(self.f_x.subs(self.x, c)) < abs(self.f_x.subs(self.x, c_prev)):
                    c = c_prev

                else:
                    c = 1 / 2 * (c_prev + c)

            if abs(c - c_prev) < self.eps or self.f_x(self.x, c) < self.delta:
                end = time.time()
                break

        return [c, end - start, count]
