common_passwords = ["admin", "123456", "password", "admin123"]

user_input = input("Enter password to check: ")

if user_input in common_passwords:
    print("Weak password! Choose something stronger.")
else:
    print("Password looks okay.")
