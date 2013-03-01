import sqlite3 as lite

con = lite.connect('test.db')
Name = raw_input("Name: ")
Def = raw_input("Definition: ")

with con:
    cur = con.cursor()
    
    cur.execute("INSERT INTO Dict VALUES(NULL, ?, ?)", (Name, Def))
    
    print "inserted!"
    
    #cur.execute("CREATE TABLE Dict(Id INTEGER PRIMARY KEY AUTOINCREMENT, Word TEXT, Def TEXT)")
