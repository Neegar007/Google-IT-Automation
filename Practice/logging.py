#!/usr/bin/env python3

# This script searches for lines that contain 'GET' requests
# in a log file that user specify 
# and writes those lines to a new file.
import sys

def extract_get_requests(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    get_lines = [line for line in lines if 'GET' in line]

    with open(output_file, 'w+') as f:
        f.writelines(get_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python logging.py <input_log_file> <output_log_file>")
        sys.exit(1)

    input_log_file = sys.argv[1]
    output_log_file = sys.argv[2]

    extract_get_requests(input_log_file, output_log_file)
    print(f"Extracted GET requests from {input_log_file} to {output_log_file}")