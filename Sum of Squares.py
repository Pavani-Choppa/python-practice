# Read N
n = int(input())

# Calculate and print sum of squares
sumi = []
sum = 0
sumi = [x**2 for x in range(n+1)] 
for i in sumi:
    sum += i
print("Sum:",sum)
