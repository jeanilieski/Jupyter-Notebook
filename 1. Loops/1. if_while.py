x=5
if x<10: #this is a question
    print 'smaller'
    print 'smaller then 10'# what is indented is executed or 
                           # not depending if it is true or not
if x>20:
    print 'Bigger' #this will not be printed since is False 

print 'Fine'  

print '--------------'

for s in range(5):
    print s
    if s>2:
        print 'Bigger then 2'
    print 'Done with ', s    

print '--------------'

#ONE WAY DECISION

x=42 #finding  value within a defined range
if x>1: # True, so it goes furhter
    print 'bigger then 1'
    if x<100: #still True so it also prints out
        print 'smaller then 100'
print x, 'is smaller then 1 and bigger then 100'        
                        
print '--------------'        


#TWO WAY DECISION

x=4
if x>2:
    print 'bigger'
else:
    print 'smaller'
print 'All done'


print '--------------'

#MULTY-WAY IF
x=4
if x<2:
    print 'small'
elif x<10:
    print 'medium' 
elif x<20:
    print 'smaller then 20'
else:
    print 'large'
print 'All done'
#there could be many elif in one command but only one
#will be executed

print '--------------'

for x in range(15): #it works with loop as well
    print x
    if x<2:
        print 'small'
    elif x<10:
        print 'medium'
    else:
        print 'large'
print 'All done'

#indentation in 11 min

print '--------------'  





#5.1 Loops and Iteration, Week 7

n=5
while n>0:#n is iteration variable, one changing each time
    print n
    n=n-1
print 'Blastoff!'
print n

#the loop prints the number if it is bigger then 0 AND
#substrackts the number for 1. The next time is comming up
#it is not 5 already, but 4. while is just like if, but
#repeated N-times (since it is loop)
#the print n at the end is only to see that the program
#ends with 0, not 5,4,3,2 or 1

print '--------------'

#INFINITE LOOP 
#The "break" statement ends the current loop and jumps to the
#statement immediately following the loop, in this case it
#skips 'print line' and goes to 'print end'

while True:
    line=raw_input('>')
    if line=='done':
        break  
    print line
print 'end, done has been entered'

#this loop ends in two ways: 1.f, e.g 2.'end, done has been entered'
print '--------------'

#The "continue" statement ends the current iterataion and jumps
#to the top of the loop and starts the next iteration. HOWEVER, it saves
#what it found in a document
#this loop may end in three ways: 1. f, e.g. 2.nothing 3. done 
while True:
    line=raw_input('>')
    if line[0]=='#':#if the first caracter of the line is "#" print nothing but continue
        continue
    if line=='done':
        break
    print line
print 'end'
