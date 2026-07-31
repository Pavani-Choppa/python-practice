# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
k = int(input())

# Rotate left and print
k = k % n
rotated = numbers[k:] + numbers[:k]
print(*rotated)
