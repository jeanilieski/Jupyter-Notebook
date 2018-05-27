score = raw_input("Enter Score: ")

num=float(score) #float not int (since 0.8)
print num


if num<0 or num>1:
        print 'error'
elif num>=0.9:
        print 'A'
elif num>=0.8:
        print 'B'
        


