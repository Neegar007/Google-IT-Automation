#!/usr/bin/env python3

# File creation script that checks if a file exists before creating it
import os
import sys

filename=sys.argv[1] # Get the filename from command line argument

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("File created successfully.\n")
else:
    print("Error: File '{}' already exists.".format(filename))
    sys.exit(1)  # Exit with non-zero status to indicate error
