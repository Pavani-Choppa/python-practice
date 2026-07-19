# Read the number
n = int(input())

# Calculate digit sum and print
sum = 0
while n > 0:
  rem = n % 10
  sum += rem
  n = n // 10
print("Digit sum:",sum)
