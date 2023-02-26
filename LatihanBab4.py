#mengubah file json

import json
data= None
with open('nasabah.json','r') as datafile:
    data = json.load(datafile)

data[0]['nama'] = 'Agus Gus Gus Gus'

data[1]['saldo'] = 300000

with open('nasabah.json', 'w') as datafile:
    json.dump(data,datafile)
