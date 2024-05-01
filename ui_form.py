# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import res_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1347, 482)
        Widget.setMinimumSize(QSize(732, 482))
        Widget.setMaximumSize(QSize(2000, 500))
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.integrateTab = QWidget()
        self.integrateTab.setObjectName(u"integrateTab")
        self.horizontalLayout_3 = QHBoxLayout(self.integrateTab)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 0, 12, 0)
        self.input = QGroupBox(self.integrateTab)
        self.input.setObjectName(u"input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setMinimumSize(QSize(360, 0))
        self.input.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.input)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 3, 6, 6)
        self.label = QLabel(self.input)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setItalic(False)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)

        self.integrateTextEdit = QPlainTextEdit(self.input)
        self.integrateTextEdit.setObjectName(u"integrateTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.integrateTextEdit.sizePolicy().hasHeightForWidth())
        self.integrateTextEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.integrateTextEdit)

        self.label_2 = QLabel(self.input)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.aLayout = QHBoxLayout()
        self.aLayout.setSpacing(12)
        self.aLayout.setObjectName(u"aLayout")
        self.label_3 = QLabel(self.input)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.aLayout.addWidget(self.label_3)

        self.aSpinBox = QDoubleSpinBox(self.input)
        self.aSpinBox.setObjectName(u"aSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.aSpinBox.sizePolicy().hasHeightForWidth())
        self.aSpinBox.setSizePolicy(sizePolicy2)
        self.aSpinBox.setDecimals(6)
        self.aSpinBox.setMaximum(1000000000.000000000000000)

        self.aLayout.addWidget(self.aSpinBox)


        self.horizontalLayout.addLayout(self.aLayout)

        self.bLayout = QHBoxLayout()
        self.bLayout.setSpacing(12)
        self.bLayout.setObjectName(u"bLayout")
        self.label_7 = QLabel(self.input)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.bLayout.addWidget(self.label_7)

        self.bSpinBox = QDoubleSpinBox(self.input)
        self.bSpinBox.setObjectName(u"bSpinBox")
        sizePolicy2.setHeightForWidth(self.bSpinBox.sizePolicy().hasHeightForWidth())
        self.bSpinBox.setSizePolicy(sizePolicy2)
        self.bSpinBox.setDecimals(6)
        self.bSpinBox.setMaximum(1000000000.000000000000000)
        self.bSpinBox.setValue(10.000000000000000)

        self.bLayout.addWidget(self.bSpinBox)


        self.horizontalLayout.addLayout(self.bLayout)

        self.epsLayout = QHBoxLayout()
        self.epsLayout.setSpacing(12)
        self.epsLayout.setObjectName(u"epsLayout")
        self.label_8 = QLabel(self.input)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.epsLayout.addWidget(self.label_8)

        self.epsSpinBox = QDoubleSpinBox(self.input)
        self.epsSpinBox.setObjectName(u"epsSpinBox")
        sizePolicy2.setHeightForWidth(self.epsSpinBox.sizePolicy().hasHeightForWidth())
        self.epsSpinBox.setSizePolicy(sizePolicy2)
        self.epsSpinBox.setDecimals(6)
        self.epsSpinBox.setMinimum(0.000001000000000)
        self.epsSpinBox.setMaximum(0.001000000000000)
        self.epsSpinBox.setSingleStep(0.000001000000000)

        self.epsLayout.addWidget(self.epsSpinBox)


        self.horizontalLayout.addLayout(self.epsLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.integrateSaveFunc = QPushButton(self.input)
        self.integrateSaveFunc.setObjectName(u"integrateSaveFunc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.integrateSaveFunc.sizePolicy().hasHeightForWidth())
        self.integrateSaveFunc.setSizePolicy(sizePolicy3)
        self.integrateSaveFunc.setMinimumSize(QSize(360, 55))
        self.integrateSaveFunc.setMaximumSize(QSize(16777215, 55))
        self.integrateSaveFunc.setFont(font)
        self.integrateSaveFunc.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.integrateSaveFunc)


        self.horizontalLayout_3.addWidget(self.input)

        self.showInput = QGroupBox(self.integrateTab)
        self.showInput.setObjectName(u"showInput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.showInput.sizePolicy().hasHeightForWidth())
        self.showInput.setSizePolicy(sizePolicy4)
        self.showInput.setMinimumSize(QSize(360, 0))
        self.showInput.setFont(font)
        self.verticalLayout = QVBoxLayout(self.showInput)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 3, 6, 6)
        self.integrateWebEngine = QWebEngineView(self.showInput)
        self.integrateWebEngine.setObjectName(u"integrateWebEngine")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.integrateWebEngine.sizePolicy().hasHeightForWidth())
        self.integrateWebEngine.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.integrateWebEngine)

        self.integrateButton = QPushButton(self.showInput)
        self.integrateButton.setObjectName(u"integrateButton")
        sizePolicy3.setHeightForWidth(self.integrateButton.sizePolicy().hasHeightForWidth())
        self.integrateButton.setSizePolicy(sizePolicy3)
        self.integrateButton.setMinimumSize(QSize(0, 55))

        self.verticalLayout.addWidget(self.integrateButton)


        self.horizontalLayout_3.addWidget(self.showInput)

        self.output = QGroupBox(self.integrateTab)
        self.output.setObjectName(u"output")
        self.output.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy6)
        self.output.setMinimumSize(QSize(400, 0))
        self.output.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.output)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 3, 6, 6)
        self.label_4 = QLabel(self.output)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_4.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_4)

        self.trapRuleOutput = QTextEdit(self.output)
        self.trapRuleOutput.setObjectName(u"trapRuleOutput")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.trapRuleOutput.sizePolicy().hasHeightForWidth())
        self.trapRuleOutput.setSizePolicy(sizePolicy7)
        self.trapRuleOutput.setMaximumSize(QSize(16777215, 55))
        font3 = QFont()
        font3.setPointSize(14)
        self.trapRuleOutput.setFont(font3)
        self.trapRuleOutput.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.trapRuleOutput)

        self.label_5 = QLabel(self.output)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_5)

        self.simpRuleOutput = QTextEdit(self.output)
        self.simpRuleOutput.setObjectName(u"simpRuleOutput")
        sizePolicy7.setHeightForWidth(self.simpRuleOutput.sizePolicy().hasHeightForWidth())
        self.simpRuleOutput.setSizePolicy(sizePolicy7)
        self.simpRuleOutput.setMaximumSize(QSize(16777215, 55))
        self.simpRuleOutput.setFont(font3)
        self.simpRuleOutput.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.simpRuleOutput)

        self.label_6 = QLabel(self.output)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_6)

        self.newtonRuleOutput = QTextEdit(self.output)
        self.newtonRuleOutput.setObjectName(u"newtonRuleOutput")
        sizePolicy7.setHeightForWidth(self.newtonRuleOutput.sizePolicy().hasHeightForWidth())
        self.newtonRuleOutput.setSizePolicy(sizePolicy7)
        self.newtonRuleOutput.setMaximumSize(QSize(16777215, 55))
        self.newtonRuleOutput.setFont(font3)
        self.newtonRuleOutput.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.newtonRuleOutput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(self.output)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy8)
        self.pushButton_3.setMinimumSize(QSize(360, 55))
        self.pushButton_3.setMaximumSize(QSize(16777215, 55))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIconSize(QSize(16, 16))

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_3.addWidget(self.output)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.tabWidget.addTab(self.integrateTab, "")
        self.diffTab = QWidget()
        self.diffTab.setObjectName(u"diffTab")
        self.verticalLayout_4 = QVBoxLayout(self.diffTab)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.numDiffTableOrSymbolic = QGroupBox(self.diffTab)
        self.numDiffTableOrSymbolic.setObjectName(u"numDiffTableOrSymbolic")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.numDiffTableOrSymbolic.sizePolicy().hasHeightForWidth())
        self.numDiffTableOrSymbolic.setSizePolicy(sizePolicy9)
        self.numDiffTableOrSymbolic.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(self.numDiffTableOrSymbolic)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 3, 12, 3)
        self.symbolic = QRadioButton(self.numDiffTableOrSymbolic)
        self.symbolic.setObjectName(u"symbolic")
        self.symbolic.setChecked(True)

        self.horizontalLayout_4.addWidget(self.symbolic)

        self.table = QRadioButton(self.numDiffTableOrSymbolic)
        self.table.setObjectName(u"table")

        self.horizontalLayout_4.addWidget(self.table)


        self.horizontalLayout_6.addWidget(self.numDiffTableOrSymbolic)

        self.groupBox_2 = QGroupBox(self.diffTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.diffOrd1 = QRadioButton(self.groupBox_2)
        self.diffOrd1.setObjectName(u"diffOrd1")
        self.diffOrd1.setChecked(True)

        self.horizontalLayout_5.addWidget(self.diffOrd1)

        self.diffOrd2 = QRadioButton(self.groupBox_2)
        self.diffOrd2.setObjectName(u"diffOrd2")

        self.horizontalLayout_5.addWidget(self.diffOrd2)


        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.diffTab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.diffEvalPoint_label = QLabel(self.groupBox)
        self.diffEvalPoint_label.setObjectName(u"diffEvalPoint_label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.diffEvalPoint_label.sizePolicy().hasHeightForWidth())
        self.diffEvalPoint_label.setSizePolicy(sizePolicy10)
        self.diffEvalPoint_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.diffEvalPoint_label)

        self.diffEvalPoint = QDoubleSpinBox(self.groupBox)
        self.diffEvalPoint.setObjectName(u"diffEvalPoint")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.diffEvalPoint.sizePolicy().hasHeightForWidth())
        self.diffEvalPoint.setSizePolicy(sizePolicy11)

        self.horizontalLayout_7.addWidget(self.diffEvalPoint)

        self.diffCloseness_label = QLabel(self.groupBox)
        self.diffCloseness_label.setObjectName(u"diffCloseness_label")
        sizePolicy10.setHeightForWidth(self.diffCloseness_label.sizePolicy().hasHeightForWidth())
        self.diffCloseness_label.setSizePolicy(sizePolicy10)
        self.diffCloseness_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.diffCloseness_label)

        self.diffCloseness = QDoubleSpinBox(self.groupBox)
        self.diffCloseness.setObjectName(u"diffCloseness")
        sizePolicy11.setHeightForWidth(self.diffCloseness.sizePolicy().hasHeightForWidth())
        self.diffCloseness.setSizePolicy(sizePolicy11)

        self.horizontalLayout_7.addWidget(self.diffCloseness)


        self.horizontalLayout_6.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.funcGroupBox = QGroupBox(self.diffTab)
        self.funcGroupBox.setObjectName(u"funcGroupBox")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.funcGroupBox.sizePolicy().hasHeightForWidth())
        self.funcGroupBox.setSizePolicy(sizePolicy12)
        self.horizontalLayout_9 = QHBoxLayout(self.funcGroupBox)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableFunction = QWidget(self.funcGroupBox)
        self.tableFunction.setObjectName(u"tableFunction")
        self.tableFunc = QVBoxLayout(self.tableFunction)
        self.tableFunc.setObjectName(u"tableFunc")
        self.diffTableWidget = QTableWidget(self.tableFunction)
        self.diffTableWidget.setObjectName(u"diffTableWidget")
        sizePolicy8.setHeightForWidth(self.diffTableWidget.sizePolicy().hasHeightForWidth())
        self.diffTableWidget.setSizePolicy(sizePolicy8)
        self.diffTableWidget.setMinimumSize(QSize(0, 55))

        self.tableFunc.addWidget(self.diffTableWidget)

        self.tableButtons = QHBoxLayout()
        self.tableButtons.setSpacing(8)
        self.tableButtons.setObjectName(u"tableButtons")
        self.diffSaveTableInput = QPushButton(self.tableFunction)
        self.diffSaveTableInput.setObjectName(u"diffSaveTableInput")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.diffSaveTableInput.sizePolicy().hasHeightForWidth())
        self.diffSaveTableInput.setSizePolicy(sizePolicy13)
        self.diffSaveTableInput.setMinimumSize(QSize(55, 55))
        icon = QIcon()
        icon.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.diffSaveTableInput.setIcon(icon)
        self.diffSaveTableInput.setIconSize(QSize(20, 20))

        self.tableButtons.addWidget(self.diffSaveTableInput)

        self.addColumn = QPushButton(self.tableFunction)
        self.addColumn.setObjectName(u"addColumn")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.addColumn.sizePolicy().hasHeightForWidth())
        self.addColumn.setSizePolicy(sizePolicy14)
        self.addColumn.setMinimumSize(QSize(55, 55))
        icon1 = QIcon()
        icon1.addFile(u":/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addColumn.setIcon(icon1)
        self.addColumn.setIconSize(QSize(20, 20))

        self.tableButtons.addWidget(self.addColumn)

        self.removeColumn = QPushButton(self.tableFunction)
        self.removeColumn.setObjectName(u"removeColumn")
        sizePolicy14.setHeightForWidth(self.removeColumn.sizePolicy().hasHeightForWidth())
        self.removeColumn.setSizePolicy(sizePolicy14)
        self.removeColumn.setMinimumSize(QSize(55, 55))
        icon2 = QIcon()
        icon2.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removeColumn.setIcon(icon2)
        self.removeColumn.setIconSize(QSize(20, 20))

        self.tableButtons.addWidget(self.removeColumn)

        self.diffTableImportData = QPushButton(self.tableFunction)
        self.diffTableImportData.setObjectName(u"diffTableImportData")
        sizePolicy13.setHeightForWidth(self.diffTableImportData.sizePolicy().hasHeightForWidth())
        self.diffTableImportData.setSizePolicy(sizePolicy13)
        self.diffTableImportData.setMinimumSize(QSize(55, 55))
        icon3 = QIcon()
        icon3.addFile(u":/icons/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.diffTableImportData.setIcon(icon3)
        self.diffTableImportData.setIconSize(QSize(20, 20))

        self.tableButtons.addWidget(self.diffTableImportData)

        self.diffTableExportData = QPushButton(self.tableFunction)
        self.diffTableExportData.setObjectName(u"diffTableExportData")
        sizePolicy13.setHeightForWidth(self.diffTableExportData.sizePolicy().hasHeightForWidth())
        self.diffTableExportData.setSizePolicy(sizePolicy13)
        self.diffTableExportData.setMinimumSize(QSize(55, 55))
        icon4 = QIcon()
        icon4.addFile(u":/icons/export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.diffTableExportData.setIcon(icon4)
        self.diffTableExportData.setIconSize(QSize(20, 20))

        self.tableButtons.addWidget(self.diffTableExportData)

        self.resetTable = QPushButton(self.tableFunction)
        self.resetTable.setObjectName(u"resetTable")
        sizePolicy14.setHeightForWidth(self.resetTable.sizePolicy().hasHeightForWidth())
        self.resetTable.setSizePolicy(sizePolicy14)
        self.resetTable.setMinimumSize(QSize(55, 55))
        icon5 = QIcon()
        icon5.addFile(u":/icons/rotate-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetTable.setIcon(icon5)
        self.resetTable.setIconSize(QSize(20, 20))

        self.tableButtons.addWidget(self.resetTable)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tableButtons.addItem(self.horizontalSpacer)

        self.diffTableButton = QPushButton(self.tableFunction)
        self.diffTableButton.setObjectName(u"diffTableButton")
        sizePolicy4.setHeightForWidth(self.diffTableButton.sizePolicy().hasHeightForWidth())
        self.diffTableButton.setSizePolicy(sizePolicy4)

        self.tableButtons.addWidget(self.diffTableButton)


        self.tableFunc.addLayout(self.tableButtons)


        self.horizontalLayout_9.addWidget(self.tableFunction)

        self.symbolicFunction = QWidget(self.funcGroupBox)
        self.symbolicFunction.setObjectName(u"symbolicFunction")
        self.symbolicFuncion = QVBoxLayout(self.symbolicFunction)
        self.symbolicFuncion.setSpacing(6)
        self.symbolicFuncion.setObjectName(u"symbolicFuncion")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.diffTextEdit = QPlainTextEdit(self.symbolicFunction)
        self.diffTextEdit.setObjectName(u"diffTextEdit")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.diffTextEdit.sizePolicy().hasHeightForWidth())
        self.diffTextEdit.setSizePolicy(sizePolicy15)

        self.horizontalLayout_8.addWidget(self.diffTextEdit)

        self.diffWebEngine = QWebEngineView(self.symbolicFunction)
        self.diffWebEngine.setObjectName(u"diffWebEngine")
        sizePolicy9.setHeightForWidth(self.diffWebEngine.sizePolicy().hasHeightForWidth())
        self.diffWebEngine.setSizePolicy(sizePolicy9)

        self.horizontalLayout_8.addWidget(self.diffWebEngine)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.symbolicFuncion.addLayout(self.horizontalLayout_8)

        self.diffFuncButtons = QHBoxLayout()
        self.diffFuncButtons.setSpacing(8)
        self.diffFuncButtons.setObjectName(u"diffFuncButtons")
        self.diffSaveFuncInput = QPushButton(self.symbolicFunction)
        self.diffSaveFuncInput.setObjectName(u"diffSaveFuncInput")
        sizePolicy14.setHeightForWidth(self.diffSaveFuncInput.sizePolicy().hasHeightForWidth())
        self.diffSaveFuncInput.setSizePolicy(sizePolicy14)
        self.diffSaveFuncInput.setMinimumSize(QSize(55, 55))
        self.diffSaveFuncInput.setIcon(icon)
        self.diffSaveFuncInput.setIconSize(QSize(20, 20))

        self.diffFuncButtons.addWidget(self.diffSaveFuncInput)

        self.resetFunc = QPushButton(self.symbolicFunction)
        self.resetFunc.setObjectName(u"resetFunc")
        sizePolicy14.setHeightForWidth(self.resetFunc.sizePolicy().hasHeightForWidth())
        self.resetFunc.setSizePolicy(sizePolicy14)
        self.resetFunc.setMinimumSize(QSize(55, 55))
        self.resetFunc.setIcon(icon5)
        self.resetFunc.setIconSize(QSize(20, 20))

        self.diffFuncButtons.addWidget(self.resetFunc)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.diffFuncButtons.addItem(self.horizontalSpacer_2)

        self.diffSymbolicButton = QPushButton(self.symbolicFunction)
        self.diffSymbolicButton.setObjectName(u"diffSymbolicButton")
        sizePolicy4.setHeightForWidth(self.diffSymbolicButton.sizePolicy().hasHeightForWidth())
        self.diffSymbolicButton.setSizePolicy(sizePolicy4)

        self.diffFuncButtons.addWidget(self.diffSymbolicButton)


        self.symbolicFuncion.addLayout(self.diffFuncButtons)


        self.horizontalLayout_9.addWidget(self.symbolicFunction)


        self.verticalLayout_4.addWidget(self.funcGroupBox)

        self.numDiffOutput = QGroupBox(self.diffTab)
        self.numDiffOutput.setObjectName(u"numDiffOutput")
        sizePolicy1.setHeightForWidth(self.numDiffOutput.sizePolicy().hasHeightForWidth())
        self.numDiffOutput.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.numDiffOutput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(9, 3, 9, 9)
        self.diffOutput = QWebEngineView(self.numDiffOutput)
        self.diffOutput.setObjectName(u"diffOutput")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.diffOutput.sizePolicy().hasHeightForWidth())
        self.diffOutput.setSizePolicy(sizePolicy16)
        self.diffOutput.setMinimumSize(QSize(0, 89))

        self.gridLayout.addWidget(self.diffOutput, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.numDiffOutput)

        self.tabWidget.addTab(self.diffTab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.input.setTitle(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u044b\u043d\u0442\u0435\u0433\u0440\u0430\u043b\u044c\u043d\u0430\u044f \u0444-\u0446\u0438\u044f  f(x)", None))
        self.integrateTextEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444-\u0446\u0438\u044e", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0435\u0434\u0435\u043b\u044b \u0438\u043d\u0442\u0435\u0433\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f a, b \u0438 \u0442\u043e\u0447\u0442\u043e\u0441\u0442\u044c \u03b5", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"a =", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"b =", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u03b5 =", None))
        self.integrateSaveFunc.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.showInput.setTitle(QCoreApplication.translate("Widget", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.integrateButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0433\u0440\u0430\u043b", None))
        self.output.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0441\u0442\u0430\u0432\u043d\u0430\u044f \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0443\u0440\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0439 (n=1)", None))
        self.trapRuleOutput.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0441\u0442\u0430\u0432\u043d\u0430\u044f \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0443\u0440\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430 \u0421\u0438\u043c\u043f\u0441\u043e\u043d\u0430 (n=2)", None))
        self.simpRuleOutput.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0441\u0442\u0430\u0432\u043d\u0430\u044f \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0443\u0440\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430 \u041d\u044c\u044e\u0442\u043e\u043d\u0430 (n=3)", None))
        self.newtonRuleOutput.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">I = 32320,334734; h = 0,443434; t = 12,0343444</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.integrateTab), QCoreApplication.translate("Widget", u"Tab 1", None))
        self.numDiffTableOrSymbolic.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u0444-\u0446\u0438\u0438", None))
        self.symbolic.setText(QCoreApplication.translate("Widget", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.table.setText(QCoreApplication.translate("Widget", u"\u0422\u0430\u0431\u043b\u0438\u0447\u043d\u044b\u0439", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439", None))
        self.diffOrd1.setText(QCoreApplication.translate("Widget", u"1-\u0439", None))
        self.diffOrd2.setText(QCoreApplication.translate("Widget", u"2-\u0439", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u0447\u043a\u0443 x \u0438 \u043e\u0446\u0435\u043d\u043a\u0443 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u0438 M", None))
        self.diffEvalPoint_label.setText(QCoreApplication.translate("Widget", u"x =", None))
        self.diffCloseness_label.setText(QCoreApplication.translate("Widget", u"M =", None))
        self.funcGroupBox.setTitle(QCoreApplication.translate("Widget", u"\u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u0434\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u0443\u0435\u043c\u0443\u044e \u0444-\u0446\u0438\u044e", None))
        self.diffSaveTableInput.setText("")
        self.addColumn.setText("")
        self.removeColumn.setText("")
        self.diffTableImportData.setText("")
        self.diffTableExportData.setText("")
        self.resetTable.setText("")
        self.diffTableButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0443\u044e", None))
        self.diffTextEdit.setPlaceholderText("")
        self.diffSaveFuncInput.setText("")
        self.resetFunc.setText("")
        self.diffSymbolicButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0443\u044e", None))
        self.numDiffOutput.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diffTab), QCoreApplication.translate("Widget", u"Tab 2", None))
    # retranslateUi

