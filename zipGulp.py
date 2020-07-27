#
# Helps in zipping contents of folder.
# Reusable code for any tasks by adjusting variables.
#
import zipfile
import os
import sys

def zipfolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

zipfolder('vendor.resource', './vendor.resource') #insert your variables here
zipfolder('cpqSM.resource', './cpqSM.resource') #insert your variables here
zipfolder('ngCPQ.resource', './ngCPQ.resource') #insert your variables here
sys.exit()
