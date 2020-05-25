#!/usr/bin/env python3
import csv
import MySQLdb
#import sys

# CSV 입력 파일 경로와 파일명
input_file = 'csv/data_for_updating_mysql.csv'

# MySQL 데이터베이스에 접속한다.
user = input("user: ")
passwd = input("passwd: ")
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', \
                      user=user, passwd=passwd)
c = con.cursor() #실제적으로 연결하는 것.

# CSV 파일을 읽고 특정 행을 갱신한다.
file_reader = csv.reader(open(input_file, 'r', newline=''),delimiter=',')
#헤더를 읽음
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""UPDATE Suppliers SET Cost = %s, Purchase_Date = %s WHERE Supplier_Name = %s;""",data)
con.commit()

print("\n데이터베이스 확인\n");

# Suppliers 테이블에 질의한다.
c.execute("SELECT * FROM Suppliers")
rows= c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)