import json
import requests
import datetime

#print(datetime.date.today() + datetime.timedelta(days=1))

# r = requests.get("https://www.codewars.com/api/v1/users/Nfyz")
# print(r)
# print(r.status_code)
# print(r.json())


# with open('users.json') as json_file:
#     a = json.load(json_file)
# json_file.close()
#
# s = 'Favor'

# with open('users.json', 'a') as json_file:
#     json.dump(a, json_file, indent=4)
#
# if s not in a:
#     print('sss')
# print(a)


k = [('sss',1,1), ('sss',2,3), ('sss',3,4),('aaa',2,3),('aaa',3,4),('aaa',5,6)]

print(list(range(0,10)))
# q = enumerate(k)
# for i,v in q:
    # print(i,v)

d = {}


for n in k:
    name = ''
    if name != n[0]:
        l = [(i,x[1:]) for i,x in enumerate(list(filter(lambda x:x[0] ==n[0] ,k)))]

        name = n[0]
        d[name] = l

print(d)
j = json.dumps(d)
print(j)