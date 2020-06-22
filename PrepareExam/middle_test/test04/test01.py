import csv
import sys
import MySQLdb
from datetime import date, datetime

input_file = sys.argv[1]
con = MySQLdb.connect(host='localhost', port=3306, db='mySuppliers',
                      user='user', passwd='my_passwd')
c = con.cursor()

file_reader = csv.reader(open(input_file),'r',delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:
            data.appned(str(row[column_index]).lstrip('$')\
                        .replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strftime(str(row[column_index]),'%m/%d/%Y'))
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s)""")
con.commit()
######################################
c.execute("SELECT * FROM Supplier")
row = c.fetchall()
for rows in row:
    index = []
    for column_index in range(len(rows)):
        index.append(str(row[column_index]))
    print(index)

