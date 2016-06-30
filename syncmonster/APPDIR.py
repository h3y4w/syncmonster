import appdirs
import os


 # WHEN COMPLETED, THIS FILE WILL SET UP APPLICATION DIRECTORY CROSS PLATFORMS
appname = "SyncMonster"
appauthor = "SyncMonster"


app_path = appdirs.site_data_dir(appname, appauthor).replace('ubuntu', '')
if not os.path.exists(app_path):
    create_path = appdirs.site_data_dir(appname, appauthor)
    os.makedirs(create_path+'/temp')
    os.makedirs(create_path+'/Upload')
    
    sym_upload_dir = os.path.join(os.path.expanduser("~"), "Desktop", 'SyncMonster Upload')
    os.symlink(app_path+'/Upload', sym_upload_dir)


    print 'MADE DIR'
else:
    print '%s EXISTS' % app_path

