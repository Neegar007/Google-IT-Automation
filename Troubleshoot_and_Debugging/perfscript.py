#!/usr/bin/env python3

import sys

data = sys.argv[1]
booklist = ['Longer','Tester','Joebiden', 'Alakure']
#'Mokhtar', 'Salah', 'Hassan', 'Abdelaziz', 'Yasser', 'Mohamed']

def lookup(book):
    length = len(book)
    return length 

for book in booklist:
    if book in data:
        result = lookup(book)
        print(result)

