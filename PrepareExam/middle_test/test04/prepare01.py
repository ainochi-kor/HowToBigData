#!/usr/bin/env python3
import csv
import MySQLdb
import sys
from datetime import datetime,date
# CSV 입력 파일 경로
input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers',
                      user='users', passwd='passwd')
c = con.cursor()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$')\
                        .replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strftime(str(row[column_index]), '%m/%d/%Y'))
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppiers VALUES (%s, %s, %s, %s, %s);""",data)
con.commit()
print("")
############################################
c.execute("""SELECT * FROM Supliers""")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)


