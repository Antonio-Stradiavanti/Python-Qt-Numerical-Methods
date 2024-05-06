from NumericOperation import *
import time
from sympy import diff, evalf
class UnlinearEquationSolver(NumericOperation):
    def __init__(self):
        super().__init__()
        # c -> Предполагаемый корень
        self.a = None; self.b = None; self.c = None

        self.delta = None

    # метод половинного деления
    def dichotomy_method(self):
        # eps -> допустимая погрешность, delta -> допуск, связанный с точностью вычисления зр ф-ции
        count = 0
        start = time.time()
        while True:
            count += 1
            self.c = (self.a + self.b) / 2
            # Если b-a < 2*eps ИЛИ если |f(c)| < delta
            if self.b - self.a < 2 * self.eps or abs(self.f_x.subs(self.x, self.c)) < 2 * self.delta:
                end = time.time()
                break

            # Если f(a) * f(b) < 0, то b = c, иначе a = c;
            if self.f_x.subs(self.x, self.a) * self.f_x.subs(self.x, self.c) < 0:
                self.b = self.c
            else:
                self.a = self.c

        # Возвращаем корень, время работы и количество итераций
        return [self.c, end - start, count]

    def chord_method(self):
        count = 0
        start = time.time()
        while True:
            count += 1

            # c = a - f(a) * (b - a) / (f(b) - f(a))
            self.c = self.a - self.f_x.subs(self.x, self.a) * ((self.b - self.a) / (self.f_x.subs(self.x, self.b) - self.f_x.subs(self.x, self.a)))

            if self.b - self.a < 2 * self.eps or abs(self.f_x.subs(self.x, self.c)) < 2 * self.delta:
                end = time.time()
                break

            if self.f_x.subs(self.x, self.a) * self.f_x.subs(self.x, self.c) < 0:
                self.b = self.c
            else:
                self.a = self.c

        return [self.c, end - start, count]


    def newton_method(self):
        count = 0
        start = time.time()
        self.c = self.b
        while True:
            count += 1
            c_prev = self.c
            self.c = self.c - self.f_x.subs(self.x, self.c) / diff(self.f_x, self.x).doit().subs(self.x, self.c).evalf(6)
            if abs(self.c - c_prev) < self.eps or self.f_x.subs(self.x, self.c) < self.delta:
                end = time.time()
                break

        return [self.c, end - start, count]


    def secant_method(self):
        count = 0
        start = time.time()
        self.c = self.b
        h = (self.b - self.a) / 100
        while True:
            count += 1
            c_prev = self.c
            self.c = c_prev - self.f_x.subs(self.x, c_prev) * h / (self.f_x.subs(self.x, c_prev + h) - self.f_x.subs(self.x, c_prev))
            h = c_prev - self.c
            if abs(self.c - c_prev) < self.eps or self.f_x.subs(self.x, self.c) < self.delta:
                end = time.time()
                break

        return [self.c, end - start, count]


    def hybrid_method(self):
        count = 0
        start = time.time()
        self.c = (self.a + self.b) / 2
        c_prev = self.c
        while True:
            count += 1
            # Если производная в точке c == 0, то применить метод дихотомии.
            # x_k = c_prev, ~x_k = c;
            if diff(self.f_x, self.x, 1).doit().subs(self.x, self.c).evalf() == 0:
                if self.f_x.subs(self.x, self.a) * self.f_x.subs(self.x, self.c) < 0:
                    self.b = self.c
                else:
                    self.a = self.c

                self.c = self.a - self.f_x.subs(self.x, self.a) * (self.b - self.a) / (self.f_x.subs(self.x, self.b) - self.f_x.subs(self.x, self.a))
            else:
                self.c = c_prev
                self.c = c_prev - self.f_x.subs(self.x, c_prev) / diff(self.f_x, self.x, 1).doit().subs(self.x, self.c).evalf()

                if abs(self.f_x.subs(self.x, self.c)) < abs(self.f_x.subs(self.x, c_prev)):
                    self.c = c_prev

                else:
                    self.c = 1 / 2 * (c_prev + self.c)

            if abs(self.c - c_prev) < self.eps or self.f_x(self.x, self.c) < self.delta:
                end = time.time()
                break

        return [self.c, end - start, count]
