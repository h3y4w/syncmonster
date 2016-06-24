import dropbox
from mediafire import MediaFireApi
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import webbrowser


class AccountManager (object):
    connectedAccounts = None

    def refresh_googleDrive (self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("gDrivecreds.txt")
        gauth.Refresh()
        gauth.SaveCredentialsFile("gDrivecreds.txt")

    def connect_googleDrive (self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("gDrivecreds.txt")
    def connect_mediaFire (self):
        api = MediaFireApi()
        session = api.user_get_session_token(
                email='hmeteke@syncmonster.io',
                password='******',
                app_id='ENTER THAT HERE'
        )
        api.session = session

        response = api.user_get_info()
        print(response['user_info']['display_name'])
    
    def connect_dropBox (self):
        app_key = 'tzhked17hdn328j'
        app_secret = ''
        
        try:
            flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
            url = flow.start()
            webbrowser.open(url)
            code = raw_input("Code: ").strip()
            access_token, user_id = flow.finish(code) 
            client = dropbox.client.DropboxClient(access_token)
            return True

        except:
            return False

