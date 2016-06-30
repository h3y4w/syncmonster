from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL
from passlib.hash import pbkdf2_sha256 as sha256
import accountapi
# SET UP OAUTH EXAMPLE BELOW ######################################
#oauth = OAuth2Provider(app)
#api = restful.Api(app, decorators=[oauth.require_oauth('email')])
###############################################################333

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'SM'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql.init_app(app)

api = Api(app)

class AuthenticateUser(Resource):
    def post(self):
        try:
            # Parse the arguments

            parser = reqparse.RequestParser()

            parser.add_argument('email', type=str, help='Email address for Authentication')
            parser.add_argument('password', type=str, help='Password for Authentication')
            
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spAuthenticateUser',(_userEmail,))
            raw_hash = cursor.fetchall()
            _hash = str(raw_hash[0][0])

            return (sha256.verify(_userPassword,_hash))

        except Exception as e:
            return {'error': str(e)}


class GetAllFiles(Resource):
    def get(self):
        try: 
            # Parse the arguments

            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int)
            args = parser.parse_args()

            _userId = args['user_id']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spGetAllFiles',(_userId,))
            data = cursor.fetchall()

            files=[];
            for File in data:
                i = [
                    File[0],
                    File[1],
                    File[2],
                ]
                files.append(i)

            return files

        except Exception as e:
            return {'error': str(e)}

class DeleteFile(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file_id', type=int)
        args = parser.parse_args()

        _fileId = args['file_id']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spDeleteFile',(_fileId,))
        data = cursor.fetchall()
        conn.commit()

class UploadFile(Resource):
    def put(self):
        try: 
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('user_id', type=int)
            parser.add_argument('size', type=int)
            parser.add_argument('compression', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _name = args['name']
            _compression = args['compression']
            _userId = args['user_id']
            _size = args['size']
            _password = args['password']


            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spUploadFile',(_userId,_name,_size,_compression,_password))
            data = cursor.fetchall()

            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
            return {'error': str(e)}
            
                

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = sha256.encrypt(args['password'], rounds=12345)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spCreateUser',(_userEmail,_userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200','Message': 'User creation success'}
            else:
                return {'StatusCode':'1000','Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}


class GetAllAccounts(Resource):
    def get(self):
        try: 

            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int)
            parser.add_argument('account_id', type=int)

            args = parser.parse_args()

            _userId = args['user_id']
            _accountId = args['account_id']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spGetAllAccounts',(_userId,_accountId))
            data = cursor.fetchall()

            accounts=[];
            print 'data: ',
            print data
            for account in data:
                i = [
                    account[0],
                    account[1]
                ]
                accounts.append(i)

            return accounts

        except Exception as e:
            return {'error': str(e)}



class AddAccount(Resource):
    account_types = {'googledrive': accountapi.ConnectGoogleDrive.auth, 'dropbox':accountapi.ConnectDropbox.auth}
    def post(self):
        try:
            parser = reqparse.RequestParser()
            
            parser.add_argument('user_id', type=int, help='User id')
            parser.add_argument('type', type=str, help='What cloud account')
            parser.add_argument('name', type=str, help='Given name for account')
            parser.add_argument('token', type=str, help='token')

            args = parser.parse_args()

            _userId = args['user_id']
            _userType = args['type']
            _userName = args['name']
            _userToken = args['token']

            gen_token = self.account_types[_userType](_userToken)
            if gen_token:
                _userToken = gen_token

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spAddAccount',(_userName, _userType, _userToken,_userId))
            conn.commit()
            return {'Success':True}

        except Exception as e:
            return {'error': str(e)}




class DeleteAccount(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int)
        args = parser.parse_args()

        _accountId = args['account_id']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spDeleteAccount',(_accountId,))
        data = cursor.fetchall()
        conn.commit()

api.add_resource(accountapi.ConnectGoogleDrive, '/ConnectGoogleDrive')
api.add_resource(accountapi.ConnectDropbox, '/ConnectDropbox')
api.add_resource(CreateUser, '/CreateUser')
api.add_resource(AuthenticateUser, '/AuthenticateUser')
api.add_resource(UploadFile, '/UploadFile')
api.add_resource(GetAllFiles, '/GetAllFiles')
api.add_resource(GetAllAccounts, '/GetAllAccounts')
api.add_resource(AddAccount, '/AddAccount')
api.add_resource(DeleteFile, '/DeleteFile')
api.add_resource(DeleteAccount, '/DeleteAccount')
if __name__ == '__main__':
    app.run(debug=True)
