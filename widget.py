# This Python file uses the following encoding: utf-8
from NumericIntegration import *
from NumericDifferentiation import *
import time
import sympy as smp
import re
from sympy import symbols, latex, sympify
from PySide6.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QVBoxLayout,  QPushButton, QLabel, QPlainTextEdit, QSizePolicy, QSpacerItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        # Конфигурация виджета верзнего уровня
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Калькулятор производных и интегралов")
        self.ui.tabWidget.setTabText(0, "Численное интегрирование")
        self.ui.tabWidget.setTabText(1, "Численное дифференцирование")
        self.ui.output.setVisible(False)

        # --- Свойства
        self.numeric_integration = NumericIntegration()
        self.numeric_differentiation = NumericDifferentiation()
        # --- Конфигурация вкладок управления

        self.__initIntegrateTab()
        self.__initDiffTab()

        # --- Раскрашиваем элементы управления
        #     """.format(
        #         tab_padding="12px", button_color="#689D6A", bg_color="#FBF1C7", input_field_color="#EBDBB2",
        #     border_color="#928374",
        #         border_width="2px", text_color="#3C3836", selected_tab_border_color="#D65D0E"
        #     )
        # )
        # --- Связываем сигналы и слоты
        #self.ui.saveInputButton.clicked.connect(self.__handleSymbolicInput)


    def __initIntegrateTab(self):
        self.ui.integrateButton.setEnabled(False)

        self.ui.integrateTextEdit.setPlaceholderText("""Введите подынтегральную ф-цию.\nИнформация о используемой системе обозначений: \n\t- exp() -> показательная ф-ция с числом Эйлера в основании;\n\t- ** -> операция возведения в степень;\n\t- * / + - -> операции умножение, деление, сложение и вычитание соответственно.
                           """)
        self.ui.integrateButton.clicked.connect(self.on_integrateButton)
        self.ui.integrateButton.clicked.connect(self.on_reset)
        self.ui.integrateSaveFunc.clicked.connect(self.on_integrandInput)

    def __initDiffTab(self):
        self.ui.tableFunction.setVisible(False)

        self.ui.diffTableButton.setEnabled(False)
        self.ui.diffSymbolicButton.setEnabled(False)


        self.ui.diffTextEdit.setPlaceholderText("""Введите дифференцируемую ф-цию.\nИнформация о используемой системе обозначений: \n\t- exp() -> показательная ф-ция с числом Эйлера в основании;\n\t- ** -> операция возведения в степень;\n\t- * / + - -> операции умножение, деление, сложение и вычитание соответственно.
                   """)

        self.ui.diffTableWidget.setRowCount(2)
        self.__on_resetTable_clicked()
        # funcGroupBoxLayout.addLayout(inputLayout); funcGroupBoxLayout.addLayout(previewLayout)
        # inputLayout.addWidget(inputFunc)
        self.ui.table.clicked.connect(self.__on_radioButton_clicked)
        self.ui.symbolic.clicked.connect(self.__on_radioButton_clicked)

        self.ui.addColumn.clicked.connect(lambda: self.ui.diffTableWidget.insertColumn(self.ui.diffTableWidget.columnCount()))

        self.ui.resetTable.clicked.connect(self.__on_resetTable_clicked)

        self.ui.removeColumn.clicked.connect(
            lambda: self.ui.diffTableWidget.removeColumn(self.ui.diffTableWidget.columnCount() - 1))

        self.ui.diffSaveFuncInput.clicked.connect(self.on_diffFunctionInput)
        self.ui.diffSaveTableInput.clicked.connect(self.on_diffTableInput)

        self.ui.diffTableButton.clicked.connect(self.on_diffButton)
        self.ui.diffSymbolicButton.clicked.connect(self.on_diffButton)

    def __on_symbolicInput(self,  to_display, met):
        # ---
        isButtonEnabled = True
        if met == NumericMethod.INTEGRATION:
            text_edit = self.ui.integrateTextEdit
            operation = self.numeric_integration
            button = self.ui.integrateButton
            web_engine = self.ui.integrateWebEngine
        else:
            text_edit = self.ui.diffTextEdit
            operation = self.numeric_differentiation
            if self.ui.symbolic.isChecked():
                button = self.ui.diffSymbolicButton
            else:
                button = self.ui.diffTableButton

            web_engine = self.ui.diffWebEngine
        try:
            # expr = text_edit.toPlainText()
            # expr = re.sub(r'(?:e|exp)\s*(?=[*\/\-\+%*])', "exp(1)", text_edit.toPlainText())
            # expr = re.sub(r'e\((.*?)\)', r'exp(\1)', expr)
            operation.f_x = sympify(text_edit.toPlainText())

            if operation.f_x.has(smp.zoo) or operation.f_x.has(smp.nan):
                raise ValueError()
            to_display = to_display.replace("f_x", latex(operation.f_x))

            web_engine.setHtml(f"""
            <html>
                <head>
                    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
                    </script>
                </head>
                <body>
                    <p>
                        <mathjax style="font-size:1.5em">
                            {to_display}
                        </mathjax>
                    </p>
                </body>
            </html>""")
        except (ValueError, TypeError):
            web_engine.setHtml("""
            <html><body>
            <p> Некорректные входные данные </p>
            </body></html>
            """)
            operation.f_x = None
            isButtonEnabled = False

        finally:
            button.setEnabled(isButtonEnabled)


    def on_integrandInput(self):
        self.numeric_integration.a = self.ui.aSpinBox.value()
        self.numeric_integration.b = self.ui.bSpinBox.value()
        self.numeric_integration.eps = self.ui.epsSpinBox.value()

        if self.numeric_integration.a < self.numeric_integration.b:
            latex_integral = f"$$\\int_{{ {str(self.numeric_integration.a)} }}^{{ {str(self.numeric_integration.b)} }}(f_x) dx;$$"
        else:
            latex_integral = f"$$-\\int_{{ {str(self.numeric_integration.b)} }}^{{ {str(self.numeric_integration.a)} }}(f_x) dx; \\epsilon = {self.numeric_integration.eps}$$"

        self.__on_symbolicInput(latex_integral, NumericMethod.INTEGRATION)


    def on_diffFunctionInput(self):
        self.numeric_differentiation.M = self.ui.diffCloseness
        if self.ui.diffOrd1.isChecked():
            latex_derivative = "$$\\frac{d(f_x)}{dx}$$"
        else:
            latex_derivative = "$$\\frac{d^{2}(f_x)}{dx^{2}}$$"

        self.__on_symbolicInput(latex_derivative, NumericMethod.DIFFERENTIATION)

    # Обработка табличного ввода


    def __on_radioButton_clicked(self):
        if self.ui.table.isChecked() :
            self.ui.tableFunction.setVisible(True)
            self.ui.symbolicFunction.setVisible(False)
            self.ui.userEval.setText("ε =")
        else:
            self.ui.tableFunction.setVisible(False)
            self.ui.symbolicFunction.setVisible(True)
            self.ui.userEval.setText("M =")

    def on_diffTableInput(self):
    # Отсортировать и удалить дубликаты
        data = dict(); i =0
        while i < self.ui.diffTableWidget.columnCount():
            it0 = self.ui.diffTableWidget.item(0, i); it1 =  self.ui.diffTableWidget.item(1, i)
            try:
                if it0 is not None and it1 is not None :
                    data[float(it0.text())] = float(it1.text())
                    i+=1
                else:
                    raise ValueError()
            except ValueError:
                self.ui.diffTableWidget.removeColumn(i)

        data = {k: data[k] for k in sorted(data.keys())}

        for i in range(self.ui.diffTableWidget.columnCount()):
            k_i = list(data.keys())[i]
            self.ui.diffTableWidget.item(0, i).setText(str(k_i))
            self.ui.diffTableWidget.item(1, i).setText(str(data[k_i]))

        col_count = self.ui.diffTableWidget.columnCount()
        if col_count < 10:
            if col_count == 0 : self.__on_resetTable_clicked()
            else: self.ui.diffTableButton.setEnabled(False)

            self.numeric_differentiation.f_x = None
        else:
            self.ui.diffTableButton.setEnabled(True)
            self.numeric_differentiation.f_x = data

    def __on_resetTable_clicked(self):
        self.ui.diffTableWidget.clear()
        self.ui.diffTableWidget.setColumnCount(5)
        self.ui.diffTableButton.setEnabled(False)

    # Бизнес логика
    def on_integrateButton(self):

        # --- Скрываем один GroupBox, показываем другой
        self.ui.showInput.setVisible(False)
        self.ui.output.setVisible(True)
        # --- Вызываем замыкания.
        it_me = [(lambda l_n: self.numeric_integration.trapRule(l_n), self.ui.trapRuleOutput, NumericIntegration.NewCotQuads.TRAPEZOID),
                 (lambda l_n: self.numeric_integration.simpRule(l_n), self.ui.simpRuleOutput, NumericIntegration.NewCotQuads.SIMPSON),
                 (lambda l_n: self.numeric_integration.newtonRule(l_n), self.ui.newtonRuleOutput, NumericIntegration.NewCotQuads.NEWTON)]
        for met, field, rule in it_me:
            n = 100; old_res = 0
            t0 = time.time()
            old_res = met(n)
            res = self.numeric_integration.runge(rule, old_res, n)
            t1 = time.time()
            field.setText(f"I = {res[0].evalf(6)}; δ = {res[1].evalf(6)}; t = {round((t1-t0)*1000, 6)}мс")

    def on_diffButton(self):
        ...

    def on_reset(self):
        for field in [self.ui.trapRuleOutput, self.ui.simpRuleOutput, self.ui.newtonRuleOutput]:
            field.setText("")
        self.ui.output.setVisible(False)
        self.ui.showInput.setVisible(True)
        self.ui.integrateButton.setEnabled(False)
        self.ui.diffWebEngine.setHtml("")
