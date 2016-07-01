import os
import requests
#import accountmanager
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from mediafire import MediaFireApi, MediaFireUploader
from dropbox import Dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import APIReciever
class Uploader (object):
    connectedAccounts = None
    upload_to = {}
    files_to_uplad = None
    def __init__ (self, files_to_upload):
        self.upload_to.update({'googledrive':self.googleDrive, 'dropbox':self.dropBox})
        self.files_to_upload = files_to_upload

    def start(self):
        for account_id in self.files_to_upload:
            if account_id is not None:
                accounts = APIReciever.getAccounts(-1,account_id)
                FILE = self.files_to_upload[account_id]
                for account in accounts:
                    if account[1]:
                        print account[1]
                        self.upload_to[account[0]](FILE, account[1],account_id)

    def googleDrive (self, FILE, token):
        
        gauth = GoogleAuth()
        print token
        print gauth.Auth(token)

        if gauth.credentials is None:
            self.am.connect_googleDrive

        elif gauth.access_token_expired:
            self.am.refresh_googleDrive

        else:
            print 'Google auth works - now add google uploading'
            exit(1)
            gauth.Authorize()

        drive = GoogleDrive(gauth)

        f = drive.CreateFile()
        f.SetContentFile(self.file_dir+FILE)
        f.Upload()

        print 'folder id :' + f['id']

    def mediaFire (self):
        self.am.connect_to.mediaFire()
        api = MediaFireApi()
        MF_uploader = MediaFireUploader(api)

        f = open(file_path, 'rb')
        result = MF_uploader.upload(f, FILE)
        print api.file_get_info(result.quickkey)
    
    def dropBox (self, FILE, token, account_id):
        try:
            dbx = Dropbox(token)
            head, tails = os.path.split(FILE)
            with open(FILE, 'r') as f_in:
                mode = WriteMode('overwrite', None) #ADD SOME EXCEPTIONS HERE TO CATCH IF IT DOESNT UPLAD
                dbx.files_upload(f_in, '/'+tails, mode=mode)
        except Exception as e:
            return str(e)
