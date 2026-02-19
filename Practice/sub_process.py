#!/usr/bin/activate

# This script run a Linux command to change the permission on a file

import subprocess
# This command changes the permission of the file 'flowers.csv' to 
# 755 meaning read, write, and execute for the owner, and read and 
# execute for group and others
permission = subprocess.run(['chmod', '755', '../flowers.csv'])
print("Permission changed with return code:", permission.returncode)