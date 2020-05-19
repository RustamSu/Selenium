import datetime
import json
import mysql.connector as con
import requests

from GrabCodewars import helper as h


def insert_into_user(name, r):
    if r.status_code != 200:
        return 'Error: status code = ' + str(r.status_code) + ' Name is ' + name
    user = r.json()
    # Важно ! используй `, а не ' или " в наименовании полей, таблиц, баз
    sql = "INSERT INTO `{}`.`Users` (`username`, `name`) VALUES ('{}','{}');".format(
        h.MySQLDB, user['username'], user['name'])
    # print(sql)
    cursor.execute(sql)
    mydb.commit()
    return 'insert into user: ' + name


def insert_into_ranks(name, r, day):
    if r.status_code != 200:
        return 'Error: status code = ' + str(r.status_code) + ' Name is ' + name
    user = r.json()
    # user_arr = [user['username'], str(user['honor']), str(user['clan']),
    #             str(user['codeChallenges']['totalCompleted'])]
    usr_over = user['ranks']['overall']
    usr_lang = user['ranks']['languages']
    # print(usr_over)
    # print(usr_lang)

    # print(user['username'], 'overall',usr_over['rank'],usr_over['score'])
    # for x in usr_lang:
    #     print(x, usr_lang[x]['rank'],usr_lang[x]['score'])

    if usr_over:
        sql = "INSERT INTO `{}`.`Ranks` (`username`, `date`,`clan`,`honor`,`totalComplete`,`language`,`rank`, `score`) " \
              "VALUES ('{}','{}','{}',{},{},'{}',{},{});".format(
            h.MySQLDB,
            user['username'],
            day,
            #datetime.date.today(),
            str(user['clan']),
            str(user['honor']),
            str(user['codeChallenges']['totalCompleted']),
            'overall',  # language
            usr_over['rank'],
            usr_over['score'])
        cursor.execute(sql)
        mydb.commit()

    for x in usr_lang:
        sql = "INSERT INTO `{}`.`Ranks` (`username`, `date`,`clan`,`honor`,`totalComplete`,`language`,`rank`, `score`) " \
              "VALUES ('{}','{}','{}',{},{},'{}',{},{});".format(
            h.MySQLDB,
            user['username'],
            day,
            # datetime.date.today(),
            str(user['clan']),
            str(user['honor']),
            str(user['codeChallenges']['totalCompleted']),
            x,  # language
            usr_lang[x]['rank'],
            usr_lang[x]['score'])
        cursor.execute(sql)
        mydb.commit()
    return 'insert into ranks: ' + name


if __name__ == '__main__':
    try:
        with open('users.json') as json_file:
            a = json.load(json_file)
    except:
        print(Exception + ' Open file Error')

    try:
        mydb = con.connect(host="remotemysql.com", user=h.MySQLDB, passwd=h.MySQLpassw)
    except:
        print(Exception + ': DB Connection Error')
    cursor = mydb.cursor()

    sql = 'SELECT username FROM {}.Users;'.format(h.MySQLDB)
    cursor.execute(sql)
    users_in_db = [x[0] for x in cursor.fetchall()] # [('name',)] == fetchall()

    #for tests day = today - 1
    day = datetime.date.today() - datetime.timedelta(days=1)
    sql = 'SELECT DISTINCT username FROM {}.Ranks WHERE date = "{}";'.format(h.MySQLDB, day)
    cursor.execute(sql)
    ranks_in_db = [x[0] for x in cursor.fetchall()]

    for n in a: # a - список с сайта
        req = requests.get("https://www.codewars.com/api/v1/users/{}".format(n.replace(' ','%20')))
        if n not in users_in_db:
            print(insert_into_user(n, req))
        if n not in ranks_in_db:
            print(insert_into_ranks(n, req, day))


