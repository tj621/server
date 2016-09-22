import MySQLdb

conn = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='root',
                       db='test')
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print "server version:", row[0]
cursor.close()
conn.close()