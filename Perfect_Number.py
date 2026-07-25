# Read the number
n = int(input())

# Check and print
divisor = []
for i in range(1,n):
  if n % i == 0:
    divisor += [i]
if sum(divisor) == n:
  print("Yes")
else:
  print("No")
    
