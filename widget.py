# This Python file uses the following encoding: utf-8
from NumericIntegration import *
from NumericDifferentiation import *
from NonlinearEquationSolver import *

import time
import sympy as smp
import re
import csv
from sympy import symbols, latex, sympify, log, sqrt

from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QPlainTextEdit, QFileDialog, QTableWidgetItem
)

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
        self.ui.tabWidget.setTabText(2, "Решение нелинейных уравнений")
        self.ui.output.setVisible(False)

        # --- Свойства
        self.numeric_integration = NumericIntegration()
        self.numeric_differentiation = NumericDifferentiation()
        self.nonlinear_equation_solvers = [NonlinearEquationSolver(), NonlinearEquationSolver(), NonlinearEquationSolver()]

        self.placeHolder = "\n\t- exp() ➡️ показательная ф-ция с числом Эйлера в основании;\n\t- ** ➡️ операция возведения в степень;\n\t- * / + - ➡️ операции умножение, деление, сложение и вычитание соответственно."
        # --- Конфигурация вкладок управления

        self.__init_integrateTab()
        self.__init_diffTab()
        self.__init_solverTab()

        # --- Раскрашиваем элементы управления
        #     """.format(
        #         tab_padding="12px", button_color="#689D6A", bg_color="#FBF1C7", input_field_color="#EBDBB2",
        #     border_color="#928374",
        #         border_width="2px", text_color="#3C3836", selected_tab_border_color="#D65D0E"
        #     )
        # )
        # --- Связываем сигналы и слоты
        #self.ui.saveInputButton.clicked.connect(self.__handleSymbolicInput)


    def __init_integrateTab(self):
        self.ui.integrateButton.setEnabled(False)

        self.ui.integrateTextEdit.setPlaceholderText("Введите подынтегральную ф-цию.\n" + "Информация о используемой системе обозначений" + self.placeHolder)
        self.ui.integrateButton.clicked.connect(self.on_integrateButton)
        self.ui.integrateButton.clicked.connect(self.on_reset)
        self.ui.integrateSaveFunc.clicked.connect(self.on_integrandInput)

    def __init_diffTab(self):
        self.ui.tableFunction.setVisible(False)

        self.ui.diffTableButton.setEnabled(False)
        self.ui.diffSymbolicButton.setEnabled(False)


        self.ui.diffTextEdit.setPlaceholderText("Введите дифференцируемую ф-цию.\n" + "Информация о используемой системе обозначений" + self.placeHolder)

        self.minimusNumberOfValidRecors = 5
        self.diffTableInputLabel = QLabel(f"! В таблице должно быть не менее {self.minimusNumberOfValidRecors} записей с уникальными значениями независимой переменной.")

        self.ui.diffTableWidget.setRowCount(2)
        self.diffTableInputFieldLabels = ["x", "y"]

        self.__on_resetTable_clicked()

        tableFunctionLayout = self.ui.tableFunction.layout()
        tableFunctionLayout.insertWidget(
            tableFunctionLayout.indexOf(self.ui.diffTableWidget),
            self.diffTableInputLabel
        )

        # Сигналы и слоты
        self.ui.table.clicked.connect(self.__on_radioButton_clicked)
        self.ui.symbolic.clicked.connect(self.__on_radioButton_clicked)

        self.ui.addColumn.clicked.connect(lambda: self.ui.diffTableWidget.insertColumn(self.ui.diffTableWidget.columnCount()))

        self.ui.resetTable.clicked.connect(self.__on_resetTable_clicked)

        self.ui.removeColumn.clicked.connect(
            lambda: self.ui.diffTableWidget.removeColumn(self.ui.diffTableWidget.columnCount() - 1))

        self.ui.diffSaveFuncInput.clicked.connect(self.on_diff_symbolic_saveButton)
        self.ui.diffSaveTableInput.clicked.connect(self.on_diffTableSaveInput)

        self.ui.diffTableButton.clicked.connect(self.on_diffButton)
        self.ui.diffSymbolicButton.clicked.connect(self.on_diffButton)

        self.ui.diffTableImportData.clicked.connect(self.__on_importData_clicked)
        self.ui.diffTableExportData.clicked.connect(self.__on_exportData_clicked)

    def __init_solverTab(self):
        self.ui.solver_output.setVisible(False)
        solver_methods = ["Метод дихотомии", "Метод хорд", "Метод Ньютона", "Метод секущих", "Гибридный метод Ньютона-половинного деления"]
        NonlinearEquationSolver.met_dict(solver_methods)


        self.ui.solver_methodComboBox_1.addItems(solver_methods)
        self.ui.solver_methodComboBox_2.addItems(solver_methods)
        self.ui.solver_methodComboBox_3.addItems(solver_methods)

        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 2)
        self.ui.splitter.setStretchFactor(2, 1)

        self.ui.solver_plainTextEdit_1.setPlainText("4 * x * log(x) ** 2 - 4 * sqrt(1 + x) + 5 = 0")
        self.ui.solver_plainTextEdit_1.setReadOnly(True)

        self.ui.solver_solveButton.setEnabled(False)
        self.on_solver_resetButton()

        # Сигналы и слоты
        self.ui.solver_saveButton.clicked.connect(self.on_solver_saveButton)
        self.ui.solver_solveButton.clicked.connect(self.on_solver_solveButton)
        self.ui.solver_resetButton.clicked.connect(self.on_solver_resetButton)

    def __diffResetEvalPointConstraints(self):
        self.ui.diffEvalPoint.setMinimum(-100000)
        self.ui.diffEvalPoint.setMaximum(100000)
        self.ui.diffEvalPoint.setValue(0)

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


    def on_diff_symbolic_saveButton(self):
        self.numeric_differentiation.M = self.ui.diffCloseness
        if self.ui.diffOrd1.isChecked():
            latex_derivative = "$$\\frac{d(f_x)}{dx}$$"
        else:
            latex_derivative = "$$\\frac{d^{2}(f_x)}{dx^{2}}$$"

        self.__on_symbolicInput(latex_derivative, NumericMethod.DIFFERENTIATION)

    # Обработка табличного ввода
    def __on_radioButton_clicked(self):
        self.__on_resetTable_clicked()

        if self.ui.table.isChecked() :
            self.ui.tableFunction.setVisible(True)
            self.ui.symbolicFunction.setVisible(False)
            self.ui.diffCloseness_label.setText("ε =")
        else:
            self.ui.tableFunction.setVisible(False)
            self.ui.symbolicFunction.setVisible(True)
            self.ui.diffCloseness_label.setText("M =")

    def on_diffTableSaveInput(self):
    # Отсортировать и удалить дубликаты
        data = dict(); i = 0
        while i < self.ui.diffTableWidget.columnCount():
            it0 = self.ui.diffTableWidget.item(0, i); it1 = self.ui.diffTableWidget.item(1, i)
            try:
                if it0 is not None and it1 is not None :
                    data[float(it0.text())] = float(it1.text())
                    i+=1
                else:
                    raise ValueError()
            except ValueError:
                self.ui.diffTableWidget.removeColumn(i)

        data = {k: data[k] for k in sorted(data.keys())}

        j = 0
        for i in data.keys():
            self.ui.diffTableWidget.item(0, j).setText(str(i))
            self.ui.diffTableWidget.item(1, j).setText(str(data[i]))
            j+=1

        col_count = self.ui.diffTableWidget.columnCount()

        try:
            if col_count < self.minimusNumberOfValidRecors:
                if col_count == 0 : self.__on_resetTable_clicked()
                else:
                    self.diffTableInputLabel.setText("Заданная сетка содержит недостаточное количество узлов")
                    raise ValueError

            else:
                data_keys = list(data.keys())
                d = data_keys[1] - data_keys[0]

                if any(data_keys[i + 1] - data_keys[i] != d for i in range(len(data_keys) - 1)):
                    self.diffTableInputLabel.setText("Заданная сетка не является равномерной")
                    raise ValueError
                else:
                    self.ui.diffTableButton.setEnabled(True)
                    self.ui.diffTableExportData.setEnabled(True)

                    self.ui.diffEvalPoint.setMinimum(data_keys[0])
                    self.ui.diffEvalPoint.setMaximum(data_keys[-1])
                    self.ui.diffEvalPoint.setValue(data_keys[2])

                    self.numeric_differentiation.f_x = data
                    self.numeric_differentiation.h_0 = d

        except ValueError:
            self.ui.diffTableButton.setEnabled(False)
            self.ui.diffTableExportData.setEnabled(False)

    def __on_resetTable_clicked(self):
        self.__diffResetEvalPointConstraints()

        self.diffTableInputLabel.setText(f"! В таблице должно быть не менее {self.minimusNumberOfValidRecors} записей с уникальными значениями независимой переменной.")
        self.ui.diffTableWidget.clear()

        self.ui.diffTableWidget.setColumnCount(5)
        self.ui.diffTableWidget.setVerticalHeaderLabels(self.diffTableInputFieldLabels)

        self.ui.diffTableButton.setEnabled(False)
        self.ui.diffTableExportData.setEnabled(False)

    def __on_importData_clicked(self):
        filePath = QFileDialog.getOpenFileName(self, "Выберите csv файл для чтения", "",
        "CSV файлы (*.csv);;Все файлы (*.*)", "", QFileDialog.Option.ReadOnly)

        if len(filePath) == 0:
            self.diffTableInputLabel.setText("Файл для чтения не выбран")
            return

        try:
            with open(filePath[0], newline='', encoding='utf-8') as file:

                my_reader = csv.DictReader(file, fieldnames=self.diffTableInputFieldLabels, delimiter=',')
                fisrt_row = next(iter(my_reader))

                lx = self.diffTableInputFieldLabels[0]; ly = self.diffTableInputFieldLabels[1]
                if len(fisrt_row.keys()) == 2 and lx in fisrt_row[lx] and ly in fisrt_row[ly]:
                    i = 0
                    self.__on_resetTable_clicked()
                    for row in my_reader:
                        if i >= self.ui.diffTableWidget.columnCount():
                            self.ui.diffTableWidget.insertColumn(i)

                        self.ui.diffTableWidget.setItem(0, i, QTableWidgetItem(row[lx]))
                        self.ui.diffTableWidget.setItem(1, i, QTableWidgetItem(row[ly]))

                        i+=1

                    self.diffTableInputLabel.setText("Данные успешно загружены из файла " + file.name)

                else:
                    raise TypeError()

        except OSError:
            self.diffTableInputLabel.setText("Возникла ошибка при открытии файла: " + file.name + " на "
                                                                                                                "чтение")
        except TypeError:
            self.diffTableInputLabel.setText("Открыт файл некорректного формата, корректные входные данные должны "
                                             "содержать 2 столбца "
                                             "x, y")
        except:
            self.diffTableInputLabel.setText("Возникла ошибка при работе с файлом: " + file.name)

    def __on_exportData_clicked(self):
        filePath = QFileDialog.getSaveFileName(self, "Выберите csv файл для записи", "", "CSV файлы (*.csv);;Все файлы (*.*)")

        if len(filePath) == 0:
            self.diffTableInputLabel.setText("Файл для записи не выбран")
            return

        try:
            with open(filePath[0], "w", newline='', encoding='utf-8') as file:
                my_writer = csv.DictWriter(file, fieldnames=self.diffTableInputFieldLabels)

                my_writer.writeheader()

                ks = self.diffTableInputFieldLabels

                for i in range(self.ui.diffTableWidget.columnCount()):
                    vls = [self.ui.diffTableWidget.item(j, i).text() for j in range(2)]
                    my_writer.writerow(dict(zip(ks, vls)))

        except OSError:
           self.diffTableInputLabel.setText("Возникла ошибка при открытии файла: " + file.name + "на запись")
        except:
            self.diffTableInputLabel.setText("Возникла ошибка при работе с файлом: " + file.name)

    def __set_latex_output(self, s):
        return f"""
               <html>
                   <head>
                       <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
                   </script>
                   </head>
                       <body>
                           <p><mathjax style="font-size:1.5em">
                           $${s}$$            
                           </mathjax></p>
                       </body>
                   </html    
           """
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
        x0 = self.ui.diffEvalPoint.value()
        if self.ui.diffOrd1.isChecked(): order = 1
        else: order = 2

        if self.ui.symbolic.isChecked():
            res = self.numeric_differentiation.symbolic_function(x0, order, self.ui.diffCloseness.value())
        else:
            res = self.numeric_differentiation.table_function(x0, order)

        self.ui.diffOutput.setHtml(self.__set_latex_output(f"\\frac{{df}}{{dx}} = {round(res[0], 6)}; \ \\epsilon = {round(res[1], 6)}; \ g(h) = {res[2]})"))

    def on_reset(self):
        for field in [self.ui.trapRuleOutput, self.ui.simpRuleOutput, self.ui.newtonRuleOutput]:
            field.setText("")
        self.ui.output.setVisible(False)
        self.ui.showInput.setVisible(True)
        self.ui.integrateButton.setEnabled(False)
        self.ui.diffWebEngine.setHtml("")


    def on_solver_saveButton(self):
        if not len(self.ui.solver_plainTextEdit_2.toPlainText()) or not len(self.ui.solver_plainTextEdit_3.toPlainText()):
            self.ui.solver_solveButton.setEnabled(False)
            return

        self.ui.solver_inputSaved.setVisible(True)
        self.ui.solver_output.setVisible(False)

        F = [self.ui.solver_plainTextEdit_1.toPlainText(), self.ui.solver_plainTextEdit_2.toPlainText(), self.ui.solver_plainTextEdit_3.toPlainText()]
        A = [self.ui.solver_aSpinBox_1.value(), self.ui.solver_aSpinBox_2.value(), self.ui.solver_aSpinBox_3.value()]
        B = [self.ui.solver_bSpinBox_1.value(), self.ui.solver_bSpinBox_2.value(), self.ui.solver_bSpinBox_3.value()]
        E = [self.ui.solver_epsSpinBox_1.value(), self.ui.solver_epsSpinBox_2.value(), self.ui.solver_epsSpinBox_3.value()]
        D = [self.ui.solver_deltaSpinBox_1.value(), self.ui.solver_deltaSpinBox_2.value(), self.ui.solver_deltaSpinBox_3.value()]

        flag = False

        try:
            for i in range(3):
                expr = sympify((re.sub("=.*0", "", F[i])).strip())
                if expr.has(smp.zoo) or expr.has(smp.nan):
                    raise ValueError()
                self.nonlinear_equation_solvers[i].f_x = expr
                self.nonlinear_equation_solvers[i].a = A[i]
                self.nonlinear_equation_solvers[i].b = B[i]
                self.nonlinear_equation_solvers[i].eps = E[i]
                self.nonlinear_equation_solvers[i].delta = D[i]

            self.ui.solverWebEngine.setHtml(f"""
                    <html>
                        <head>
                            <script type="text/javascript"
                                src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
                            </script>
                        </head>
                        <body>
                            <p>
                                Обозначения: x — корень уравнения, t — время работы алгоритма, c — количество итераций. 
                            </p>    
                            <dl>
                                <dt>- Уравнение 1</dt>
                                <dd>$${latex(self.nonlinear_equation_solvers[0].f_x)} = 0$$</dd>
                                <dt>- Уравнение 2🤺</dt>
                                <dd>$${latex(self.nonlinear_equation_solvers[1].f_x)} = 0$$</dd>
                                <dt>- Уравнение 3</dt>
                                <dd>$${latex(self.nonlinear_equation_solvers[2].f_x)} = 0$$</dd>
                            </dl>
                        </body>
                    </html> 
                    """)
            flag = True

        except ValueError:
            self.ui.solverWebEngine.setHtml("""
            <html><body style="color:red;">
            <p>Некорректные входные данные </p>
            </body></html>
            """)
        finally:
            self.ui.solver_solveButton.setEnabled(flag)

    def on_solver_resetButton(self):
        self.ui.solver_inputSaved.setVisible(True)
        self.ui.solver_output.setVisible(False)

        self.ui.solver_plainTextEdit_2.setPlainText("")
        self.ui.solver_plainTextEdit_3.setPlainText("")

        self.ui.solverWebEngine.setHtml(f"""
            <html>
                <head>
                    <script type="text/javascript"
                        src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
                    </script>
                </head>
                <body style="color:gray;">
                    <p>Информация о используемой системе обозначений:</p>
                    <ul>
                    {self.placeHolder.replace("\n\t", "</li><li>").replace("- ", "")} 
                    </ul>  
                </body>
            </html> 
            """)

    def on_solver_solveButton(self):
        self.ui.solver_inputSaved.setVisible(False)
        self.ui.solver_output.setVisible(True)

        # Если не введена ф-ция
        M = [self.ui.solver_methodComboBox_1.currentText(), self.ui.solver_methodComboBox_2.currentText(), self.ui.solver_methodComboBox_3.currentText()]
        S = [self.ui.solver_equationOutput_1, self.ui.solver_equationOutput_2, self.ui.solver_equationOutput_3]

        for i in range(3):
            s = self.nonlinear_equation_solvers[i].solve(M[i])
            S[i].setHtml(self.__set_latex_output(f"x = {s[0]}; t = {s[1]}; c = {s[2]}"))