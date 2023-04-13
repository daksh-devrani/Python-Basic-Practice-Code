import sqlite3
import sqlite3 as sqlite

def createbooktable():
    con=sqlite3.connect('data.db')
    cur=con.cursor()
    cur.execute('create table if not exists books(name text primary key,author text,read integer)')
    con.commit()
    con.close()


def addbooks(name,author):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('insert into books values(?,?,0)',(name,author))
    con.commit()
    con.close()


def getallbooks():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('select * from books')
    data=cur.fetchall()
    a=[]
    for i in data:
        b={}
        b['name']=i[0]
        b['author']=i[1]
        b['read']=i[2]
        a.append(b)
        return a
    con.close()


def markasread(name,author):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('update books set read=1 where name=? and author=?',(name,author))
    con.commit()
    con.close()


def deletebook(name,author):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('delete from books where name=? and author=?', (name, author))
    con.commit()
    con.close()

