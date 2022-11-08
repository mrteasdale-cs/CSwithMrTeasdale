#import aspose.words as aw
from operator import contains
import os,sys

docs = []

#for file in folder:

#doc = aw.Document("C6 Booklet 6.1")

directory_path = os.getcwd()
print("My current directory is : " + directory_path)


for root, subdirs, files in os.walk(directory_path):
    for subd in subdirs:
        subdirpath = os.path.join(directory_path, subd)

    for filename in files:

        file_path = os.path.join(subdirpath, filename)

        if "password-protect-files.py" not in file_path:

            print('\t- file %s (full path: %s)' % (filename, file_path))