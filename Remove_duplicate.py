# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Remove duplicates and print
res = []
for i in numbers:
  if i not in res:
    res.append(i)
print(*res)
