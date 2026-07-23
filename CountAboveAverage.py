# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Calculate average and count above
avg = sum(numbers)/n
count = 0
for i in numbers:
  if i > avg:
    count += 1
print("Above average:",count)
    
  
