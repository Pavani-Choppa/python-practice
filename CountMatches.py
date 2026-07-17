# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
target = int(input())

# Count and print
count = 0
for i in numbers:
  if target == i:
    count += 1
print("Count:",count)
