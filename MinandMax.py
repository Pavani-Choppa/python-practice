# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Find and print min and max
#print("Min:",min(numbers))
#print("Max:",max(numbers))
mi = ma = numbers[0]
for i in numbers:
  if i < mi:
    mi = i
  elif i > ma:
    ma = i
print("Min:",mi)
print("Max:",ma)
  
