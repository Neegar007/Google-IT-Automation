

"""
SIGNALS are tokens delivered to running processes to indicate a desied action.
Using signals, we can tell a program that we want it to pause or terminate. 
We can also cause it to reload its configuration, or to close all open files.
Knowing how to send these signals lets us interact with processes and have
more control over how they behave. 
# Run the following ate the command line

ping www.example.com

press ctrl C to stop the process, SIGNT signal
ctrl Z to pause , SIGSTOP
run 'fg' to continue

Open another terminal
---------------------------------
run : ps ax | grep ping 
---------------------------------
ps : list the current processes
ps ax : list all the running processes on the current computer
grep : And then we'll use the grep command to only keep lines that contain 
the name of the process that we're looking for. In this case, ping processes
this will list the ping process that is running. The Proces ID with 
other info will be displayed.
Run :
kill [ID] to terminate the process. SIGTERM signal

Operating with processes
These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

ps: lists the processes executing in the current terminal for the current user

ps ax: lists all processes currently executing for all users  

ps e: shows the environment for the processes listed  

kill PID: sends the SIGTERM signal to the process identified by PID

fg: causes a job that was stopped or in the background to return to the foreground

bg: causes a job that was stopped to go to the background

jobs: lists the jobs currently running or stopped

top: shows the processes currently using the most CPU time (press "q" to quit)  
"""