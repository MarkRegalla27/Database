# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:22:51 2015

@author: markregalla
"""

# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('getting_started.db')

with con:
  # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
  cur = con.cursor()    
  #cur.execute('SELECT SQLITE_VERSION()')
  # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
  data = cur.fetchall()
  # Finally, print the result.
  #print "SQLite version: %s" % data


# Inserting rows by passing values directly to `execute()`
#with con:
#    cur = con.cursor()
#    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
#    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
   # cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', '51')")
   # cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January','72')")

with con:    

    cur = con.cursor()    
    cur.execute("SELECT * FROM weather")

    rows = cur.fetchall()

    for row in rows:
        print row