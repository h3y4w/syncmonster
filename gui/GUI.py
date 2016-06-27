import sys 
import wx  
import FileDB
import syncmonster-desktop.File

class Mywin(wx.Frame): 
            
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title, size =(600,300)) 
                
        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL)
                
        self.lst = wx.ListCtrl(panel, -1, style = wx.LC_REPORT) 
        self.lst.InsertColumn(0, 'File Name', width = 150) 
        self.lst.InsertColumn(1, 'size', wx.LIST_FORMAT_RIGHT, 100) 
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
        files = FileDB.update()
        print 'Updating Files...'
        for f in files: #same as above
            index = self.lst.InsertStringItem(sys.maxint, f[1]) # file name
            self.lst.SetStringItem(index, 1, str(f[2])) # add later
            self.lst.SetStringItem(index, 2, str(f[2])) #sets parts
            self.lst.SetStringItem(index, 3, str(f[0])) # file id
        wx.CallLater(5000, self.update_files)

    def openFile(self, e):
        fileDialog = wx.FileDialog(self, "Open")
        fileDialog.ShowModal()
        file_path = fileDialog.GetPath()
        fileDialog.Destroy()

    def deleteButton (self, e):
        item = self.lst.GetFocusedItem()
        file_id = self.lst.GetItem(item, 3).GetText()
        if file_id:
            FileDB.delete(file_id)
            self.lst.DeleteItem(self.lst.GetFocusedItem())

    def downloadButton (self, e):
        print self.lst.GetItemText(self.lst.GetFocusedItem())
  
FileDB = file_checker.FileDB()
files = FileDB.update()
ex = wx.App() 
frame = Mywin(None,'SyncMonster') 
frame.Show()
ex.MainLoop()
