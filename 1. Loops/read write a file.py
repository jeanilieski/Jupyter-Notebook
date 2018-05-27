#read write a file

import csv
from csv import DictReader

value=('the answer', 42)
print value
s=str(value)
print s
#f.write(s)
for sth in s:
    print sth


f=open('csv1.csv')
r=csv.DictReader(f)#r = csv.DictReader(f) or r=csv.reader(f)
for sth in r:
    print sth


print '********************'
data_rdr = DictReader(open('mn.csv', 'rb'))
header_rdr = DictReader(open('mn_headers.csv', 'rb'))
data_rows = [d for d in data_rdr]#list generator
header_rows = [h for h in header_rdr]
print '********************'
print 'DATA ROWS: ', data_rows[:2]
print '********************'
print 'DATA HEADERS: ', header_rows[:2]
