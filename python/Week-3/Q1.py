import re
def is_strong_password(password):
    if len(password) < 8: # Check for at least eight characters
        return False
    if not re.search('[a-z]', password) or not re.search('[A-Z]', password): # Check for uppercase and lowercase characters
        return False
    if not re.search('[0-9]', password): # Check for at least one digit
        return False
    if not re.search('[^a-zA-Z0-9]', password): # Check for at least one special character
        return False
    return True
password = input("Enter password:")
if(is_strong_password(password)):
    print("Strong Password")
else:
    print("Weak Password")