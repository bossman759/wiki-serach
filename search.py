#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import urllib
import BeautifulSoup

con = lite.connect('test.db')
t = raw_input("Search: ")
if("HELP" in t):
    print "**HELP**"
    
    print "Search: Enter a search term to receive results."

    print "**HELP**"
    
else:
    print "**Type HELP for assistance.**"
    
with con:
    cur = con.cursor()    
    
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
    
