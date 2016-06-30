#!/usr/bin/env python
import os
import time
import gzip
import shutil
import sys
import ntpath
import appdirs
# This class does a various of methods to manipulate a file a user uploads
class File (object):
    temp_dir = None
    file_path = None
    split_names = []
    compressed_file = None
    split_ext = None

    def __init__ (self, file_path):

        self.file_path = file_path
        file_dir, self.FILE = ntpath.split(self.file_path)
        del file_dir #not needed
        self.split_ext = self.FILE + '0'

    def split (self,pieces,account): #splits files into x numbers of pieces
                # Split into x files
                split_files = {} # holds all files which correlate to which account it will be uploaded to
                f = open(self.file_path, 'rb')
                data = f.read()
                f.close()

                bytes = len(data)
                inc = (bytes+pieces)/pieces
                counter = 0
                for i in range(0, bytes+1, inc):
                    name = "%s.part%d" % (self.file_path, counter)
                    split_dir = "%s.part%d" % (self.file_path, counter) # CHOOSE WERE TO TEMP STORE SPLIT FILES
                    split_files[account[counter]] = name
                    f = open(split_dir, 'wb')
                    f.write(data[i:i+inc])
                    f.close()
                    counter +=1
                return split_files

    def join(self): #joins x amount of split files together
            dataList = []

            for fn in os.listdir(self.temp_dir):
                if fn.startswith(self.FILE):
                    f = open('outputs/'+fn, 'rb')
                    dataList.append(f.read())
                    f.close()

            f = open(self.compressed_file, 'wb')
            for data in dataList:
                f.write(data)
            f.close()

    def compress(self):
        #If os.path(file_path) == file then compress with gzip ELSE compress with zip format ~~ PSUEDO CODE ## Have to add folder compressor
        with open(self.file_path, 'rb') as f_in, gzip.open(self.compressed_file, 'wb') as f_out: #gets files path and compresses it with .gz format
            shutil.copyfileobj(f_in, f_out)

    def decompress(self): #if os.basename(file) == gz then decompress with GZIP IF it == zip then decompress with ZIP
        with gzip.open(self.compressed_file, 'rb') as f_in, open(self.FILE, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

        os.remove(self.compressed_file) # cleans up temp folder in APP directory

