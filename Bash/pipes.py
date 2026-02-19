#!/usr/bin/env python3

# Using pipes, you can connect multiple scripts, commands, or other programs 
# into a data processing pipeline. 
# Pipes connects the output of one program into the input of another in order to
# pass data between programs. 
# Pipe (|) is used to connect the programs

# ls -l | less [This take the output of ls command into the input of 'less'
# command which ia a python pagination program to display page by page]

import sys

for line in sys.stdin: # THis is a STDIN file handle through the commandline
    print(line.strip().capitalize())

    # On the commandline, a file will be sent to this script.
    # Run :
    # cat stdoutput.txt | python3 pipes.py

    # DIFFERENCE BTW PIPES AND RE-DIRECTION
    # For simple I/O stream , use redirection. But in a case where you want
    # to extract a content from a file, pass it to another file for processing,
    # use pipes to conect them

