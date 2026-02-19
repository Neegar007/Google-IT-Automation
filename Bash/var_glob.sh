#!/usr/bin/bash

# Defining variables

line="------------------------------------" 
# variable. No space in btw var name and = sign
# var is accessed using the $ sign
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"
who
echo

echo "Finishing at: $(date)" 

# globs are like wildcard charaters

# Globs : * matches all characters. ? matches single charater
echo $line
echo "Look for files with .py extension"; echo *.py 
echo c* # will match all files that starts with letter 
echo $line
echo "Look for files with six letters"; echo ?????.*


echo "Who am I talking to?"

read varname # Read ask for user input

echo "Yoou are welcome : $varname"

read -p 'Username: ' uservar
read -sp 'Password: ' passvar
echo
echo Thankyou $uservar we now have your login details