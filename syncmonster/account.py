from dropbox import DropboxOAuth2FlowNoRedirect
import APIReciever
import webbrowser


class AccountManager(object):

        
    def connect_dropbox (self):
        key = 'bn8ub3zq0ytazro'
        secret = 'xbepfvaz1rzudcg'
        auth_flow = DropboxOAuth2FlowNoRedirect(key,secret)
        webbrowser.open(auth_flow.start(), new=1, autoraise=True)
        code = raw_input('code: ').strip()

        user_info = auth_flow.finish(code)

        name = raw_input('What would you like to call it?')
        r = APIReciever.AddAccount('DROPBOX', name, user_info[0])
        
    def connect_googleDrive (self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("gDrivecreds.txt")



am = AccountManager()
am.connect_dropbox()
