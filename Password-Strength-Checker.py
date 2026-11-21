print("Welcome to the Password Strength Checker!")
password = input("Enter your password: ")
has_uppercase = False
has_lowercase = False
has_digit = False
has_special_character = False
special_characters = "!@#$%^&*()-.+"
for letter in password:
    if letter.isupper():
        has_uppercase = True
    if letter.islower():
        has_lowercase = True 
    if letter.isdigit():
        has_digit = True
    if letter in special_characters:
        has_special_character = True
if len(password) >= 8:
    print("Password meets the minimum length requirement.")
else:
    print("Password is too short.")
if has_uppercase:
    print("Password contains an uppercase letter.")
else:
    print("Password has no uppercase letters.")
if has_lowercase:
    print("Password contains a lowercase letter.")
else:
    print("Password has no lowercase letters.")
if has_digit:
    print("Password contains a digit.")
else:
    print("Password has no digits.")
if has_special_character:
    print("Password contains a special character.")
else:
    print("Password has no special characters.")
if has_uppercase and has_lowercase and has_digit and has_special_character and len(password) >= 8:
    print("Strong password")
else:
    print("Password is not strong enough.")    