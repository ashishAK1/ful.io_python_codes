import re

def is_valid_contact_number(number):
    patterns = [
        r'^\d{10}$',                         # 2124567890
        r'^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$',  # 212-456-7890, 212.456.7890, 212 456 7890
        r'^\(\d{3}\)[-.\s]?\d{3}[-.\s]?\d{4}$',  # (212)456-7890, (212)-456-7890
        r'^\+\d{11}$',                       # +12124567890
        r'^\+\d{1}\s\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$',  # +1 212.456.7890
        r'^\+\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$',  # +212-456-7890
        r'^1-\d{3}-\d{3}-\d{4}$',            # 1-212-456-7890
    ]
    
    # Checking if the number matches any of the patterns
    for pattern in patterns:
        if re.match(pattern, number):
            return True
    return False

# user input
contact_number = input("Enter a contact number: ")

if is_valid_contact_number(contact_number):
    print(f"{contact_number} is a valid contact number.")
else:
    print(f"{contact_number} is an invalid contact number.")
