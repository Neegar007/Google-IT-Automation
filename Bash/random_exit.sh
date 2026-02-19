#!/bin/bash

n=1

# In python, we access the terminal value with sys.argv(1)
# in bash, $1
command="$1"
# On the terminal, this file and random_exit.py will be run together 
# the python file will produce a number that will be captured by $1 var.

while ! command && [ $n -le 5 ]; do
    echo "Retry #$n"
    sleep "$n"
    ((n++))
done;