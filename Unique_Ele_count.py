# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Count and print unique numbers

count = 0
for i in numbers:
  if numbers.count(i) == 1:
    count += 1
print("Unique:",count)
