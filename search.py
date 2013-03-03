#!/usr/bin/python
# -*- coding: utf-8 -*-
#import need packages
import sqlite3 as lite
import sys
import urllib
import BeautifulSoup

#create a connection with the test.db file
con = lite.connect('test.db')
#gets the search term
t = raw_input("Search: ")
#checks to see if the user typed HELP for assistance
if("HELP" in t):
    print "**HELP**"
    
    print "Search: Enter a search term to receive results."
    
    print "History: Enter HISTORY to see recent searches."

    print "**HELP**"
    
else:
    print "**Type HELP for assistance.**"


with con:
    #create our cursor
    cur = con.cursor()
    
    if("HISTORY" in t):
        cur.execute("select * from HISTORY")
        rows = cur.fetchall()
        
        for row in rows:
            
            print row[1]
    else: 
            
        cur.execute("INSERT INTO History VALUES(NULL, ?)", (t,))        
               
        #SQL query for search through Dict table
        cur.execute("select * from Dict where Def LIKE ? OR word LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
        rows = cur.fetchall()
        
        for row in rows:
            #printing second & third column(See tuples)
            print row[1]
            
            print row[2]
            
            #SQL query for search through Websites table
        cur.execute("SELECT * FROM Websites WHERE Name LIKE ? OR Url LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
        rows = cur.fetchall()
        
        for row in rows:
            #printing second & third column(See tuples)
            print row[1]
            
            print row[2]
            #SQL query for search through Things table    
        cur.execute("select * from Things where Name like ? LIMIT 12", ('%'+t+'%',))
        rows = cur.fetchall()
        
        for row in rows:
            #printing second & third column(See tuples)
            print row[1]
            
            print row[2]
            
        
