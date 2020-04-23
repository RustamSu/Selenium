import json
import re
from Kroger import cookies as cook
c = cook.cookies
a = c.split(';')
a[0] = a[0].replace('Cookie: ','')
s = '{'
for x in a:
    key = x[:x.index('=')].strip()
    value = x.replace(key+'=', '').strip()
    if key == 'RT' or key == 'x-active-modality':
        s += '"'+key+'":' + value + ','
    else:
        s += '"'+key+'":"' + value + '",'

s = s[:-1] + '}'
# print(s)
js_st = json.loads(s)
print(js_st)
with open('output.json', 'w') as outfile:
    json.dump(js_st, outfile)


