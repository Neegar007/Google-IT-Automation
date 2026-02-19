#!/usr/bin/bash

# grep is a regular expression to
# search for text patterns inside files or command output
# Basically, grep finds lines that match what you’re looking for.
# -------------------------------------------------------------------
# Check id 127.0.0.1 can be found in /etc/hosts dir
# Succesfull command execution return exit status of zero (0) while failed one returns numbers other 
# than 0.
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything Ok"
else
    echo "Error: 127.0.0.1 is not in etc/hosts"
fi # To end the conditional statement


# ------------------------------------------------------------------

# Test is a command that evaluates the conditions received and 
# exits with zero when they are true and with one when they're false. 
# E.g -n checks if a var is empty. Test receives the condition for
# evaluation 
# ; in bash means end of line
if test -n "$PATH"; then echo "Path not empty"; fi
# Alternative way of writing test. Space must be btw the square brackets
if [ -n "$PATH" ]; then echo "Path not empty"; fi