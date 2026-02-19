#!/usr/bin/env python3

# Reading environment variables in Python
import os

# Get the value of the HOME environment variable
print("HOME: " + os.environ.get("HOME"))
print("SHELL: " + os.environ.get("SHELL"))
# .get() dictionary method avoids KeyError if variable is not found
# Returns ' ' if 'Fruit' variable does not exist
print("Fruit :" + os.environ.get("Fruit", " "))

# Run 'export Fruit=Apple' in terminal to set the variable before running this script
# Then run this script to see the value of the 'Fruit' environment variable
# The export command sets environment variables in the shell session