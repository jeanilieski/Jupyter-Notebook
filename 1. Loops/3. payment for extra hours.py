hrs=raw_input('Enter Hours: ')
rate=raw_input('Enter Rate: ')
h=float(hrs)
r=float(rate)

p=0
if h<=40:
    p=h*r
elif h>40:
    p=(40*r)+((h-40)*(r*1.5))
print 'salary', p    

#40*10.5+(45-40*(10.5*1.5)) 420+5*15.7
