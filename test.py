import json
import requests
import datetime

#print(datetime.date.today() + datetime.timedelta(days=1))
req = "https://api.123formbuilder.com/v2/forms/5356316?JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJTRVJWRVJFTlYiOiJ3d3ciLCJzdWIiOjI0NzQ3NDYsImlzcyI6Imh0dHBzOi8vYXBpLjEyM2Zvcm1idWlsZGVyLmNvbS92Mi90b2tlbi9yZWZyZXNoIiwiaWF0IjoxNTkyMjQwODA3LCJleHAiOjE1OTIzMjcyMzIsIm5iZiI6MTU5MjI0MDgzMiwianRpIjoiZEc1OEdkNTk0YkxGMWJ4UyJ9.VXHF4c1rqYhAfzMCdKzp4VqA5i6LiF56ocKwN-rPlKc"

r = requests.get(req)
print(r)
print(r.status_code)
print(r.json())


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


