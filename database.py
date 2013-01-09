import MySQLdb

def cursor():
    conn = MySQLdb.connect (host="localhost", user="root", 
                        passwd="blabla", db="kanjibridge")

    curs = conn.cursor()

    curs.execute("SET NAMES 'utf8'")

    return curs
