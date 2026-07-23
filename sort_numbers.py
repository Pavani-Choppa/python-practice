# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Sort and print
print(*sorted(numbers))
