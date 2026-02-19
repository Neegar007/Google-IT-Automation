#!/bin/bash

# In bash, items of iteration are separated by space


for fruit in orange apple pear pineapple; do
    echo "I love $fruit very much"
done

# Useful example: Lets say you want to rename a couple of files with a particular
# extension. instead of renaming them one by one, you run a bash script
# we use a command 'basename' to get file name without extension

for file in *.sh; do
    name=$(basename "$file" .sh)
    echo "Renamed " "$file" " $name.html"
done 