# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Reverse and print
print(*numbers[::-1])
