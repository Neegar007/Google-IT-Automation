#!/usr/bin/.venv python3

# This script will accept input from a file and generate STDERR 
# Instead of accepting input from the keyboard.
# run :
# ~$ python3 stderr.py < stdoutput.txt
# ~$ run:
# ~$ python3 stderr.py < stdoutput.txt 2> errorlog.txt
# This will capture the error STDERR into errorlog.txt. the 2 is a file descriptor

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")