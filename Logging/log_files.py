#!/usr/bin/env python3
"""
import sys

logfile = sys.argv[1]

with open(logfile) as f:
    for line in f:
        print(line.strip())
"""

"""
# Match only IP address and request method
import re
pattern = r"(\d.)+"
line = "118.148.239.174 - - [27/Dec/2037:12:00:00 +0530] PUT /usr HTTP/1.0 404 4962 http://www.parker-miller.org/tag/list/list/privacy/" "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749 1431"
result = re.search(pattern, line)
print(result[1])

"""
#!/bin/env/python3
# Using regex to extract IP addresses from log files
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "GET" not in line:
      continue
    pattern = r"[\d.]+"
    result = re.search(pattern, line)
    print(result.group())
