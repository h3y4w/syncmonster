#!/usr/bin/env python
import os
import time
import gzip
import shutil
import sys
import ntpath
import appdirs

class File (object):
    temp_dir = None
    file_path = None
    split_names = []
    compressed_file = None
    split_ext = None

    def __init__ (self, file_path):

        self.file_path = file_path
        file_dir, self.FILE = ntpath.split(self.file_path)
        del file_dir
        self.compressed_file = self.FILE + '.gz'
        self.compressed_path = os.path.join(self.temp_dir + self.FILE + '.gz')
        self.split_ext = self.FILE + '0'

    def split (self,pieces):
                # Split into x files
                f_in = None
                if self.compressed_file:
                    f_in = self.compressed_file #shorten this
                else:
                    f_in = self.file_path
                f = open(f_in, 'rb')
                data = f.read()
                f.close()

                bytes = len(data)
                inc = (bytes+pieces)/pieces
                counter = 0
                for i in range(0, bytes+1, inc):
                    split_name = "%s.part%d" % (self.compressed_file, counter)
                    split_dir = "%s.part%d" % (self.compressed_path, counter)
                    self.split_names.append(split_name)
                    f = open(split_dir, 'wb')
                    f.write(data[i:i+inc])
                    f.close()
                    counter +=1
                return self.split_names

    def join(self):
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
        with open(self.file_path, 'rb') as f_in, gzip.open(self.compressed_file, 'wb') as f_out: #gets files path and compresses it with .gz format
            shutil.copyfileobj(f_in, f_out)

    def decompress(self):
        with gzip.open(self.compressed_file, 'rb') as f_in, open(self.FILE, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

        os.remove(self.compressed_file)

