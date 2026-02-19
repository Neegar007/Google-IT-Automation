#!/usr/bin/env python3

"""
STANDARD STREAMS EXPLANATION (A.K.A I/O STREAMS):
------------------------------------------------
Most operating systems provide three standard streams for input and output operations:
SDTIN  - Standard Input:  Used to get input from the user or another program.
STDOUT - Standard Output: Used to display output to the user or send it to another program.
STDERR - Standard Error:  Used to display error messages to the user or send them to another program.
In this example, we read a line of input from STDIN, write it to STDOUT,
and then attempt to write an erroneous output to STDERR.
This will generate a TypeError since we are trying to concatenate a string with an integer.
---------------------------------------------------------
cat also command writes to STDOUT:
cat greeting.txt [It reads the file and outputs its content to STDOUT]
------------------------------------------------
wrong command too generate error to STDERR:
ls -z [The -z flag is invalid for ls command and will generate an error message to STDERR]
NOTE : I/O streams are ways for programs to get and receive information.
"""
# Read input from standard input (keyboard)
data = input("This will come from STDIN: ") 
# Write output to standard output (console)
print("Now we write it to STDOUT: " + data)
# Write erroneous output to standard error (console) 
print("Now we generate an error to STDERR: " + data + 1)