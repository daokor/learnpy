__author__ = 'ttazhang'

import socket
import os
import subprocess
import datetime

class FileMeta:
    def __init__(self, abs_filename):
        self.abs_filename = abs_filename
        self.on_host = socket.gethostname()
        self.file_name, self.file_type  = os.path.splitext(abs_filename)
        self.tag='em'
        self.cksum=0
        self.size=0
        self.creation_time=''

    # def __init__(self):
    #     pass

    # return filename
    def get_file_name(self):
        return self.file_name

    # return file suffix
    def get_file_type(self):
        return self.file_type

    # return full path for file name
    def get_abs_file_name(self):
        return self.abs_filename


    def run_cksum(self):
        cmd2cksum='/usr/bin/cksum '+self.abs_filename
        pipe = subprocess.Popen(cmd2cksum.split(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        text = pipe.stdout.readlines()[0]
        print 'DEBUG :'+text

        cksum=text.split(' ')[0]
        self.cksum=cksum
        size = text.split(' ')[1]
        self.size=size

    def get_size(self):
        if self.size==0:
            self.run_cksum()
        return self.size

    def get_cksum(self):
        if self.cksum==0:
            self.run_cksum()

        return self.cksum

    def get_creation_time(self):
        if self.creation_time=='':
            fct = os.path.getctime(self.abs_filename)
            fcn = datetime.datetime.fromtimestamp(fct)
            nm = fcn.strftime('%Y_%m%d_%H%M_%S')
            self.creation_time=nm
        return self.creation_time








one_file = FileMeta('/home/ttazhang/apache-tomcat-8.0.15/RUNNING.txt')
filename= one_file.get_file_name()
print 'filename : '+filename
print 'absfilename : '+one_file.get_abs_file_name()
print 'extension : '+one_file.get_file_type()
print 'hostname : '+one_file.on_host
print 'cksum : '+ one_file.get_cksum()
print 'creation time : '+one_file.get_creation_time()
print 'size: '+one_file.get_size()
#one_file = FileMeta()




