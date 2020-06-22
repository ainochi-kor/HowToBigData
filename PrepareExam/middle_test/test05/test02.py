#!/usr/bin/env python3
import csv
import MySQLdb
import sys

input_file = sys.argv[1]

con = MySQLdb.connect()
c = con.cursor()

file_reader = csv.reader(open(input_file,'r',newline=''),delimiter=',')
header = next(file_reader,None)

for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""
                UPDATE Suppliers
                SET Cost=%s, Purchase_Date=%s 
                WHERE Supplier_Name = %s
            """,data)
con.commit()

c.execute("SECLET * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output_list = []
    for index in range(len(row)):
        output_list.append(str(row[index]))
    print(output_list)
