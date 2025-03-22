#!/usr/bin/python3

# INET4031
# Abdurahman Tobe
# Date Created: 2025-03-22
# Last Modified: 2025-03-22



import os # Allows for system commands like "adduser" and "passwd"
import re # Filters out comment lines using regular expressions
import sys # Allows access to stdin for reading input line by line


def main():
    for line in sys.stdin:

	# Ignores lines that begin with "#" (used as comments in input file)
        match = re.match("^#",line)

	# Splits each input line into fields using ":" as delimiter
        fields = line.strip().split(':')


	# Skips line if it's a comment, or if it does not contain exactly 5 fields
	# Makes sure only well formed, non commented entries are processed
        if match or len(fields) != 5:
            continue


	# Extracting individual user info from the fields

        username = fields[0] # Linux user to create 
        password = fields[1] # Initial password for the user above
        gecos = "%s %s,,," % (fields[3],fields[2]) # the full name of user in GECOS format; "First Last..."

        # Splitting group field into a list of groups that are comma separated
        groups = fields[4].split(',')

        # Print statement notifying admin that user account creation has started
        print("==> Creating account for %s..." % (username))
        # Building the shell command that creates the user without a password, but with full name
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

        #REPLACE THIS COMMENT - what is the point of this print statement?
        print("==> Setting the password for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain. You'll need to lookup what these linux commands do.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

	# Looping through each assigned group, adding user to each one
        for group in groups:
            # If group isn't just placeholder ("-"), start process of adding the user to it 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
