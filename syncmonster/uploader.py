import os
import requests
#import accountmanager
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from mediafire import MediaFireApi, MediaFireUploader
import dropbox
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
        for FILE in self.files_to_upload:
            if file is not None:
                accounts = APIReciever.getAccounts(-1,FILE)
                for account in accounts:
                    print self.upload_to[account[0]](FILE)

    def googleDrive (self, FILE):
        print "IT WORKED FOR GDRIVE NIGGA"
        exit(0) # TEMP TO TEST IT OUT
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("gDrivecreds.txt")

        if gauth.credentials is None:
            self.am.connect_googleDrive

        elif gauth.access_token_expired:
            self.am.refresh_googleDrive

        else:
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
    
    def dropBox (self, FILE):
        print "IT WORK FOR DP FAGGOT"
        exit(0) # TEMP TO TEST IT OUT
        dbx = self.am.connect_dropBox()
        with open(self.file_dir+FILE, 'r') as f_in:
            mode = WriteMode('add', None) #ADD SOME EXCEPTIONS HERE TO CATCH IF IT DOESNT UPLAD
            dbx.files_upload(f_in, '/'+FILE, mode=mode)
            print 'UPLOADED'


