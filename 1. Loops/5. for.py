#definite loops

for s in [5,4,3,2,1]:
    print s
print 'end'


ppl=['goc', 'nes', 'jur']
for s in ppl:
    print 'happy new year', s
print 'done!'


#finding the LARGEST item in a list
largest_so_far=-1
print 'Before', largest_so_far
for item in [9,41,12,3,74,15]:
    if item>largest_so_far:
        largest_so_far=item
    print largest_so_far, item
print 'After', largest_so_far



#'to COUNT how many times we execute a loop we introduce
#a countrer variable that starts with 0 and we add one to
#each time we go through the loop (this also counts how many
#items there are in a list

z=0
print 'Before', z
for sth in [9,41,12,3,74,15]:
    z=z+1
    print z,sth
print 'After', z# just to see that z now ends up as 6
# (the number of items in the list), not as 0


#SUMing in a loop (running total)
z=0
print 'Before', z
for sth in [9,41,12,3,74,15]:
    z=z+sth
    print z,sth
print 'After', z


#finding the AVERAGE of a list of numbers
count=0
total=0
for value in [9,41,12,3,74,15]:
    count=count+1
    total=total+value
    print count, total, value
print 'Average: ', count, total, total/count



#FINDING PARTICULAR ITEMS in a list
for value in [9,41,12,3,74,15]:
    if value>20:
        print 'larger then 20: ', value
print 'done!'        


#SEARCH for a single item in a list using BOOLEAN
found=False
for v in [9,41,12,3,74,15]:
    if v==3:
        found=True
        break
print 'I found number 3 there!'


#same with strings in a list
found=False
for v in ['love', 'hate']:
    if v=='love':
        found=True
        break
print 'I found love!'






#SEARCH for the SMALLEST ITEM
smallest_so_far=None# "None" is not a number
for v in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far=v #after the first execution smallest becomes 9 and is never again 'None'
    elif v<smallest_so_far: #when v=3 and is therefore <9(the smallest so far)...
        smallest_so_far=v #... in the this row we assign 3 to become the new smallest 
    print smallest_so_far, v
print smallest_so_far
#(if and elif) not (if and else)        
#use 'is' with 'True or False', other times '=='





