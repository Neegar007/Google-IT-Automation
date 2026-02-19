

"""
Environment Variables Explanation
------------------------------------------------
Environment variables are dynamic values that can affect the 
way running processes behave on a computer.
They are part of the operating system's environment and can be 
used to store configuration settings, paths, and other information
that programs can access during execution.
Common environment variables include:
A SHELL is the application that interprets commands and 
acts as an interface between the user and the operating system.
When we open a Linux terminal, the application that executes 
our commands is called a SHELL.
The most common used shells are:
- bash (Bourne Again SHell) for Linux and macOS [Most Popular]
- sh (Bourne Shell) for Unix
- csh (C Shell) for Unix
- ksh (Korn Shell) for Unix
- zsh (Z Shell) for macOS and Linux
- fish (Friendly Interactive SHell) for Linux and macOS
--------------------------------------------------------------
Python programs get executed inside a command line shell environment
(e.g., bash, zsh, cmd, PowerShell). The shell provides environment variables
that can influence the behavior of the Python interpreter and the
programs it runs.
The variables set in that environment are another source of
information we can use in our scripts.
--------------------------------------------------------------
'env' command in Linux/MacOS terminal lists all environment variables:
echo $HOME [Displays the home directory path of the current user]
echo $PATH [Displays the system PATH variable]
variables are preceeded by a $ sign when used in the linux shell.
"""
  