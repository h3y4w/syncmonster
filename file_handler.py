#!/usr/bin/env python

#from gzopen import gzopen
import os
import time
import gzip
import shutil
import sys
import ntpath

class File (object):

    file_path = '/Users/deno/Programs/python/syncmonster-desktop/tests/git-2.8.1-intel-universal-mavericks.dmg'
    file_names = [] 
    compressed_file = None
    def __init__ (self):
        
        file_dir, self.FILE = ntpath.split(self.file_path)
        
        self.compressed_file = self.FILE + '.gz'
        self.split_ext = self.FILE + '0'
        self.compress()
        self.split()

        self.join()
        self.decompress()
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
                    fn1 = "outputs/%s.0%d" % (self.FILE, counter)
                    self.file_names.append(fn1)
                    f = open(fn1, 'wb')
                    f.write(data[i:i+inc])
                    f.close()
                    counter +=1

#                os.remove(self.compressed_file) # add this when it starts to automatically upload file

    def join(self):
            dataList = []
            
            for fn in os.listdir('/Users/deno/Programs/python/syncmonster-desktop/outputs/'):
                if fn.startswith(self.FILE):
                    f = open('/Users/deno/Programs/python/syncmonster-desktop/outputs/'+fn, 'rb')
                    dataList.append(f.read())
                    f.close()
            
            f = open(self.compressed_file, 'wb')
            for data in dataList:
                f.write(data)
            f.close() 
            #with gzip.open(self.compressed_file, 'wb') as f:
                #for data in dataList:
                    #f.write(data)

    def compress(self):
        with open(self.file_path, 'rb') as f_in, gzip.open(self.compressed_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    def decompress(self):
        #file_in = gzip.open(self.compressed_file, 'rb')
        #data = file_in.read()
        #file_out = file(self.FILE, 'wb')
        #file_out.write(data)

        ##file_out.write(file_in.read())
        #file_out.close()
        #file_in.close()

        with gzip.open(self.compressed_file, 'rb') as file_in:
            with open('outputs/'+self.FILE, 'wb') as file_out:
                file_out.write(file_in.read())
                file_out.close()
            file_in.close()

        os.remove(self.compressed_file)

File = File()

