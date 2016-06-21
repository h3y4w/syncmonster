import os
import time
import gzip
import shutil

class File (object):

    file_path = '/Users/deno/Programs/python/syncmonster-desktop/vid.mov'
    file_names = [] 
    compressed_file = None    
    def __init__ (self):
        fn, ext = os.path.splitext(self.file_path)
        self.FILE = fn + ext
        choice = int(raw_input('>'))
        if self.compressed_file is None:
            self.compressed_file = self.FILE + '.gz'
        
        if choice == 1:
            self.compress()
            self.split()
        else:
            self.join()
            self.uncompress()
    def split (self):
        pieces = 3
        # Split into x files
        f_in = None
        if self.compressed_file:
            f_in = self.compressed_file
        else:
            f_in = self.file_path
        f = open(f_in, 'rb')
        data = f.read()
        f.close()
         
        bytes = len(data)
        inc = (bytes+pieces)/pieces
        counter = 0
        for i in range(0, bytes+1, inc):
            fn1 = "part%d" % counter
            self.file_names.append(fn1)
            f = open(fn1, 'wb')
            f.write(data[i:i+inc])
            f.close()
            counter +=1

    def join(self):
        new_file = 'outputs/recreated.mov'
        dataList = []
         
        for fn in self.file_names:
            f = open(fn, 'rb')
            dataList.append(f.read())
            f.close()
         
        f = open(new_file, 'wb')
        for data in dataList:
            f.write(data)

    def compress(self):
        

        with open(self.file_path, 'rb') as f_in, gzip.open(self.compressed_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    def uncompress(self):
        file_in = gzip.open(self.compressed_file, 'rb')
        self.uncompressed_file = open(self.FILE, 'wb')
        self.uncompressed_file.write(file_in.read())
        file_in.close()
        self.uncompressed_file.close()

File = File()
