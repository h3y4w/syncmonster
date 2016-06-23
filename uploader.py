import accountmanager
from pydrive.drive import GoogleDrive

class Uploader (object):
    connectedAccounts = None

    def googleDrive (self, file_info):
        drive = GoogleDrive(gauth)
        f = drive.CreateFile({'title': file_info['name']})
        f.Upload()

    def mediaFire (self):
        pass

    def dropBox (self):
        pass

class Downloader (object):

    def from_googleDrive(self,file_info):
        f = drive.CreateFile({'id':file_info['id']})
        f.GetContentFile(file_info['name'])

