# Read input
day = int(input())
month = int(input())
year = int(input())

# Check and print
valid = True

# Check month
if month < 1 or month > 12:
    valid = False

# Days in each month
elif month in [1, 3, 5, 7, 8, 10, 12]:
    if day < 1 or day > 31:
        valid = False

elif month in [4, 6, 9, 11]:
    if day < 1 or day > 30:
        valid = False

# February
else:
    # Leap year check
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if day < 1 or day > 29:
            valid = False
    else:
        if day < 1 or day > 28:
            valid = False

if valid:
    print("Valid")
else:
    print("Invalid")
