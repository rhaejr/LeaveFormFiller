import datetime as dt
from fdfgen import forge_fdf
import subprocess
from PyQt4 import QtCore, QtGui
import sys
import os
import sqlite3
from collections import OrderedDict
from pypdftk import fill_form



# Constants
NAME = "form1[0].#subform[0].Table1[0].Row2[0].TextField[0]"
SSN = "form1[0].#subform[0].Table1[0].Row2[0].TextField[1]"
ORGANIZATION = "form1[0].#subform[0].Table1[0].Row4[0].TextField[0]"

ANNUAL_FROM_DATE = "form1[0].#subform[0].Table3[0].Row3[0].DateTimeField1[0]"
ANNUAL_TO_DATE = "form1[0].#subform[0].Table3[0].Row3[0].DateTimeField2[0]"
ANNUAL_FROM_TIME = "form1[0].#subform[0].Table3[1].Row3[0].DateTimeField1[0]"
ANNUAL_TO_TIME = "form1[0].#subform[0].Table3[1].Row3[0].DateTimeField2[0]"
ANNUAL_TOTAL = "form1[0].#subform[0].Table4[0].Row2[0].TextField[0]"
ANNUAL_BOX = "form1[0].#subform[0].CheckBox1[0]"

SICK_FROM_DATE = "form1[0].#subform[0].Table3[0].Row6[0].DateTimeField7[0]"
SICK_TO_DATE = "form1[0].#subform[0].Table3[0].Row6[0].DateTimeField8[0]"
SICK_FROM_TIME = "form1[0].#subform[0].Table3[1].Row6[0].DateTimeField15[0]"
SICK_TO_TIME = "form1[0].#subform[0].Table3[1].Row6[0].DateTimeField16[0]"
SICK_TOTAL = "form1[0].#subform[0].Table4[0].Row5[0].TextField[0]"
SICK_BOX = "form1[0].#subform[0].CheckBox1[3]"

COMP_FROM_DATE = "form1[0].#subform[0].Table7[0].Row1[0].DateTimeField19[0]"
COMP_TO_DATE = "form1[0].#subform[0].Table7[0].Row1[0].DateTimeField20[0]"
COMP_FROM_TIME = "form1[0].#subform[0].Table7[0].Row1[0].DateTimeField27[0]"
COMP_TO_TIME = "form1[0].#subform[0].Table7[0].Row1[0].DateTimeField30[0]"
COMP_TOTAL = "form1[0].#subform[0].Table7[0].Row1[0].TextField[0]"
COMP_BOX = "form1[0].#subform[0].CheckBox4[0]"

OTHER_FROM_DATE = "form1[0].#subform[0].Table7[0].Row2[0].DateTimeField21[0]"
OTHER_TO_DATE = "form1[0].#subform[0].Table7[0].Row2[0].DateTimeField22[0]"
OTHER_FROM_TIME = "form1[0].#subform[0].Table7[0].Row2[0].DateTimeField28[0]"
OTHER_TO_TIME = "form1[0].#subform[0].Table7[0].Row2[0].DateTimeField31[0]"
OTHER_TOTAL = "form1[0].#subform[0].Table7[0].Row2[0].TextField[0]"
OTHER_BOX = "form1[0].#subform[0].CheckBox4[1]"

LWOP_FROM_DATE = "form1[0].#subform[0].Table7[0].Row3[0].DateTimeField23[0]"
LWOP_TO_DATE = "form1[0].#subform[0].Table7[0].Row3[0].DateTimeField24[0]"
LWOP_FROM_TIME = "form1[0].#subform[0].Table7[0].Row3[0].DateTimeField29[0]"
LWOP_TO_TIME = "form1[0].#subform[0].Table7[0].Row3[0].DateTimeField32[0]"
LWOP_TOTAL = "form1[0].#subform[0].Table7[0].Row3[0].TextField[0]"
LWOP_BOX = "form1[0].#subform[0].CheckBox4[2]"

REMARKS = "form1[0].#subform[0].Table8[0].Row2[0].TextField[0]"

SIGN_DATE = "form1[0].#subform[0].Table8[0].Row5[0].DateTimeField25[0]"

PAYDAY = "10-Nov-2016"
MISS_MONDAY = "07-Nov-2016"

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(
ssn INT PRIMARY KEY      NOT NULL,
last    TEXT NOT NULL,
first    TEXT NOT NULL,
middle    TEXT NOT NULL
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS leave_forms(
id      INT     NOT NULL,
from_date TEXT    NOT NULL,
to_date     TEXT    NOT NULL,
from_time   TEXT    NOT NULL,
to_time     TEXT    NOT NULL,
leave_type  TEXT    NOT NULL,
remarks TEXT    NOT NULL,
signed TEXT    NOT NULL,
hours INT    NOT NULL,
FOREIGN KEY(id) REFERENCES users(ssn)
);''')


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


class LeaveForm:
    def __init__(self,gui):
        self.name = ""
        self.ssn = ""
        self.gui = gui
        self.datas = {}
        self.from_date = ""
        self.to_date = ""
        self.from_time = ""
        self.to_time = ""
        self.leave_type = ""
        self.remarks = ""
        self.signed = ""
        self.hours = ""

    def fill_fields(self):
        self.datas = {REMARKS: self.remarks, NAME: self.name, SSN: self.ssn}

        if self.gui.radio_annual.isChecked():
            self.datas[ANNUAL_FROM_DATE] = self.from_date
            self.datas[ANNUAL_TO_DATE] = self.to_date
            self.datas[ANNUAL_BOX] = "1"
            self.datas[ANNUAL_FROM_TIME] = self.from_time
            self.datas[ANNUAL_TO_TIME] = self.to_time
            self.datas[ANNUAL_TOTAL] = self.hours
            self.leave_type = "Annual"

        elif self.gui.radio_sick.isChecked():
            self.datas[SICK_FROM_DATE] = self.from_date
            self.datas[SICK_TO_DATE] = self.to_date
            self.datas[SICK_BOX] = "1"
            self.datas[SICK_FROM_TIME] = self.from_time
            self.datas[SICK_TO_TIME] = self.to_time
            self.datas[SICK_TOTAL] = self.hours
            self.leave_type = "Sick"


        elif self.gui.radio_lwop.isChecked():
            self.datas[LWOP_FROM_DATE] = self.from_date
            self.datas[LWOP_TO_DATE] = self.to_date
            self.datas[LWOP_BOX] = "1"
            self.datas[LWOP_FROM_TIME] = self.from_time
            self.datas[LWOP_TO_TIME] = self.to_time
            self.datas[LWOP_TOTAL] = self.hours
            self.leave_type = "LWOP"

        elif self.gui.radio_mil.isChecked():
            self.datas[OTHER_FROM_DATE] = self.from_date
            self.datas[OTHER_TO_DATE] = self.to_date
            self.datas[OTHER_BOX] = "1"
            self.datas[OTHER_FROM_TIME] = self.from_time
            self.datas[OTHER_TO_TIME] = self.to_time
            self.datas[OTHER_TOTAL] = self.hours
            self.leave_type = "Millitary"

    def create_form(self):

        self.fill_fields()

        # fdf = forge_fdf("", self.fields, [], [], [])
        # fdf_file = open("data.fdf", "wb")
        # fdf_file.write(fdf)
        # fdf_file.close()
        fill_form("leaveForm.pdf", self.datas)
        # subprocess.call(["pdftk", "leaveForm.pdf", "fill_form", "data.fdf", "output", "output.pdf", "flatten"])



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(787, 601)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.user_list = QtGui.QComboBox(Form)
        self.user_list.setObjectName(_fromUtf8("user_list"))
        self.verticalLayout_3.addWidget(self.user_list)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.add_last4_line = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_last4_line.sizePolicy().hasHeightForWidth())
        self.add_last4_line.setSizePolicy(sizePolicy)
        self.add_last4_line.setMaximumSize(QtCore.QSize(326, 16777215))
        self.add_last4_line.setObjectName(_fromUtf8("add_last4_line"))
        self.verticalLayout_4.addWidget(self.add_last4_line)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.add_last_line = QtGui.QLineEdit(Form)
        self.add_last_line.setObjectName(_fromUtf8("add_last_line"))
        self.verticalLayout_5.addWidget(self.add_last_line)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_6.addWidget(self.label_7)
        self.add_first_line = QtGui.QLineEdit(Form)
        self.add_first_line.setObjectName(_fromUtf8("add_first_line"))
        self.verticalLayout_6.addWidget(self.add_first_line)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_8 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_7.addWidget(self.label_8)
        self.add_middle_line = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_middle_line.sizePolicy().hasHeightForWidth())
        self.add_middle_line.setSizePolicy(sizePolicy)
        self.add_middle_line.setObjectName(_fromUtf8("add_middle_line"))
        self.verticalLayout_7.addWidget(self.add_middle_line)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.add_submit_btn = QtGui.QPushButton(Form)
        self.add_submit_btn.setObjectName(_fromUtf8("add_submit_btn"))
        self.horizontalLayout_4.addWidget(self.add_submit_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
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
        self.form_table = QtGui.QTableWidget(Form)
        self.form_table.setObjectName(_fromUtf8("form_table"))
        self.form_table.setColumnCount(0)
        self.form_table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.form_table)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        self.non_generated_code()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_6.setText(_translate("Form", "Select Name", None))
        self.label_4.setText(_translate("Form", "Last 4", None))
        self.label_5.setText(_translate("Form", "last Name:", None))
        self.label_7.setText(_translate("Form", "First Name:", None))
        self.label_8.setText(_translate("Form", "Middle Initial", None))
        self.add_submit_btn.setText(_translate("Form", "Add", None))
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

    def non_generated_code(self):
        self.connections()
        self.defaults()
        self.logic()
        self.fill_drop_down()
        self.leave_form = LeaveForm(self)
        # self.user_table()

    # noinspection PyUnresolvedReferences
    def connections(self):

        self.submit_btn.clicked.connect(self.submit_leave)
        self.check_aftp.clicked.connect(self.logic)
        self.radio_mil.clicked.connect(self.logic)
        self.radio_sick.clicked.connect(self.logic)
        self.radio_lwop.clicked.connect(self.logic)
        self.radio_annual.clicked.connect(self.logic)
        self.from_time.timeChanged.connect(self.update_hours)
        self.to_time.timeChanged.connect(self.update_hours)
        self.add_submit_btn.clicked.connect(self.add_user)
        self.user_list.activated[str].connect(self.user_select)

    def defaults(self):
        self.from_date.setDate(QtCore.QDate.currentDate())
        self.to_date.setDate(QtCore.QDate.currentDate())
        self.from_time.setTime(QtCore.QTime(7, 0, 0))
        self.to_time.setTime(QtCore.QTime(16, 30, 0))
        self.user_dict = {}
        self.user_dict = OrderedDict(sorted(self.user_dict.items(), key=lambda t: t[0]))

    def submit_leave(self):

        self.leave_form.from_date = self.from_date.date().toPyDate().strftime("%d-%b-%Y")
        self.leave_form.to_date = self.to_date.date().toPyDate().strftime("%d-%b-%Y")
        self.leave_form.from_time = self.from_time.time().toPyTime().strftime("%H%M")
        self.leave_form.to_time = self.to_time.time().toPyTime().strftime("%H%M")
        self.leave_form.remarks = self.remarksText.toPlainText()
        self.leave_form.hours = self.total_hours.time().toPyTime().strftime("%H")
        self.leave_form.leave_type = ""
        self.leave_form.signed = ""
        self.leave_form.create_form()
        cur.execute('''INSERT INTO leave_forms VALUES(
        {0},
        '{1}',
        '{2}',
        '{3}',
        '{4}',
        '{5}',
        '{6}',
        '{7}',
        '{8}')'''.format(self.leave_form.ssn,
                         self.leave_form.from_date,
                         self.leave_form.to_date,
                         self.leave_form.from_time,
                         self.leave_form.to_time,
                         self.leave_form.leave_type,
                         self.leave_form.remarks,
                         self.leave_form.signed,
                         self.leave_form.hours))
        conn.commit()

        os.system("start output.pdf")


    def logic(self):
        if self.check_aftp.isChecked():
            self.remarksText.setPlainText("Military Leave for AFTP support")
            self.from_time.setTime(QtCore.QTime(14, 30, 0))
            self.to_time.setTime(QtCore.QTime(16, 30, 0))
            self.radio_mil.setChecked(True)
            self.remarksText.update()

    def update_hours(self):
        from_time = self.from_time.time().toPyTime().strftime("%H%M")
        to_time = self.to_time.time().toPyTime().strftime("%H%M")
        self.total_hours.setTime(QtCore.QTime(hours_of_leave(from_time,to_time),0,0))

    def add_user(self):

        first = self.add_first_line.text()
        last = self.add_last_line.text()
        middle = self.add_middle_line.text()
        ssn = self.add_last4_line.text()

        try:
            print("INSERT INTO users VALUES("+ssn+", '"+last+"', '"+first+"', '"+middle+"')")
            cur.execute("INSERT INTO users VALUES("+ssn+", '"+last+"', '"+first+"', '"+middle+"')")
            conn.commit()
            self.user_list.clear()
            self.fill_drop_down()
        except sqlite3.IntegrityError:
            print('User already enrolled')

    def fill_drop_down(self):
        cur.execute('''SELECT * FROM users''')
        rows = cur.fetchall()
        for row in rows:
            # self.user_list.addItem('{0} - {1}'.format(row[1], str(row[0])))
            self.user_dict[row[0]] = '{0}, {1} {2} - {3}'.format(row[1],row[2],row[3], str(row[0]))
        self.user_dict = OrderedDict(sorted(self.user_dict.items(), key=lambda t: t[1]))
        for key in self.user_dict:
            self.user_list.addItem(self.user_dict[key])


    def user_select(self, text):
        self.leave_form.name, self.leave_form.ssn = text.split(' - ')
        cur.execute("SELECT * FROM leave_forms WHERE ID="+self.leave_form.ssn)
        rows = cur.fetchall()
        self.form_table.setRowCount(len(rows))
        try:
            self.form_table.setColumnCount(len(rows[0]))
        except IndexError:
            self.form_table.setColumnCount(11)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.form_table.setItem(row_num,column,QtGui.QTableWidgetItem(str(cell)))
                column+=1
            row_num+=1

        for row in rows:
            print(row)






# Determines hours_in_day of a day assuming normal work schedule
# 13-Nov-2016 is start of pay period
def hours_in_day(date):
    date = dt.datetime.strptime(date, "%d-%b-%Y")
    miss_monday_start = dt.datetime.strptime("13-Nov-2016", "%d-%b-%Y")
    delta = abs(date - miss_monday_start).days
    days = [(0, 0), (1, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 0),
            (7, 0), (8, 0), (9, 9), (10, 9), (11, 9), (12, 9), (13, 0)]
    for day in days:
        if delta % 14 == day[0]:
            return str(day[1])

def hours_of_leave(from_time, to_time):
    minutes = 60
    hours = 60
    from_time = dt.datetime.strptime(from_time,"%H%M")
    to_time = dt.datetime.strptime(to_time, "%H%M")
    delta = to_time - from_time
    return int((delta.total_seconds() / minutes) / hours)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
