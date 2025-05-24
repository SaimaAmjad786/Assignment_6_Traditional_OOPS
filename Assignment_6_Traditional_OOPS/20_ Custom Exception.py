# Custom Exception class
class InvalidAgeError(Exception):
    """Raised when the age is less than 18"""
    pass

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted. Age is valid.")

# Test the function with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid number.")