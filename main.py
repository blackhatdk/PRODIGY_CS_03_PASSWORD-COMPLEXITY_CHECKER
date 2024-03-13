import re


def check_password_complexity(password):
    # Length check
    if len(password) < 8:
        return "Password should be at least 8 characters long."

    # Uppercase check
    if not re.search(r"[A-Z]", password):
        return "Password should contain at least one uppercase letter."

    # Lowercase check
    if not re.search(r"[a-z]", password):
        return "Password should contain at least one lowercase letter."

    # Digit check
    if not re.search(r"\d", password):
        return "Password should contain at least one digit."

    # Special character check
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)."

    return "Password is strong."


# Test the function
password = input("Enter your password: ")
print(check_password_complexity(password))
