import os
import requests
import accountmanager
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from mediafire import MediaFireApi, MediaFireUploader
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# this class allows you to download files from various services
class Downloader (object):

    def googleDrive(self):
        f = drive.CreateFile({'id':f_id})
        f.GetContentFile(FILE)

    def mediaFire (self):
        pass
    
    def dropBox (self):
        dbx = self.am.connect_dropBox()
        dbx.files_download_to_file('downloaded_files/'+FILE,'/'+FILE)
        print 'DOWNLOADED'

