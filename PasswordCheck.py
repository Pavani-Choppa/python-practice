# Read the password
password = input().strip()

# Check length and print
if len(password) >= 8:
    print("Valid")
else:
    print("Invalid")
