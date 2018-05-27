import json
from pandas import DataFrame
from numpy import corrcoef, sum, log, arange
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks


with open('all_flats.json', 'r') as file2:
    data = json.load(file2)

def to_df_row(item):
    row = {
        'price_ready': item['price_ready'],
        'price_fitting': item['price_fitting'],
        'price_lego': item['price_lego']
    }

    for feature in item['features_verbose']:
        row[feature['name']] = 1 #we can use id or name. 1 is value or 'yes',
                                #the other value is 'NaN' of the dummy

    return row

df = DataFrame([to_df_row(x) for x in data])
df1=df.fillna(0)#change the NaN with 0, because the corr() would not work
                #without two valid values

print df1.head(20)
df2=df1.corr()
print df2


#df2.to_csv('out.csv')
#df.to_csv(file_name, sep='\t')

# plotting the correlation matrix
#R = corrcoef(df1)
#pcolor(R)
#colorbar()
#yticks(arange(0.5,10.5),range(0,10))
#xticks(arange(0.5,10.5),range(0,10))
#show()





