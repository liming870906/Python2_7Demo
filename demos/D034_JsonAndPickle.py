"""
Json
"""

import json
mDic = {'name':'James','age':18,'sex':'man'}

# mData = json.dumps(mDic)
with open('files/json_test','w',encoding='utf8') as file :
    # file.write(mData)
    # file.flush()
    json.dump(mDic,file)


# with open('files/json_test','r',encoding='utf8') as file :
    # data = file.read()
    # mData = json.loads(data)

data = json.load(open('files/json_test','r',encoding='utf8'))
print(data['name'])
# print(mData['name'])

"""
pickle   shelve
"""

import shelve
f = shelve.open('files/shelve_test')

f['info'] = {'name':'Smile','age':18}
f['shop'] = {'name':'banana','price':33}

data = f.get('shop')

print(data)