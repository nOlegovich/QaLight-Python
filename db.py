import sqlite3
con = sqlite3.connect("db.db")
cur = con.cursor()
cur.execute('''CREATE TABLE mark
                             (id_exam INTEGER PRIMARY KEY,
                              id_stud INTEGER,
                              mark INTEGER,
                              FOREIGN KEY (id_stud) REFERENCES customers(id_stud),
                              FOREIGN KEY (id_exam) REFERENCES products(id_exam))''')

cur.execute(''' CREATE TABLE stud
                              (id_stud INTEGER PRIMARY KEY,
                               surname VARCHAR)''')
cur.execute(''' CREATE TABLE exam
                              (id_exam INTEGER PRIMARY KEY,
                               subject VARCHAR)''')

cur.execute('INSERT INTO mark VALUES(1, 1, "Yakushev")')
cur.execute('INSERT INTO mark VALUES(2, 2, "Moroz")')
cur.execute('INSERT INTO mark VALUES(3, 3, "Saenko")')
cur.execute('INSERT INTO stud VALUES(1, "Yakushev")')
cur.execute('INSERT INTO stud VALUES(2, "Moroz")')
cur.execute('INSERT INTO stud VALUES(3, "Saenko")')
cur.execute('INSERT INTO exam VALUES(1, "sql")')
cur.execute('INSERT INTO exam VALUES(2, "QA")')
cur.execute('INSERT INTO exam VALUES(3, "python")')

con.commit()
cur.close()
con.close()
