#!/bin/bash

# looping through the logfiles

for logfile in /var/log/syslog; do # Loop through anyfiles that ends with .log
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done