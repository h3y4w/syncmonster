import os
import requests
import accountmanager
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from mediafire import MediaFireApi, MediaFireUploader
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

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
        am.connect_to.mediaFire()
        api = MediaFireApi()
        MF_uploader = MediaFireUploader(api)

        f = open('outputs/'+FILE, 'rb')
        
        result = MF_uploader.upload(f, FILE)

        print api.file_get_info(result.quickkey)

    def dropBox (self):
        dbx = am.connect_dropBox()
        with open('outputs/' +FILE, 'r') as f_in:
            mode = WriteMode('add', None) #ADD SOME EXCEPTIONS HERE TO CATCH IF IT DOESNT UPLAD
            dbx.files_upload(f_in, '/'+FILE, mode=mode)
            print 'UPLOADED'

class Downloader (object):

    def googleDrive(self):
        f = drive.CreateFile({'id':f_id})
        f.GetContentFile(FILE)

    def mediaFire (self):
        pass
    
    def dropBox (self):
        dbx = am.connect_dropBox()
        dbx.files_download_to_file('downloaded_files/'+FILE,'/'+FILE)
        print 'DOWNLOADED'

FILE = 'HowFast.ogg.gz.part0'
am = accountmanager.AccountManager()
download_from = Downloader()
download_from.dropBox()
