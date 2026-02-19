#!/usr/bin/env python3

# This script demonstrates the use of command-line arguments (argv) 
# in Python. The user has two options:
# 1. To print out all even numbers up to a specified limit.
# 2. To print out all odd numbers up to a specified limit.
import sys
def print_even_numbers(limit):
    print(f"Even numbers up to {limit}:")
    for num in range(2, limit + 1, 2):
        print(num, end=' ')
    
def print_odd_numbers(limit):
    print(f"Odd numbers up to {limit}:")
    for num in range(1, limit + 1, 2):
        print(num, end=' ')
    print()

# Main execution starts here
if __name__ == "__main__": # Ensure this block runs only when the script is executed directly
    if len(sys.argv) != 3:
        print("Usage: python3 cmd_argv.py <even|odd> <limit>")
        sys.exit(1)
    option = sys.argv[1].lower()
    try:
        limit = int(sys.argv[2])
    except ValueError:
        print("Please provide a valid integer for the limit.")
        sys.exit(1)
    if option == "even":
        print_even_numbers(limit)
    elif option == "odd":
        print_odd_numbers(limit)
    else:
        print("Invalid option. Use 'even' or 'odd'.")
        sys.exit(1)