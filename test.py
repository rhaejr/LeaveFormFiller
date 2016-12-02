from fdfgen import forge_fdf
import subprocess
import datetime as dt
import sqlite3
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
fields = [(ANNUAL_FROM_DATE, 'Test'),
          (ANNUAL_FROM_TIME, 'Test'),
          (ANNUAL_TO_DATE, 'Test'),
          (ANNUAL_TO_TIME, 'Test'),
          (ANNUAL_TOTAL, 'Test'),
          (SICK_FROM_DATE, 'Test'),
          (SICK_FROM_TIME, 'Test'),
          (SICK_TO_DATE, 'Test'),
          (SICK_TO_TIME, 'Test'),
          (SICK_TOTAL, 'Test'),
          (COMP_FROM_DATE, 'Test'),
          (COMP_FROM_TIME, 'Test'),
          (COMP_TO_DATE, 'Test'),
          (COMP_TO_TIME, 'Test'),
          (COMP_TOTAL, 'Test'),
          (OTHER_FROM_DATE, 'Test'),
          (OTHER_FROM_TIME, 'Test'),
          (OTHER_TO_DATE, 'Test'),
          (OTHER_TO_TIME, 'Test'),
          (OTHER_TOTAL, 'Test'),
          (LWOP_FROM_DATE, 'Test'),
          (LWOP_FROM_TIME, 'Test'),
          (LWOP_TO_DATE, 'Test'),
          (LWOP_TO_TIME, 'Test'),
          (LWOP_TOTAL, 'Test'),
          (ORGANIZATION, 'Test'),
          (SSN, 'Test'),
          (NAME, 'Test'),
          (ANNUAL_BOX, '1'),
          (SIGN_DATE, 'Test')]

# fdf = forge_fdf("", fields, [], [], [])
# fdf_file = open("data.fdf", "wb")
# fdf_file.write(fdf)
# fdf_file.close()
# # cdir = "C:\\Users\\michael\\Documents\\GitHub\\learning-java\\Python34_projects\\leave_form_filler\\"
# # os.chdir("C:\\Users\\michael\\Documents\\GitHub\\learning-java\\Python34_projects\\leave_form_filler")
# subprocess.call(["pdftk",  "leaveForm.pdf", "fill_form", "data.fdf", "output",  "output.pdf", "flatten"])
PAYDAY = "10-Nov-2016"
MISS_MONDAY = "07-Nov-2016"
PAY_START = "13-Nov-2016"

start = dt.datetime.today()
test = "29-Jan-2016"
# missi_monday_start = dt.datetime.strptime("07-Nov-2016", "%d-%b-%Y")
# delta1 = test - missi_monday_start
# print(delta.days)
# print(delta.days % 14 == 0)


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
# print(hours_in_day(test))
# print(hours_of_leave("0700", "1630"))

conn = sqlite3.connect("users.db")
cur = conn.cursor()

# conn.execute('''CREATE TABLE IF NOT EXISTS users
# (ID INT PRIMARY KEY      NOT NULL,
# NAME    TEXT NOT NULL);''')

cur.execute('''SELECT * FROM users''')
rows = cur.fetchall()
print(rows[0][1])

# for row in rows:
#     print(row)

conn.close()
# print("sucess")

# conn = sqlite3.connect("test.db")
#
# conn.execute('''CREATE TABLE IF NOT EXISTS leave_forms
# (ID INT PRIMARY KEY      NOT NULL,
# NAME    TEXT NOT NULL);''')
# conn.close()





