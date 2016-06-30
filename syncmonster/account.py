from dropbox import DropboxOAuth2FlowNoRedirect
import APIReciever
import webbrowser

#This class when called allows user to connect to various services

class AccountManager(object): 

        
    def dropbox (self): 
        key = 'bn8ub3zq0ytazro'
        secret = 'xbepfvaz1rzudcg'
        auth_flow = DropboxOAuth2FlowNoRedirect(key,secret)
        webbrowser.open(auth_flow.start(), new=1, autoraise=True)
        code = raw_input('code: ').strip()

        user_info = auth_flow.finish(code)

        name = raw_input('What would you like to call it?')
        r = APIReciever.AddAccount('DROPBOX', name, user_info[0])
        
    def googleDrive (self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("gDrivecreds.txt")

    def mediafire (self):
        pass


connect_to = AccountManager()
connect_to.dropbox()
