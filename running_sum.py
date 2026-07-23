# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Print running sum
sum = 0
res = []
for i in numbers:
  sum += i
  res.append(sum)
print(*res)
