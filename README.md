# inet_4031_adduser_script
# create-users.py - Automated Linux User Creation Script

## Program Description 

This script ('create-users.py') is designed to automate the process of adding multiple users to a Linux system, by reading user data from an input file ('create-users.input') that creates user accounts, sets their passwords, and assigns them groups. This method is expecially useful when setting up a new server, or managing multiple systems. Script written in Python, but mimics some common sys.admin automation patterns. 

---

### Prerequisites:
- Must be run on a Linux system, with both sudo/root permissions
- Python 3 installed
- Input file has to follow this format:
"username:password:lastname:firstname:group1,group2"

---

### Example Line in Input File:
'user04:pass04:Last04:First04:group01,group02


--- 

### How to Run 
1. **Make the script executable**
   '''bash
   chmod +x create-users.py

2. **Dry Run mode**
- make sure the os.system() lines are commented out
- leave the print(cmd) lines uncommented to see what would run
- bash command: ./create-users.py < create-users.input

3. **Actual Run mode**
- uncomment the previous os.system() lines to enable real changes
- bash command: sudo ./create-users.py < create-users.input  
