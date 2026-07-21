# Read count
n = int(input())

# Read numbers and find the largest
numbers = [int(input()) for i in range(n)]

# Print the largest
big = numbers[0]
for i in numbers:
  if i > big:
    big = i
print("Largest:",big)
