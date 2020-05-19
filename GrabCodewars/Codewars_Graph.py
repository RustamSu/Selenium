import matplotlib.pyplot as plt
import mysql.connector as con


from GrabCodewars import helper as h

mydb = con.connect(host="remotemysql.com", user=h.MySQLDB, passwd=h.MySQLpassw)
cursor = mydb.cursor()

sql = "SELECT distinct username,date_format(date,'%Y.%m.%d') as date, honor FROM {}.Ranks order by username,date;".format(h.MySQLDB)
cursor.execute(sql)
k = cursor.fetchall() # [('name',)] == fetchall()
d = {}
for n in k:
    name = ''
    if name != n[0]:
        l = [x[1:] for x in list(filter(lambda x:x[0] ==n[0] ,k))]
        name = n[0]
        d[name] = l
# print(d)

for n in d:
    x = list(range(0,len(d[n])))
    y = [x[1] for x in d[n]]
    print(x, y)
    plt.plot(x, y, label = n)

plt.xlabel('Date')
plt.ylabel('Honor')
plt.title("CW Plot")
# plt.legend(bbox_to_anchor=(0.07,1,0.7, 1), loc='upper left', )
plt.legend(bbox_to_anchor=(1,1), loc='upper left', )

plt.show()
# style
plt.style.use('seaborn-darkgrid')

