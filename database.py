import MySQLdb

def cursor():
    conn = MySQLdb.connect (host="localhost", user="root", 
                        passwd="blabla", db="kanjibridge")

    return conn.cursor()
