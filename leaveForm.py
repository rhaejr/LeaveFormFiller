import datetime as dt
from fdfgen import forge_fdf
import subprocess
from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4 import Qt
from PyQt4.uic import loadUi
from gui4 import  Ui_MainWindow
import sqlite3
from collections import OrderedDict

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
middle    TEXT NOT NULL,
grade TEXT NOT NULL,
unit TEXT NOT NULL
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






class AftpSlip:
    def create_form(self, datas):
        fdf = forge_fdf("", datas, [], [], [])
        fdf_file = open("data1.fdf", "wb")
        fdf_file.write(fdf)
        fdf_file.close()
        subprocess.call(["pdftk", "AFTP.pdf", "fill_form", "data1.fdf", "output", "outputAFTP.pdf", "flatten"])


class LeaveForm:
    def __init__(self, gui):
        self.name = ""
        self.ssn = ""
        self.gui = gui
        self.datas = []
        self.from_date = ""
        self.to_date = ""
        self.from_time = ""
        self.to_time = ""
        self.leave_type = ""
        self.remarks = ""
        self.signed = ""
        self.hours = ""

    def fill_fields(self):

        self.datas.append((REMARKS, self.remarks))
        self.datas.append((NAME, self.name))
        self.datas.append((SSN, self.ssn))

        if self.gui.ui.radio_annual.isChecked():
            self.datas.append((ANNUAL_FROM_DATE, self.from_date))
            self.datas.append((ANNUAL_TO_DATE, self.to_date))
            self.datas.append((ANNUAL_BOX, 1))
            self.datas.append((ANNUAL_FROM_TIME, self.from_time))
            self.datas.append((ANNUAL_TO_TIME, self.to_time))
            self.datas.append((ANNUAL_TOTAL, self.hours))

        elif self.gui.ui.radio_sick.isChecked():
            self.datas.append((SICK_FROM_DATE, self.from_date))
            self.datas.append((SICK_TO_DATE, self.to_date))
            self.datas.append((SICK_BOX, 1))
            self.datas.append((SICK_FROM_TIME, self.from_time))
            self.datas.append((SICK_TO_TIME, self.to_time))
            self.datas.append((SICK_TOTAL, self.hours))


        elif self.gui.ui.radio_lwop.isChecked():
            self.datas.append((LWOP_FROM_DATE, self.from_date))
            self.datas.append((LWOP_TO_DATE, self.to_date))
            self.datas.append((LWOP_BOX, 1))
            self.datas.append((LWOP_FROM_TIME, self.from_time))
            self.datas.append((LWOP_TO_TIME, self.to_time))
            self.datas.append((LWOP_TOTAL, self.hours))

        elif self.gui.ui.radio_comp.isChecked():
            self.datas.append((COMP_FROM_DATE, self.from_date))
            self.datas.append((COMP_TO_DATE, self.to_date))
            self.datas.append((COMP_BOX, 1))
            self.datas.append((COMP_FROM_TIME, self.from_time))
            self.datas.append((COMP_TO_TIME, self.to_time))
            self.datas.append((COMP_TOTAL, self.hours))

        elif self.gui.ui.radio_mil.isChecked():
            self.datas.append((OTHER_FROM_DATE, self.from_date))
            self.datas.append((OTHER_TO_DATE, self.to_date))
            self.datas.append((OTHER_BOX, 1))
            self.datas.append((OTHER_FROM_TIME, self.from_time))
            self.datas.append((OTHER_TO_TIME, self.to_time))
            self.datas.append((OTHER_TOTAL, self.hours))

    def create_form(self):
        self.fill_fields()
        fdf = forge_fdf("", self.datas, [], [], [])
        fdf_file = open("data.fdf", "wb")
        fdf_file.write(fdf)
        fdf_file.close()
        subprocess.call(["pdftk", "leaveForm.pdf", "fill_form", "data.fdf", "output", "output.pdf", "flatten"])

class Main(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connections()
        self.defaults()
        self.logic()
        self.fill_drop_down()
        self.leave_form = LeaveForm(self)
        self.aftp_slip = AftpSlip()
        # self.user_table()

    # noinspection PyUnresolvedReferences
    def connections(self):

        self.ui.submit_btn.clicked.connect(self.submit_leave)
        self.ui.check_aftp.clicked.connect(self.logic)
        self.ui.radio_mil.clicked.connect(self.logic)
        self.ui.radio_sick.clicked.connect(self.logic)
        self.ui.radio_lwop.clicked.connect(self.logic)
        self.ui.radio_annual.clicked.connect(self.logic)
        self.ui.from_time.timeChanged.connect(self.update_hours)
        self.ui.to_time.timeChanged.connect(self.update_hours)
        self.ui.add_submit_btn.clicked.connect(self.add_user)
        self.ui.user_list.activated[str].connect(self.user_select)

    def defaults(self):
        self.ui.from_date.setDate(QtCore.QDate.currentDate())
        self.ui.to_date.setDate(QtCore.QDate.currentDate())
        self.ui.from_time.setTime(QtCore.QTime(7, 0, 0))
        self.ui.to_time.setTime(QtCore.QTime(16, 30, 0))
        self.user_dict = {}
        self.user_dict = OrderedDict(sorted(self.user_dict.items(), key=lambda t: t[0]))
        self.ui.single_dual.addItem("Periods...")
        self.ui.single_dual.addItems(["Single", "Dual"])
        self.ui.aftp_code.addItem("AFTP Code...")
        self.ui.aftp_code.addItems(["A","B","G","I","J","L","M","Q","R","S","T","V"])
        self.ui.tng_code.addItem("TNG Code...")
        self.ui.tng_code.addItems(["AST","FDM","GSC","INF","MNT","MT1","SNF","OLT","SPT","WX","TD1","TD2","TD3"])
        self.ui.grade_drop.addItems(["E-1","E-2","E-3","E-4","E-5","E-6","E-7","E-8","E-9",
                                  "WO1","CW2","CW3","CW4","CW5",
                                  "O-1","O-2","O-3","O-4","O-5","O-6","O-7","O-8","O-9"])


    def submit_leave(self):

        self.leave_form.from_date = self.from_date.date().toPyDate().strftime("%d-%b-%Y")
        self.leave_form.to_date = self.to_date.date().toPyDate().strftime("%d-%b-%Y")
        self.leave_form.from_time = self.from_time.time().toPyTime().strftime("%H%M")
        self.leave_form.to_time = self.to_time.time().toPyTime().strftime("%H%M")
        self.leave_form.remarks = self.remarksText.toPlainText()
        self.leave_form.hours = self.total_hours.time().toPyTime().strftime("%H").lstrip('0')
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

        if self.ui.check_aftp.isChecked():
            a1 = self.aftp_code.currentText()
            t1 = self.tng_code.currentText()
            p1 = "X"
            a2 = self.aftp_code.currentText()
            t2 = self.tng_code.currentText()
            p2 = "X"
            p3 = ""
            periods = self.single_dual.currentText()

            if self.ui.aftp_code.currentText() == "AFTP Code...":
                a1, a2 = ("L", "L")
            if self.ui.tng_code.currentText() == "TNG Code...":
                t1, t2 = ("SPT", "SPT")
            if self.ui.single_dual.currentText() == "Periods...":
                periods = "Dual"
            if periods == "Single":
                a2, t2, p2, p3 = ("", "", "", "X")

            cur.execute("SELECT grade, unit FROM users WHERE ssn=" + self.leave_form.ssn)
            grade, unit = cur.fetchall()[0]

            # if day_of_week(self.leave_form.from_date) == "Thur":
            #     if periods == "Single":
            #         from_time = "1630"
            #     else:
            #         from_time = "1230"
            #     to_time = "2100"

            if day_of_week(self.leave_form.from_date) == "Sun":
                from_time = "0730"
                if periods == "Single":
                    to_time = "1130"
                else:
                    to_time = "1600"
            else:
                from_time = "1530"
                to_time = "2330"



            self.aftp_data = [
                ("DATE", self.from_date.date().toPyDate().strftime("%d-%b-%Y")),
                ("SINGLE_DUAL", periods),
                ("FROM", from_time),
                ("TO", to_time),
                ("ORGANIZATION", unit),
                ("SSN", self.leave_form.ssn),
                ("GRADE", grade),
                ("NAME", self.leave_form.name),
                ("AFTP_CODE_1", a1),
                ("AFTP_CODE_2", a2),
                ("TNG_CODE_1", t1),
                ("TNG_CODE_2", t2),
                ("FLYING_TIME", ""),
                ("FLYING_TIME_2", ""),
                ("TAIL_1", ""),
                ("TAIL_2", ""),
                ("PAY", p1),
                ("PAY_2", p2),
                ("NON_PAY_1", ""),
                ("NON_PAY_2]", "")]

            self.aftp_slip.create_form(self.aftp_data)
            os.system("pdftk output.pdf outputAFTP.pdf cat output outputboth.pdf")
            os.system("start outputboth.pdf")
        else:
            os.system("start output.pdf")
    def logic(self):
        if self.ui.check_aftp.isChecked():
            self.ui.remarksText.setPlainText("Military Leave for AFTP support")
            self.ui.from_time.setTime(QtCore.QTime(15, 30, 0))
            self.ui.to_time.setTime(QtCore.QTime(16, 30, 0))
            # self.radio_mil.setChecked(True)
            self.ui.remarksText.update()


    def update_hours(self):
        from_time = self.ui.from_time.time().toPyTime().strftime("%H%M")
        to_time = self.ui.to_time.time().toPyTime().strftime("%H%M")
        self.ui.total_hours.setTime(QtCore.QTime(hours_of_leave(from_time, to_time), 0, 0))

    def add_user(self):

        first = self.ui.add_first_line.text()
        last = self.ui.add_last_line.text()
        middle = self.ui.add_middle_line.text()
        ssn = self.ui.add_last4_line.text()
        grade = self.ui.grade_drop.currentText()
        unit = self.ui.unit_edit.text()

        try:
            cur.execute("INSERT INTO users VALUES(" + ssn + ", '" + last + "', '" + first + "', '" + middle + "', '"
                        + grade + "', '" + unit + "')")
            conn.commit()
            self.ui.user_list.clear()
            self.fill_drop_down()
        except sqlite3.IntegrityError:
            self.update_user(ssn, last, first, middle, grade, unit)

    def update_user(self, ssn, last, first, middle, grade, unit):
        msg = QtGui.QMessageBox()
        msg = QtGui.QMessageBox.question(msg, "User already enrolled!",
                                         "Do you want to update the user?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:
            print("yes")
            cur.execute("UPDATE users SET last=?, first=?, middle=?, grade=?, unit=? WHERE ssn=?", (last, first, middle, grade, unit, ssn))
            conn.commit()
            self.ui.user_list.clear()
            self.fill_drop_down()

        else:
            pass

    def fill_drop_down(self):
        cur.execute('''SELECT * FROM users''')
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            if len(str(row[0])) == 3:
                row[0] = '0' + str(row[0])
            # self.user_list.addItem('{0} - {1}'.format(row[1], str(row[0])))
            self.user_dict[row[0]] = '{0}, {1} {2} - {3}'.format(row[1], row[2], row[3], str(row[0]))
        self.user_dict = OrderedDict(sorted(self.user_dict.items(), key=lambda t: t[1]))
        self.ui.user_list.addItem("Select user...")
        for key in self.user_dict:
            self.ui.user_list.addItem(self.user_dict[key])

    def user_select(self, text):
        if text == "Select user...":
            return
        self.leave_form.name, self.leave_form.ssn = text.split(' - ')
        cur.execute(
            "SELECT from_date, to_date,from_time,to_time,leave_type,remarks,signed,hours  FROM leave_forms WHERE ID=" + self.leave_form.ssn)
        rows = cur.fetchall()
        self.ui.form_table.setRowCount(len(rows))
        try:
            self.ui.form_table.setColumnCount(len(rows[0]))
        except IndexError:
            self.ui.form_table.setColumnCount(11)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.ui.form_table.setItem(row_num, column, QtGui.QTableWidgetItem(str(cell)))
                column += 1
            row_num += 1
        self.ui.form_table.setHorizontalHeaderLabels(
            ['from date', 'to date', 'from time', 'to time', 'leave type', 'remarks', 'signed', 'hours'])

        # for row in rows:

        #     print(row)

def day_of_week(date):
    date = dt.datetime.strptime(date, "%d-%b-%Y")
    miss_monday_start = dt.datetime.strptime("13-Nov-2016", "%d-%b-%Y")
    delta = abs(date - miss_monday_start).days
    days = [(0, "Sun"), (1, "Mon"), (2, "Tues"), (3, "Wed"), (4, "Thur"), (5, "Fri"), (6, "Sat"),
            (7, "Sun"), (8, "Mon"), (9, "Tues"), (10, "Wed"), (11, "Thur"), (12, "Fri"), (13, "Sat")]
    for day in days:
        if delta % 14 == day[0]:
            return str(day[1])

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
    from_time = dt.datetime.strptime(from_time, "%H%M")
    to_time = dt.datetime.strptime(to_time, "%H%M")
    delta = to_time - from_time
    return int((delta.total_seconds() / minutes) / hours)


def main():
    app = Qt.QApplication(sys.argv)
    main_view = Main()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
