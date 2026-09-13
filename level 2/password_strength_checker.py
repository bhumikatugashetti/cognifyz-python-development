def check_password(password):

    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)

    score = sum([
        length,
        uppercase,
        lowercase,
        digit,
        special
    ])

    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("Length:", "PASS" if length else "FAIL")
    print("Uppercase:", "PASS" if uppercase else "FAIL")
    print("Lowercase:", "PASS" if lowercase else "FAIL")
    print("Digit:", "PASS" if digit else "FAIL")
    print("Special character:", "PASS" if special else "FAIL")
    print("Password Strength:", strength)


password = input("Enter password: ")

check_password(password)
