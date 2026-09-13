def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False


email = input("Enter email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
