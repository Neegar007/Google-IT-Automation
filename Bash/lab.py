#!/usr/bin/env python3

import sys
import subprocess


# file = sys.argv[1]    
with open("file_list.txt", "r") as f:  
        lines = f.readlines()
for line in lines:
    line.strip()
    new = line.replace("jane", "jdoe")
    subprocess.run(["mv", line, new])