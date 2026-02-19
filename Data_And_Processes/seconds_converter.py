#!/usr/bin/env python3

# This Function converts time to seconds. 
# It Shows how to build command line interactions.  

def to_seconds(hours, minutes, seconds):
	return hours*3600+minutes*60+seconds

print("Welcome to This time converter\n---------------------")

cont = "y"
while(cont.lower()=="y"):
	hours = int(input("Enter the number of hours :"))
	minutes = int(input("Enter The number of minutes :"))
	seconds = int(input("Enter the number of seconds :"))

	print("That's {} seconds ".format(to_seconds(hours, minutes, seconds)))
	print()
	cont = input("Do you want to do another conversion? [Enter y to continue]")

print("Thanks for the time. Goodbye.")
