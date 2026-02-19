#!/bin/bash

# Example showing while loop in bash
n=1
while [ $n -le 5 ]; do
    echo "iteration number $n"
    ((n++))
done