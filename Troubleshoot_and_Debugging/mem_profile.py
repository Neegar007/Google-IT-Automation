#!/usr/bin/env python3

# This script demonstrates how to use the memory_profiler library 
# to profile the memory usage of a function that converts a list of 
# integers into a hash table (dictionary).


from memory_profiler import profile

# Convert a list of intergers into a hash table
@profile
def list_to_hash_table(lst):
    hash_table = {}
    for i in lst:
        hash_table[i] = True
    return hash_table

if __name__ == "__main__":
    lst = list(range(1000000))
    hash_table = list_to_hash_table(lst)
    print(hash_table[999999])