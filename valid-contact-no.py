import re

def is_valid_contact_number(number):
    # Regular expression pattern for valid contact number
    pattern = r'^(\+?[0-9]+)?(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})$'
    
    is_match = re.match(pattern, number)
    
    if is_match:
        return True
    else:
        return False

contact_number = input("Enter a contact number: ")

if is_valid_contact_number(contact_number):
    print(f"{contact_number} is a valid contact number.")
else:
    print(f"{contact_number} is an invalid contact number.")
