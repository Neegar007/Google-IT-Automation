#!/usr/bin/env python3
"""
Command Line Arguments (argv) in Python:
---------------------------------------
In Python, the sys module provides access to command-line arguments 
via the sys.argv list.
The first element, sys.argv[0], is the name of the script being 
executed.
Subsequent elements are the arguments passed to the script.
This allows users to provide input to the script when running it
from the command line.
This is useful for making scripts more dynamic and flexible.
And for system administration tasks where scripts need to process 
different inputs without changing the code. It allows more 
automation.
---------------------------------------
Exit Status:
In addition to command-line arguments, scripts can also return
an exit status to the operating system upon completion.
An exit status of 0 typically indicates successful execution,
while a non-zero exit status indicates an error or abnormal
termination.
This exit status can be accessed in the shell using the special
variable $? immediately after the script execution.
This is important for scripting and automation, as it allows
other programs or scripts to determine if a command executed
successfully or if there were issues that need to be handled.
E.g., after running a script, you can check the exit status:
$ python3 my_script.py arg1 arg2
$ echo $?
0  # Indicates success
1  # Indicates an error occurred
---------------------------------------
wc command example to count lines, words, and characters in a file:
$ wc myfile.txt
This command will output three numbers followed by the filename:
- The first number is the line count.
- The second number is the word count.
- The third number is the character count.
For example:
$ wc myfile.txt
10 50 300 myfile.txt
This indicates that myfile.txt contains 10 lines, 50 words, 
and 300 characters.
If you want to count only lines, words, or characters, you can use
specific flags:
- To count lines only: wc -l myfile.txt
- To count words only: wc -w myfile.txt
- To count characters only: wc -c myfile.txt
If wc runs successfully, it will return an exit status of 0.
If there is an error (e.g., file not found), it will return a
non-zero exit status.
---------------------------------------
"""
import sys

print(sys.argv)  # List of command-line arguments passed to the script

