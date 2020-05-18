#!/usr/bin/env python3
import sqlite3

# 메모리에 SQLite3 데이터베이스를 만든다
# 네 가지 속성을 지닌 sales 테이블을 만든다.
#con = sqlite3.connect(':memory:') #Ram안에 생기는 임시 데이터.
con = sqlite3.connect('my_db.db') #진짜 DB를 만드는 것.

#데이터 생성.
query = """CREATE TABLE sales(
            customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date Date);"""
con.execute(query)
con.commit() #Save하는 역할.

# sales 테이블에 데이터를 삽입한다.
# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Corw', 'Printer', 155.75,'2014-02-03'),
        ('Stephen Randolph','Computer', 679.40,'2014-02-20')]
# 물음표 자리에 data의 해당 값이 입력된다.
statement = "INSERT INTO sales VALUES (?,?,?,?)"
#실행방법.
con.executemany(statement, data)
con.commit()

# sales 테이블에 질의한다.
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall() #row에 데이터를 저장.

# 출력된 데이터의 수를 센다
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: {}'.format(row_counter))