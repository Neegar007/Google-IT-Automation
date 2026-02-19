#!/bin/bash

total=0

for file in /var/log/*log; do
    logfile=$(basename "$file" .log)
    echo "Log files are : $logfile"
    ((total++))
done;
echo
echo "$total total result" 