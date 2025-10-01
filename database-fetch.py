import sqlite3

con =  sqlite3.connect("dimik.db")
cur = con.cursor()

cur.execute("SELECT * FROM book")
row = cur.fetchone()

while row:
    print(row)
    row = cur.fetchone()

def search_by_author(cur, author):
    cur.execute("SELECT * FROM book WHERE author=:auth", {"auth": author})
    return cur.fetchall()
    
search_by_author(cur,"Tamim Shahriar")

cur.close()
con.commit()
con.close()