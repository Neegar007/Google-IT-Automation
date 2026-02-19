#!/usr/bin/env python3

# This script searches through a log file for specific request messages
# provided by the user and writes the found requests to a new log file.
# It takes the log file path as a command-line argument.


import sys
import os
import re

def error_search(log_file):
  requests = input("What is the request? ")
  returned_requests = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      requests_patterns = ["GET"]
      for i in range(len(requests.split(' '))):
        requests_patterns.append(r"{}".format(requests.split(' ')[i].lower()))
      if all(re.search(requests_pattern, log.lower()) for requests_pattern in requests_patterns):
        returned_requests.append(log)
    file.close()
  return returned_requests

def file_output(returned_requests):
  # os.expanduser('~') gets the home directory of the user
  with open(os.path.expanduser('~') + '/Logging/requests_found.log', 'w') as file:
    for request in returned_requests:
      file.write(request)
    file.close()

    
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_requests = error_search(log_file)
  file_output(returned_requests)
  sys.exit(0)