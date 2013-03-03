#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sqlite3 as lite
import Tkinter
con = lite.connect('test.db')


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"")

        button = Tkinter.Button(self,text=u"Search!",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)

    def OnButtonClick(self):
        with con:
            cur = con.cursor()
            t = self.entryVariable.get()
            #self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
            #SQL query for search through Dict table
            cur.execute("select * from Dict where Def LIKE ? OR word LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
            rows = cur.fetchall()
            
            for row in rows:
                #printing second & third column(See tuples)
                print row[1]
                self.labelVariable.set(row[1])
                print row[2]
                self.labelVariable.set(row[2])
            cur.execute("select * from Websites where Name LIKE ? OR Url LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
            rows = cur.fetchall()
            
            for row in rows:
                #printing second & third column(See tuples)
                print row[1]
                self.labelVariable.set(row[1])
                print row[2]
                self.labelVariable.set(row[2])
            cur.execute("select * from Things where Name LIKE ? OR Price LIKE ? LIMIT 12", ('%'+t+'%', '%'+t+'%'))
            rows = cur.fetchall()
            
            for row in rows:
                #printing second & third column(See tuples)
                self.labelVariable.set(row[1])
                self.labelVariable.set(row[2])
        
        
    def OnPressEnter(self,event):
        #self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        print ""
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Wiki Search')
    app.mainloop()
