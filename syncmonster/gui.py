import sys 
import wx  
import APIReciever
import pynotify

class Mywin(wx.Frame): 
            
    def __init__(self, parent, title): 

        super(Mywin, self).__init__(parent, title = title, size =(400,300)) 
        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL)
                
        self.lst = wx.ListCtrl(panel, -1, style = wx.LC_REPORT) 
        self.lst.InsertColumn(0, 'File Name', width = 200) 
        self.lst.InsertColumn(1, 'Size(mb)', wx.LIST_FORMAT_RIGHT, 100) 
        self.lst.InsertColumn(2, 'parts', wx.LIST_FORMAT_RIGHT, 100) 
        self.lst.InsertColumn(3, 'file id', wx.LIST_FORMAT_RIGHT, 0)
       
        self.update_files()

        self.upload_button = wx.Button(panel, label='Upload')
        self.download_button = wx.Button(panel, label='Download')
        self.delete_button = wx.Button(panel, label='Delete')
        self.settings_button = wx.Button(panel, label='Settings')

        self.upload_button.Bind(wx.EVT_BUTTON, self.openFile)
        self.download_button.Bind(wx.EVT_BUTTON, self.downloadButton)
        self.delete_button.Bind(wx.EVT_BUTTON, self.deleteButton)
        self.settings_button.Bind(wx.EVT_BUTTON, self.settingsButton)
        # add bind for settings

        box.Add(self.lst,1,wx.EXPAND)
        box.Add(self.upload_button, 0, wx.ALL | wx.EXPAND, 5)
        box.Add(self.download_button, 0, wx.ALL | wx.EXPAND, 5)
        box.Add(self.delete_button, 0,wx.ALL | wx.EXPAND,5)
        box.Add(self.settings_button,0,5) 
        #wx.ALL | wx.EXPAND, 5

        panel.SetSizer(box) 
        panel.Fit() 
        self.Centre() 

    def update_files (self):
        self.lst.DeleteAllItems()
        try:
            user_id = '1' #TEMPORARY - SETUP OAUTH
            files = APIReciever.getFiles(user_id)
                
            print 'Updating Files...'
            for f in files: #same as above
                index = self.lst.InsertStringItem(sys.maxint, str(f[1])) # file name
                self.lst.SetStringItem(index, 1, str(f[2])) # add later
                self.lst.SetStringItem(index, 2, str(f[0])) #sets parts
                self.lst.SetStringItem(index, 3, str(f[0])) # file id
        except:
            pass
        wx.CallLater(5000, self.update_files)

    def openFile(self, e):
        fileDialog = wx.FileDialog(self, "Open")
        fileDialog.ShowModal()
        file_path = fileDialog.GetPath()
        fileDialog.Destroy()
        if file_path:
            raw_accounts = APIReciever.getAccounts('1') # change when oauth is added (user_id)
            accounts = []
            for account in raw_accounts:
                accounts.append( account[2])
            multidlg  = wx.MultiChoiceDialog(self,
                                            'File Settings',
                                            'What accounts would you like to upload to?',
                                            accounts)
        multidlg.ShowModal()
        choices = multidlg.GetSelections()
        parts = len(choices) # using this you know how many times to split the file
        print raw_accounts[choices[0]][1]

        self.showNotify('Uploaded File')

    def deleteButton (self, e):
        item = self.lst.GetFocusedItem()
        file_id = self.lst.GetItem(item, 3).GetText()
        if file_id:
            name = self.lst.GetItemText(self.lst.GetFocusedItem())
            dlg = wx.MessageBox("Would you like to delete " + name + '?', 'Delete', wx.YES_NO | wx.NO_DEFAULT)
            if dlg == 2:
                #make sure to add authentication
                APIReciever.deleteFile(file_id)
                self.lst.DeleteItem(self.lst.GetFocusedItem())

    def downloadButton (self, e):
        print self.lst.GetItemText(self.lst.GetFocusedItem())
        self.showNotify('Finished Download')

    def showNotify (self, message):
        pynotify.init('Message')
        notice = pynotify.Notification('SyncMonster', message)
        notice.show()


    def settingsButton(self, e):
        settingsFrame = SettingsWin(None,'Settings') 
        settingsFrame.Show()

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
