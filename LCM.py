# Read two numbers
a = int(input())
b = int(input())

# Calculate and print LCM
m = a*b
while b != 0:
  a,b = b, a%b
lc = int(m/a)
print("LCM:",lc)
