#try except deals with sth that may blow up and stop the
#further execution of the code
#if the code in 'try' works it escapes the code in the 'except'
#if it falls in 'try' it jumps to 'except'

astr='one hundert twenty three'
try:
    istr=int(astr)
except:
    istr=-1
print 'First', istr



astr='123'
try:
    istr=int(astr)
except:
    istr=-1
print 'Second', istr


astr='one hundert twenty three'
try:
    istr=int(astr)
except:
    istr=-1
print 'Third', istr


print '*************'
astr='Bob'
try:
    print 'Hallo' #will be executed
    istr=int(astr) #this will blow up
    print 'There' #since it's blown up it will not print
except:
    istr=-1
print 'Done', istr


print 'example with raw input from a user:'
rawstr=raw_input('Enter a number: ')

try:
    val=int(rawstr)
except:
    val=-1

if val>0:
    print 'Nice work'
else:
    print 'Not a number'



print 'another example:'
rawstr=raw_input('Enter a number: ')

if rawstr>0:
    print 'Nice work'
else:
    print 'Not a number'











