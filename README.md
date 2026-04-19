 Basic Password Strength Checker

Author: Ayomikun Akinade  

 Overview  
This project is a simple Python script that checks whether a given password is weak based on a predefined list of commonly used passwords.

It helps demonstrate the importance of avoiding easily guessable passwords in cybersecurity.

 Objective  
To understand basic password security concepts and demonstrate how weak passwords can be easily identified using simple logic.

 How It Works  

The script compares a user-input password against a list of commonly used weak passwords.

If the password matches any entry in the list, it is flagged as weak.

Code Logic  

- A list of common weak passwords is defined  
- User inputs a password  
- The script checks if it exists in the list  
- Outputs whether the password is weak or acceptable  

 Usage  

Run the script using:

```bash id="run_cmd"
python password_checker.py
