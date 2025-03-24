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

	 #Ignores lines that begin with "#" (used as comments in input file)
        match = re.match("^#",line)

	 #Splits each input line into fields using ":" as delimiter
        fields = line.strip().split(':')


     #Skips line if it's a comment, or doesn't contain exactly 5 fields
        if match or len(fields) != 5:
            continue


	# Extracting individual user info from the fields

        username = fields[0] # Linux user to create 
        password = fields[1] # Initial password for the user above
        gecos = "%s %s,,," % (fields[3],fields[2]) # the full name of user in GECOS format; "First Last..."
        groups = fields[4].split(',')

        # Notifying admin user account creation has started
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        print(cmd)
        os.system(cmd)

        # Notifying admin user password is being set
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        print(cmd)
        os.system(cmd)

	# Looping through each assigned group, adding user to each one (unless it's a dash)
        for group in groups: 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
