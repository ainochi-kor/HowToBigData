#!/usr/bin/env python3
import csv
import MySQLdb
import sys
import getpass
from datetime import datetime,date

# CSV 입력 파일 경로와 파일명
input_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다
user_id = input("ID :: ")
user_pw = getpass.getpass("PW :: ")
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user=user_id, passwd=user_pw)
c = con.cursor()

#파일 읽기
# Suppliers 테이블에 데이터를 입력한다.
file_reader = csv.reader(open(input_file,'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_idex in range(len(header)):
        if column_idex < 4:
            data.append(str(row[column_idex]).lstrip('$')\
                        .replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strptime(\
                str(row[column_idex]), '%m/%d/%Y'))
            # %Y를 쓰면 연도를 2016으로 저장하고 %y를 쓰면 15로 저장한다
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppliers VALUES(%s, %s, %s ,%s , %s);""",data)
con.commit()
print("#Insert 작업.")

# Suppliers 테이블에 질의한다.
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_idex in range(len(row)):
        row_list_output.append(str(row[column_idex]))
    print(row_list_output)