import MySQLdb

connection = MYSQLdb.connect(
            host = '192.168.1.75',
            user = 'root',
            passwd='grassy')

cursor = connection.cursor()

cursor.execute("USE smtest")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table_name in cursor:
    print table_name
