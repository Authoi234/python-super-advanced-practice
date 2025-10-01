import sqlite3

con = sqlite3.connect("dimik.db")
cur = con.cursor()

# create table
cur.execute("CREATE TABLE IF NOT EXISTS book (name text, author text, price real)")

# insert a single row
cur.execute("INSERT INTO book VALUES ('Computer Programming Part 1', 'Tamim Shahriar', 260)")

book_list = [
    ("Computer Programming Part 2", "Tamim Shahriar", 250),
    ("Computer Programming Part 3", "Tamim Shahriar", 270),
    ("Programming Exercise", "Tahmid Rafi", 140)
]

# Insert multiple rows
cur.executemany("INSERT INTO book VALUES (?, ?, ?)", book_list)

con.commit()
cur.close()
con.close()
