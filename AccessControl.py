# Read input
role = input().strip()
age = int(input())
membership = input().strip()

# Check and print
if role == 'admin' or (age > 18 and membership == 'yes'):
  print("Access granted")
else:
  print("Access denied")
