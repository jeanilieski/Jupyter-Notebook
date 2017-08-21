import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://python-data.dr-chuck.net/geojson?'

   
    

while True:# infinite loop interupted by 'break' if not 'True'/ or 'continue',
    #returning the iteration on the begining of the loop
    
    address = raw_input('Enter location: ')
    if len(address) < 1 : break    

    url = serviceurl + urllib.urlencode({'sensor':'false',
                                         'address': address})#string concatination
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read() #reads json/ at this point is one big string
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))#if some of the following, return up at 'url' and loop again
    except: js = None #loads is the turning of json into py dictionary
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)#dump in a string/and indentation
                                    # js is a dictionary

    lat = js["results"][0]["geometry"]["location"]["lat"]#the next two lines parsing
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
