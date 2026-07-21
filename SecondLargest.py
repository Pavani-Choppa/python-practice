# Read count
n = int(input())

# Read numbers and find the largest
numbers = [int(input()) for i in range(n)]

# Print the largest
big = numbers[0]
sb = numbers[0]
for i in numbers:
  if i > big:
    sb = big
    big = i
  if i > sb and i != big:
    sb = i
print("Second Largest:",sb)
