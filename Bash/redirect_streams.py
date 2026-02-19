REDIRECTION is a process of redirecting the STDOUT to another destination


cat stdout_example.py 
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")
./stdout_example.py 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py > new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py >> new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
 #Don't mind me, just a bit of text here...
cat streams_err.py 
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
./streams_err.py < new_file.txt 2> error_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
cat error_file.txt 
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt 
#These are the contents of the file
