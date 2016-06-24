

import os
import requests
import accountmanager
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from mediafire import MediaFireApi, MediaFireUploader

class Uploader (object):
    connectedAccounts = None

    def __init__ (self):
        self.accountmanager = accountmanager.AccountManager()

    def googleDrive (self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("gDrivecreds.txt")
        
        if gauth.credentials is None:
            self.accountmanager.connect_googleDrive

        elif gauth.access_token_expired:
            self.accountmanager.refresh_googleDrive
        
        else:
            gauth.Authorize()
        
        drive = GoogleDrive(gauth)
        
        f = drive.CreateFile()
        f.SetContentFile('CM.py')
        f.Upload()
        
        print 'folder id :' + f['id']

    def mediaFire (self):
        api = MediaFireApi()
        MF_uploader = MediaFireUploader(api)

        f = open(file_path, 'rb')
        
        result = MF_uploader.upload(f, FILE)

        print api.file_get_info(result.quickkey)
       


    def dropBox (self):
        pass

class Downloader (object):

    def googleDrive(self,file_info):
        f = drive.CreateFile({'id':f_id})
        f.GetContentFile(FILE)

    def mediaFire (self):
        pass
upload_to = Uploader()
upload_to.googleDrive()
