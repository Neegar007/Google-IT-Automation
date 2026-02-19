#!/usr/bin/env python3


import re
import operator
import csv


error_msg = {}
user_entry = {}

with open("syslog.log", "r") as logfile;