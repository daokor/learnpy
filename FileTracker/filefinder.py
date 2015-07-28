import os,glob
from os.path import join

from filemeta import *


#suffixs to check
suffixs=['.zip','.opar']
exclude_words = ['sysman','files',]


target_files = []

def get_patch_file(dir):
        for root,dirs,files in os.walk(dir):
                for file in files:
                        file_suffix = '.' + file.split('.')[-1]
                        if file_suffix in suffixs:
                                full_filename=join(root,file)
                                subdirs=full_filename.split('/')
                                if len(( set(subdirs) & set(exclude_words ) ))==0 :
                                        print target_dir +'/' + full_filename


target_dir = '/u01/dummy'
os.chdir(target_dir)
for dir in glob.glob("15.*"):
        print '---------------------------------------------------------'
        print 'checking : ' + dir
        print '---------------------------------------------------------'
        get_patch_file(dir)
