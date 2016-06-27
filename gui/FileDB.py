import pymysql.cursors

class FileDB (object):
    connection = None

    def __init__ (self):
        self.connection = pymysql.connect(
                    host = 'localhost',
                    user = 'root',
                    passwd = 'root',
                    autocommit=True)
        self.cursor = self.connection.cursor()
        self.cursor.execute('USE SMUserInfo')

    def update(self): # look at DB.py in main folder to fix this
        self.cursor.execute("select file_id, file_name, parts from file")
        return (self.cursor.fetchall())

    def add(self):
#       sql = "INSERT INTO `file` (`file_name`, `parts`,`locations`)
        pass
    def delete(self, file_id):
        self.cursor.execute("delete from file where file_id = " + file_id)
