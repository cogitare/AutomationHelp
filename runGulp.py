#
# Helps in running CMD mode gulping and then zipping selective folder contents to zipGulp.py directory.
#
import os
os.system(r'cmd /k "gulp release --env dev & cd C:\Users\**path to folder**\resource-bundles & python zipGulp.py"')
