from sys import argv 

script, first, second = argv 
name_who = raw_input("who are you?") 
print "how do you do!", first 
first = raw_input() 
print "let's hang out", second 
second = raw_input() 





"""
import mysql.connector
from mysql.connector import errorcode
try:
    cnx = mysql.connector.connect(user='root', password='bit$)@1302', host='localhost', port='3306')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  cnx.close()
"""

