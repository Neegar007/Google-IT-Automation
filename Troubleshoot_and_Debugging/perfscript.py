#!/usr/bin/env python3

import sys

data = sys.argv[1]
booklist = ['Longer','Tester','Joebiden', 'Alakure']
#'Mokhtar', 'Salah', 'Hassan', 'Abdelaziz', 'Yasser', 'Mohamed']

for book in booklist:
    if book in data:
        print(f"{book} is found in the data.")