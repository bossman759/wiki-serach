#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import urllib
import BeautifulSoup

con = lite.connect('test.db')
t = raw_input("Search: ")
with con:
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Websites(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Url String)")
    #cur.execute("INSERT INTO Websites VALUES(NULL, 'Mega', 'http://mega.co.nz/')")
    #SQL = "SELECT * FROM Things WHERE Name='Samsung Galaxy S3 T-Mobile'"    
    #SQL = "SELECT * FROM Things WHERE Name='Samsung Galaxy S3 T-Mobile'"
    
    cur.execute("select * from Dict where Def LIKE ? OR word LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
    rows = cur.fetchall()
    
    for row in rows:
        print row[1]
        
        print row[2]
    
    cur.execute("SELECT * FROM Websites WHERE Name LIKE ? OR Url LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
    rows = cur.fetchall()
    
    for row in rows:
        print row[1]
        
        print row[2]
        
    cur.execute("select * from Things where Name like ? LIMIT 12", ('%'+t+'%',))
    rows = cur.fetchall()
    
    for row in rows:
        print row[1]
        
        print row[2]
    
