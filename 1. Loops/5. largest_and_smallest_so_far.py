largest_so_far=-1
print 'Before', largest_so_far
for item in [9,41,12,3,74,15]:
    if item>largest_so_far:
        largest_so_far=item
    print largest_so_far, item
print 'After', largest_so_far



smalest_so_far=1000 #if sure that the list has no higher # then 1000
print 'Before', smalest_so_far
for item in [9,41,12,3,74,15]:
    if item<smalest_so_far:
        smalest_so_far=item
    print smalest_so_far, item
print 'After', smalest_so_far


smallest_so_far=None# "None" is not a number
for v in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far=v #after the first execution smallest becomes 9 and is never again 'None'
    elif v<smallest_so_far: #when v=3 and is therefore <9(the smallest so far)...
        smallest_so_far=v #... in the this row we assign 3 to become the new smallest 
    print smallest_so_far, v
print 'After', smallest_so_far



