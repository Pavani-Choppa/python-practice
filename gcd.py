# Read two numbers
a = int(input())
b = int(input())

# Find the GCD
while b:
  a , b = b , a % b
# Print the result
print("GCD:",a)
