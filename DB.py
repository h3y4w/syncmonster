import pymysql.cursors

connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd='root')

cursor = connection.cursor()
cursor.execute('USE SMUserInfo')
sql = "INSERT INTO `file` (`file_name`,`parts`,`locations`) VALUES (%s, %s,%s)"
cursor.execute(sql,("star wars episode7.mov", "4", "mediafire"))
connection.commit()
