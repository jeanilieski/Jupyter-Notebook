import urllib
import json
import requests

chunk_size = 20#arbitrarily chosen, suitable for readability and clarity
total = 2099# seen in json format in the 'results'


url_template = 'https://fertighaus.de/-/houses?format=json&limit=20&page='
#pegination, important! the format=json

big_list=[]
for i in range(int(total/chunk_size) + 1):#integer (number with no decimals)
    url = url_template + str(i)# string method
    print url
    resp = requests.get(url)
    data=json.loads(resp.text)
    big_list.extend(data['results'])#append [1, 2, 3, [4, 5]]/extend [1, 2, 3, 4, 5]
print len(big_list)#2100; there is one more object for some reason
                    
with open('all_flats.json', 'w') as file1:#opens a document and writes into json format
    json.dump(big_list, file1)#LOAD data for i-page and add to a big list
                    # dump(), simply serializes the object to a file.
#104 pages
#2100

#It is good practice to use the with keyword when dealing with file
#objects. This has the advantage that the file is properly closed
#after its suite finishes, even if an exception is raised on the way.
#It is also much shorter than writing equivalent try-finally blocks

