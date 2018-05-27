#40,10.5 OR 45,10.5

hours=raw_input('Enter hours: ') 
rate=raw_input('Enter hourly rate: ')

try:
    h=int(hours)
except:
    h=-1
print 'hours', h


try:
    r=float(rate)
except:
    r=-1
print 'rate', r


    
def computepay(h,r):
    p=0
    if h<=40:
        p=h*r
    elif h>40:
        p=(40*r)+((h-40)*(r*1.5))
    return p    


salary=computepay(h,r)
print salary

