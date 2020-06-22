#/usr/bin/env python3
import csv
import MySQLdb
import sys

output_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='mySuppliers',
                      user='user', passwd='my_passwd')
c = con.cursor()

file_writer = csv.writer(open(output_file, 'w', newline=''),delimiter=',')
header = ['head1','head2','head3','head4','head5']
file_writer.writerow(header)

c.execute("SELECT * FROM Suppliers WHERE Cost < 700.0;")
row = c.fetchall()
for rows in row:
    file_writer.writerow(rows)


