import re

# Custom annotation (decorator) for validation
def validate(pattern, message):
    def decorator(func):
        def wrapper(value):
            if not re.match(pattern, value):
                print(message)
                return None
            return func(value)
        return wrapper
    return decorator


# Validation functions

@validate(r"^[A-Za-z ]+$", "Invalid Name! Only letters allowed.")
def validate_name(name):
    return name


@validate(r"^[\w\.-]+@[\w\.-]+\.\w+$", "Invalid Email Format!")
def validate_email(email):
    return email


@validate(r"^\d{10}$", "Invalid Phone Number! Must be 10 digits.")
def validate_phone(phone):
    return phone


@validate(r"^EMP\d{3}$", "Invalid Employee ID! Format: EMP001")
def validate_empid(empid):
    return empid


# Employee storage
employees = {}

# Input
name = input("Enter Employee Name: ")
email = input("Enter Email: ")
phone = input("Enter Phone Number: ")
empid = input("Enter Employee ID (EMP001 format): ")

# Validation
name = validate_name(name)
email = validate_email(email)
phone = validate_phone(phone)
empid = validate_empid(empid)

# Store data
if name and email and phone and empid:
    employees[empid] = {
        "name": name,
        "email": email,
        "phone": phone
    }
    print("\nEmployee Registered Successfully!")

# Display employees
print("\nEmployee Details:")
for empid, data in employees.items():
    print("Employee ID:", empid)
    print("Name:", data["name"])
    print("Email:", data["email"])
    print("Phone:", data["phone"])
    print("----------------------")