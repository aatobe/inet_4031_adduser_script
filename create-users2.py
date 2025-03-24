# INET4031
# Abdurahman Tobe
# Date Created: 2025-03-22
# Last Modified: 2025-03-22

import os  # Allows for system commands like "adduser" and "passwd"
import re  # Filters out comment lines using regular expressions
import sys  # Allows access to stdin for reading input line by line

def main():
	'''

	This script supports real execution AND a dry-run mode.
	- If the user enters "Y", the script is run in **test mode**.
	 In test mode:
	 - No system cmds are executed.
	 - Instead, script will print out the exact OS commands that WOULD be run.
	 - Outputs printed messages for skipped lines or false input lines.

	- If user enters "N", the script is run in **normal mode**.
	 In normal mode:
	 - Script adds users, sets passwords, assigns groups via OS commands.
	 - Quietly ignores false or skipped lines without outputting anything.

	'''
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().lower()
    dry_run = dry_run_input == 'y'

    with open("create-users.input", "r") as f:
        for line_num, line in enumerate(f, start=1):
            # Ignores lines that begin with "#" (used as comments in input file)
            match = re.match("^#", line)
            # Splits each input line into fields using ":" as delimiter
            fields = line.strip().split(':')

            # Skips line if it's a comment, or doesn't contain exactly 5 fields
            if match:
                if dry_run:
                    print(f"[Line {line_num}] Skipped (comment line): {line.strip()}")
                continue

            if len(fields) != 5:
                if dry_run:
                    print(f"[Line {line_num}] ERROR: Invalid number of fields ({len(fields)} instead of 5): {line.strip()}")
                continue

            # Extracting user info from the fields
            username = fields[0]  # Linux user to create
            password = fields[1]  # Initial password for the user above
            gecos = "%s %s,,," % (fields[3], fields[2])  # the full name of user in GECOS format; "First Last..."
            groups = fields[4].split(',')

            # Creating User
            print("==> Creating account for %s..." % (username))
            cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
            if dry_run:
                print(f"[Dry Run] Would run: {cmd}")
            else:
                os.system(cmd)

            # Setting User Password
            print("==> Setting the password for %s..." % (username))
            cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
            if dry_run:
                print(f"[Dry Run] Would run: {cmd}")
            else:
                os.system(cmd)

            # Looping through each assigned group, adding user to each one (unless it's a dash)
            for group in groups:
                if group != '-':
                    print("==> Assigning %s to the %s group..." % (username, group))
                    cmd = "/usr/sbin/adduser %s %s" % (username, group)
                    if dry_run:
                        print(f"[Dry Run] Would run: {cmd}")
                    else:
                        os.system(cmd)

if __name__ == '__main__':
    main()
