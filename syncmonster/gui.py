import sys 
import wx
import files
import APIReciever
import pynotify
import uploader

# TO DOOOOOOOOOOOOOOOOOOOOOOOOOOOOO:
# MAKE SEPERATE FILE FOR FILE HANDLING TO KEEP THIS WINDOW GUI ONLY!!!!

class Mywin(wx.Frame): 
    user_id = 7 # MAKE SURE OT CHANGE FOR AUTHENTICATION            
    def __init__(self, parent, title): 
        

        super(Mywin, self).__init__(parent, title = title, size =(400,300)) 
        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL)
                
        self.lst = wx.ListCtrl(panel, -1, style = wx.LC_REPORT) # Creates List to Display files and sets column headers
        self.lst.InsertColumn(0, 'File Name', width = 200) 
        self.lst.InsertColumn(1, 'Size(mb)', wx.LIST_FORMAT_RIGHT, 100) 
        self.lst.InsertColumn(2, 'parts', wx.LIST_FORMAT_RIGHT, 100) 
        self.lst.InsertColumn(3, 'file id', wx.LIST_FORMAT_RIGHT, 0)
       
        self.update_files()

        self.upload_button = wx.Button(panel, label='Upload') # Creates Buttons on main frame 
        self.download_button = wx.Button(panel, label='Download')
        self.delete_button = wx.Button(panel, label='Delete')
        self.settings_button = wx.Button(panel, label='Settings')

        self.upload_button.Bind(wx.EVT_BUTTON, self.openFile) # assigns buttons to methods
        self.download_button.Bind(wx.EVT_BUTTON, self.downloadButton)
        self.delete_button.Bind(wx.EVT_BUTTON, self.deleteButton)
        self.settings_button.Bind(wx.EVT_BUTTON, self.settingsButton)

        box.Add(self.lst,1,wx.EXPAND)
        box.Add(self.upload_button, 0, wx.ALL | wx.EXPAND, 5)
        box.Add(self.download_button, 0, wx.ALL | wx.EXPAND, 5)
        box.Add(self.delete_button, 0,wx.ALL | wx.EXPAND,5)
        box.Add(self.settings_button,0,5) 
        #wx.ALL | wx.EXPAND, 5

        panel.SetSizer(box) 
        panel.Fit() 
        self.Centre() 

    def update_files (self): # refreshes the file list on the main frame
        self.lst.DeleteAllItems()
        try:
            files = APIReciever.getFiles(self.user_id) #CHANGE USER_ID
                
            for f in files: #same as above
                index = self.lst.InsertStringItem(sys.maxint, str(f[1])) # file name
                self.lst.SetStringItem(index, 1, str(f[2])) # add later
                self.lst.SetStringItem(index, 2, str(f[0])) #sets parts
                self.lst.SetStringItem(index, 3, str(f[0])) # file id
        except:
            pass
        wx.CallLater(15000, self.update_files)

    def openFile(self, e): #Lets user select file or folder to upload
        fileDialog = wx.FileDialog(self, "Open")
        fileDialog.ShowModal()
        file_path = fileDialog.GetPath()
        fileDialog.Destroy()

        if file_path:
            raw_accounts = APIReciever.getAccounts(self.user_id,-1) # change when oauth is added (user_id) #- Change the user id every time
            accounts = ['Compress File (zip for folder, gzip for file)'] # MAKE IT ALSO RETURN ACCOUNT ID
            accounts_id = []
            for account in raw_accounts:
                accounts.append( account[1])
                accounts_id.append(account[0])
            multidlg  = wx.MultiChoiceDialog(self,
                                            'File Upload Settings',
                                            'What accounts would you like to upload to?',
                                            accounts)
            while True:
                multidlg.ShowModal()
                choices = multidlg.GetSelections()
                parts = 0 # Holds how many pieces to split the file
                upload_to = [] #holds the accounts user wants to uplad to
                compress = None #To compress or not to compress

                if choices[0] != 0: # user chose not to compress file
                    parts = len(choices) 
                    compress = False

                else: # user chose to compress file so we subtract 1 from the list because we dont want the file to be split more
                    parts = len(choices) - 1
                    compress = True
                    choices.pop(0) # Removes 'Compress' option from list to allow only accounts in it
                
                
                if parts is not 0: # makes sure that they choose at least one account to upload it too
                    for choice in choices:
                        upload_to.append(accounts_id[choice-1]) # associates a split file to an account_id

                    
                    File = files.File(file_path) # creates instances of File from files.py which allows file manipulation
                    
                    if compress is True:
                        pass

                    files_to_upload = File.split(parts, upload_to)
                    upload = uploader.Uploader(files_to_upload)
                    print upload.start()

                    self.showNotify('Uploaded File')
                    break

                elif multidlg.ShowModal() is not None: # if a user click cancel or exit it doesnt bring it again
                    multidlg.Destroy()
                    break

                else: # reopens the dialog if they press OK without selecting any options
                    print multidlg.ShowModal()
                    continue



    def deleteButton (self, e): # lets user select a file or folder to delete
        item = self.lst.GetFocusedItem()
        file_id = self.lst.GetItem(item, 3).GetText()
        if file_id:
            name = self.lst.GetItemText(self.lst.GetFocusedItem())
            dlg = wx.MessageBox("Would you like to delete " + name + '?', 'Delete', wx.YES_NO | wx.NO_DEFAULT)
            if dlg == 2:
                #make sure to add authentication 
                APIReciever.deleteFile(file_id) #send a request to delete file to API 
                self.lst.DeleteItem(self.lst.GetFocusedItem())

    def downloadButton (self, e):
        print self.lst.GetItemText(self.lst.GetFocusedItem())
        self.showNotify('Finished Download')

    def showNotify (self, message): #sends a computer hud notification
        pynotify.init('Message')
        notice = pynotify.Notification('SyncMonster', message)
        notice.show()


    def settingsButton(self, e):
        settingsFrame = SettingsWin(None,'Settings') 
        settingsFrame.Show()

class LoginWin(wx.Dialog): #display to make sure user logs in
    authorize = False
    def __init__(self, parent, title):

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
          
        self.email_q = wx.TextCtrl(panel, -1, size=(140, -1))
        self.password_q = wx.TextCtrl(panel)
                
        login_button = wx.Button(panel, label='Login In')
        login_button.Bind(wx.EVT_BUTTON, self.loginButton)

        box.Add(self.email_q)
        box.Add(self.password_q)
        box.Add(login_button, 0, wx.ALL | wx.EXPAND, 5)


        panel.SetSizer(box)
        panel.Fit()
        self.Centre()

    def loginButton(self, e):
        email = self.email_q.GetValue()
        password = self.password_q.GetValue()
        self.authorize=APIReciever.authenticateUser(email, password)

class SettingsWin(wx.Frame):
    def __init__(self, parent, title):

        super(SettingsWin, self).__init__(parent, title = title, size =(300,300))
        
        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL)


        panel.SetSizer(box) 
        panel.Fit() 
        self.Centre() 

ex = wx.App() 
frame = Mywin(None,'SyncMonster') 
frame.Show()
ex.MainLoop()
