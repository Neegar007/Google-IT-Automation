#!/bin/bash

> oldFiles.txt

files=$(grep ' jane ' ~/data/list.txt | cut -d' ' -f 3)

if test -e $files; then

        echo "file: $files found"

else

        echo "Filename not found"

fi;



for file in $files; do 

        if test -n $file; then                  

                echo "$file" >> oldFiles.txt

        else
        fi;
done