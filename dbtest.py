#!/usr/bin/python

import sys

import MySQLdb

print "Done"

# Open database connection
db = MySQLdb.connect("localhost","root","root","test" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT * from emp")
# Fetch a single row using fetchone() method.
rows = cursor.fetchall()

for row in rows:
    print "ID : "+str(row[0])+"\tName : "+str(row[1])

#print "id : "+data[0].__str__()
#print "name : "+data[1].__str__()
#print "Database version : %s " % data
# disconnect from server
#db.close()