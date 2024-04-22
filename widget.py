# This Python file uses the following encoding: utf-8

import time
import sympy as smp
import re

from enum import Enum
from sympy import symbols, latex, sympify
from PySide6.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QVBoxLayout,  QPushButton, QLabel, QPlainTextEdit

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        # --- Свойства
        self.a = None; self.b = None; self.eps = None
        self.f_x = None
        self.x = symbols('x')

        self.isIntegrateEnabled = False

        # --- Настраиваем элементы управления
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Калькулятор производных и интегралов")
        self.ui.tabWidget.setTabText(0, "Численное интегрирование")
        self.ui.tabWidget.setTabText(1, "Численное дифференцирование")
        self.ui.output.setVisible(False)
        self.resize(750, 482)
        self.ui.integrateButton.setEnabled(self.isIntegrateEnabled)

        self.initDiffTab()

        # --- Раскрашиваем элементы управления
        # self.setStyleSheet("""
        #     QWidget {{
        #         background: {bg_color};
        #         background-clip: content;
        #         border: 0px;
        #     }} QPushButton {{
        #         background-color: {button_color};
        #         color: {text_color};
        #         border-radius: 24px;
        #     }} QPushButton:hover {{
        #         background-color: #427B58;
        #         color: {bg_color};
        #     }} QPushButton:disabled {{
        #         background-color: {input_field_color};
        #         color: {text_color};
        #     }} QPlainTextEdit {{
        #         background-color: {input_field_color};
        #         color: {text_color};
        #         placeholder-text-color: {text_color};
        #         border: {border_width} solid {border_color};
        #     }} QLabel {{
        #         color: {text_color};
        #     }} QTabWidget::pane {{
        #         border-top: {border_width} solid {border_color};
        #         margin-top: -2px;
        #     }} QTabBar::tab {{
        #         background: {bg_color};
        #         padding-left: {tab_padding}; padding-right: {tab_padding}; padding-bottom: 3px; padding-top: 3px;
        #         border-bottom: {border_width} solid {border_color};
        #     }} QTabBar::tab:selected {{
        #         background: {input_field_color};
        #         border-bottom: {border_width} solid {selected_tab_border_color};
        #     }} QDoubleSpinBox {{
        #         background: {input_field_color};
        #         border: {border_width} solid {border_color};
        #     }}
        #     """.format(
        #         tab_padding="12px", button_color="#689D6A", bg_color="#FBF1C7", input_field_color="#EBDBB2",
        #     border_color="#928374",
        #         border_width="2px", text_color="#3C3836", selected_tab_border_color="#D65D0E"
        #     )
        # )
        # --- Сигналы и слоты
        self.ui.saveInputButton.clicked.connect(self.on_integrand_save)
        self.ui.integrateButton.clicked.connect(self.on_integrateButton)
        self.ui.integrateButton.clicked.connect(self.on_reset)
    class NewCotQuads(Enum):
        TRAPEZOID = 1
        SIMPSON = 2
        NEWTON = 3
    def on_integrand_save(self):
        self.on_reset()

        # ---
        self.a = self.ui.aSpinBox.value()
        self.b = self.ui.bSpinBox.value()
        self.eps = self.ui.epsSpinBox.value()
        try:
            expr = re.sub(r'(?:e|exp)\s*(?=[*\/\-\+%*])', "exp(1)",  self.ui.plainTextEdit.toPlainText())
            expr = re.sub(r'e\((.*?)\)', r'exp(\1)', expr)
            self.f_x = sympify(
                expr
            )
            if self.f_x.has(smp.zoo) or self.f_x.has(smp.nan):
                raise ValueError()
            if self.a < self.b :
                latex_integral = f"$$\\int_{{ {str(self.a)} }}^{{ {str(self.b)} }}({latex(self.f_x)}) dx;$$"
            elif self.a > self.b:
                latex_integral = f"$$-\\int_{{ {str(self.b)} }}^{{ {str(self.a)} }}({latex(self.f_x)}) dx;$$"

            self.ui.webEngine.setHtml("""
            <html><head>
                 <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
                 </script></head>
                 <body>
                     <p><mathjax style="font-size:2.3em">""" + latex_integral + """\n$$\\epsilon = """ + str(self.eps) +
                                      """.$$</mathjax></p>
                </body>
            </html>
            """)
            self.isIntegrateEnabled = True

        except (ValueError, TypeError):
            self.f_x = None
            self.ui.webEngine.setHtml("""
            <html><body>
            <p> Некорректные входные данные </p>
            </body></html>
            """)
            isIntegrateEnabled = False

        finally:
            self.ui.integrateButton.setEnabled(self.isIntegrateEnabled)
    # Инициализация
    def initDiffTab(self):
        self.ui.tableFunction.setVisible(False)
        self.ui.symbolicDiffMe.setEnabled(False)
        self.ui.tableDiffMe.setEnabled(False)

        self.ui.symbolicTextEdit.setPlaceholderText("""Введите ф-цию.\nИнформация о используемой системе обозначений: \n\t- exp() -> показательная ф-ция с числом Эйлера в основании;\n\t- ** -> операция возведения в степень;\n\t- * / + - -> операции умножение, деление, сложение и вычитание соответственно.
                   """)

        # funcGroupBoxLayout.addLayout(inputLayout); funcGroupBoxLayout.addLayout(previewLayout)
        # inputLayout.addWidget(inputFunc)
        self.ui.table.clicked.connect(self.handleRadioButton)
        self.ui.symbolic.clicked.connect(self.handleRadioButton)

    def handleRadioButton(self):
        if self.ui.table.isChecked() :
            self.ui.tableFunction.setVisible(True)
            self.ui.symbolicFunction.setVisible(False)
            self.ui.userEval.setText("ε =")
        else:
            self.ui.tableFunction.setVisible(False)
            self.ui.symbolicFunction.setVisible(True)
            self.ui.userEval.setText("M =")

    # Бизнес логика
    def on_integrateButton(self):
        def trapRule(n):
            h = (self.b-self.a)/n
            i_r = 0; i_t = (self.f_x.subs(self.x, self.a) + self.f_x.subs(self.x, self.b))/2
            for i in range(1, n):
               i_r += self.f_x.subs(self.x, self.a + i*h)

            return h*(i_t + i_r)
        def simpRule(n):
            h = (self.b - self.a) / n
            s = 0
            for i in range(n):
                s += (1/6)*self.f_x.subs(self.x, self.a + i*h) + (2/3)*self.f_x.subs(self.x, self.a + (i + .5)*h) + (1/6)*self.f_x.subs(self.x, self.a + (i + 1)*h)
            return s*h
        def newtonRule(n):
            h = (self.b - self.a) / n;
            s = 0
            for i in range(n):
                s += ((1 / 8) *  self.f_x.subs(self.x, self.a + i * h) + (3 / 8) *  self.f_x.subs(self.x, self.a + (i + 1 / 3) * h) + (3 / 8) * self.f_x.subs(self.x, self.a + (i + 2 / 3) * h) + (1 / 8) *  self.f_x.subs(self.x, self.a + (i + 1) * h))
            return s * h

        def runge(quad_type, old_res, n):
            n *= 2; fact = 1; delta = 1
            match quad_type:
                case self.NewCotQuads.TRAPEZOID:
                    new_res = trapRule(n)
                    fact = 3
                case self.NewCotQuads.SIMPSON:
                    new_res = simpRule(n)
                    fact = 15
                case self.NewCotQuads.NEWTON:
                    new_res = newtonRule(n)
                    fact = 15
            delta = abs(new_res - old_res) / fact
            if delta < self.eps:
                return [new_res, delta]
            else:
                return runge(quad_type, new_res, n)
        # --- Скрываем один GroupBox, показываем другой
        self.ui.showInput.setVisible(False)
        self.ui.output.setVisible(True)
        # --- Вызываем замыкания.
        it_me = [(lambda l_n: trapRule(l_n), self.ui.trapRuleOutput, self.NewCotQuads.TRAPEZOID),
                 (lambda l_n: simpRule(l_n), self.ui.simpRuleOutput, self.NewCotQuads.SIMPSON),
                 (lambda l_n: newtonRule(l_n), self.ui.newtonRuleOutput, self.NewCotQuads.NEWTON)]
        for met, field, rule in it_me:
            n = 100; old_res = 0
            t0 = time.time()
            old_res = met(n)
            res = runge(rule, old_res, n)
            t1 = time.time()
            field.setText(f"I = {res[0].evalf(6)}; δ = {res[1].evalf(6)}; t = {round((t1-t0)*1000, 6)}мс")
    def on_reset(self):
        for field in [self.ui.trapRuleOutput, self.ui.simpRuleOutput, self.ui.newtonRuleOutput]:
            field.setText("")
        self.ui.output.setVisible(False)
        self.ui.showInput.setVisible(True)
        self.ui.integrateButton.setEnabled(False)
        self.ui.webEngine.setHtml("")
