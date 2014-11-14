# -*- coding: utf-8 -*-
import psycopg2

def tabulate(tex, uid, uname) :
    flag = False
    data_set = [tex, uid, uname]
    next_data_set = ["","",""]
    
    i = 0
    for itera in data_set:
        if len(itera) > 20:
            print "{0:^20}".format(itera[0:20]),
            flag = True
            next_data_set[i] = itera[20:]
        else :
            print "{0:^20}".format(itera),
        i = i + 1
    print ""

    if flag == True:
        tabulate(next_data_set[0], next_data_set[1], next_data_set[2])

def main():
    PostgreSQL_IP = 'iservdb.cloudopenlab.org.tw'
    DBName = "hohohahalala1223_db_5136"
    user = "hohohahalala1223_user_5136"
    password = "Dn5Kbovg"
    port = 5432
    conn_string = "host='%s' port='%s' dbname='%s' user='%s' password='%s'" % (PostgreSQL_IP, port, DBName, user, password)
    connection = psycopg2.connect(conn_string)
    global keyword
    keyword = ' '
    while 1:
        keyword = raw_input('Please Input Keyword :')
        if keyword == 'exit' :
            break 
        cursor = connection.cursor()
        query = "SELECT text, user_id, user_name FROM twitter WHERE q = \'" + keyword + "\' ORDER BY cast(user_id as numeric(20));"
        cursor.execute(query)
        records = cursor.fetchall()

        print "{0:-^20}".format("text"),
        print "{0:-^20}".format("user_name"),
        print "{0:-^20}".format("user_id")
        for itera in records :
            tex = itera[0]
            uid = itera[1]
            uname = itera[2]
            tabulate(tex, uid, uname)
            print "------------------------------------------------------------"

if __name__ == '__main__':
    main()