#https://stackoverflow.com/questions/4613465/using-python-to-write-mysql-query-to-csv-need-to-show-field-names



import MySQLdb as sql
import sys
import csv

#servername-localhost, user, password, db name(e.g., db:bank and table:account)
db=sql.connect('localhost','root','7b48i49x','banc')


dbQuery='SELECT * FROM employee_banc;'
cur=db.cursor()
cur.execute(dbQuery)
result=cur.fetchall()

##c = csv.writer(open("temp.csv","wb"))
##c.writerow(result)


rows = cur.fetchall()
fp = open('temp.csv', 'wb')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
