import sqlite3

def connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor() 
    cur.execute("INSERT INTO Book VALUES(NULL, ?, ? ,?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor() 
    cur.execute("SELECT * FROM Book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("Books.db") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM Book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor() 
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))  
    conn.commit()
    conn.close()

connect()  
#insert("The Invisible man", "Chetan Bhagat", 2012, 1524834)  
#delete(2)
#update(11,"The","John",2002, 2371912)
#print(view())
#print(search(author="Chetan Bhagat"))

