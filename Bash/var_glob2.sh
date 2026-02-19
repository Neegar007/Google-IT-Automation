# Special Variables

$0 - The name of the Bash script.
$1 - $9 - The first 9 arguments to the Bash script. (As mentioned above.)
$# - How many arguments were passed to the Bash script.
$@ - All the arguments supplied to the Bash script.
$? - The exit status of the most recently run process.
$$ - The process ID of the current script.
$USER - The username of the user running the script.
$HOSTNAME - The hostname of the machine the script is running on.
$SECONDS - The number of seconds since the script was started. 
$RANDOM - Returns a different random number each time is it referred to.
$LINENO - Returns the current line number in the Bash script. 

--------------------------------------------------------------------------------
cut -d' ' # cut is like split() function in python. The -d flag is the delimeter
# in this case, ' ' . to select the field or index where the data we want 
# is located, we use -f[index num]-. e.g -f5-. the dash after -f5 means onward
# Hence from field 5 onward