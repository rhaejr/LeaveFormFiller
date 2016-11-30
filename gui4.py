# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(787, 601)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.from_date = QtGui.QDateEdit(Form)
        self.from_date.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.from_date.setCalendarPopup(True)
        self.from_date.setObjectName(_fromUtf8("from_date"))
        self.verticalLayout_2.addWidget(self.from_date)
        self.from_time = QtGui.QTimeEdit(Form)
        self.from_time.setObjectName(_fromUtf8("from_time"))
        self.verticalLayout_2.addWidget(self.from_time)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.to_date = QtGui.QDateEdit(Form)
        self.to_date.setCalendarPopup(True)
        self.to_date.setObjectName(_fromUtf8("to_date"))
        self.verticalLayout.addWidget(self.to_date)
        self.to_time = QtGui.QTimeEdit(Form)
        self.to_time.setObjectName(_fromUtf8("to_time"))
        self.verticalLayout.addWidget(self.to_time)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.check_aftp = QtGui.QCheckBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_aftp.sizePolicy().hasHeightForWidth())
        self.check_aftp.setSizePolicy(sizePolicy)
        self.check_aftp.setObjectName(_fromUtf8("check_aftp"))
        self.horizontalLayout_2.addWidget(self.check_aftp)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radio_annual = QtGui.QRadioButton(Form)
        self.radio_annual.setObjectName(_fromUtf8("radio_annual"))
        self.gridLayout.addWidget(self.radio_annual, 0, 0, 1, 1)
        self.radio_mil = QtGui.QRadioButton(Form)
        self.radio_mil.setObjectName(_fromUtf8("radio_mil"))
        self.gridLayout.addWidget(self.radio_mil, 0, 1, 1, 1)
        self.radio_sick = QtGui.QRadioButton(Form)
        self.radio_sick.setObjectName(_fromUtf8("radio_sick"))
        self.gridLayout.addWidget(self.radio_sick, 0, 2, 1, 1)
        self.radio_lwop = QtGui.QRadioButton(Form)
        self.radio_lwop.setObjectName(_fromUtf8("radio_lwop"))
        self.gridLayout.addWidget(self.radio_lwop, 0, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.total_hours = QtGui.QTimeEdit(Form)
        self.total_hours.setObjectName(_fromUtf8("total_hours"))
        self.horizontalLayout_3.addWidget(self.total_hours)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.submit_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_btn.sizePolicy().hasHeightForWidth())
        self.submit_btn.setSizePolicy(sizePolicy)
        self.submit_btn.setAutoFillBackground(False)
        self.submit_btn.setObjectName(_fromUtf8("submit_btn"))
        self.verticalLayout_3.addWidget(self.submit_btn)
        self.remarksLabel = QtGui.QLabel(Form)
        self.remarksLabel.setObjectName(_fromUtf8("remarksLabel"))
        self.verticalLayout_3.addWidget(self.remarksLabel)
        self.remarksText = QtGui.QPlainTextEdit(Form)
        self.remarksText.setEnabled(True)
        self.remarksText.setMaximumSize(QtCore.QSize(16777215, 50))
        self.remarksText.setObjectName(_fromUtf8("remarksText"))
        self.verticalLayout_3.addWidget(self.remarksText)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "From", None))
        self.from_date.setDisplayFormat(_translate("Form", "dd-MMM-yyyy", None))
        self.label.setText(_translate("Form", "To", None))
        self.to_date.setDisplayFormat(_translate("Form", "dd-MMM-yyyy", None))
        self.check_aftp.setText(_translate("Form", "AFTP", None))
        self.radio_annual.setText(_translate("Form", "Annual", None))
        self.radio_mil.setText(_translate("Form", "Military", None))
        self.radio_sick.setText(_translate("Form", "Sick", None))
        self.radio_lwop.setText(_translate("Form", "LWOP", None))
        self.label_3.setText(_translate("Form", "Total Hours", None))
        self.total_hours.setDisplayFormat(_translate("Form", "h", None))
        self.submit_btn.setText(_translate("Form", "Submit", None))
        self.remarksLabel.setText(_translate("Form", "Remarks:", None))

