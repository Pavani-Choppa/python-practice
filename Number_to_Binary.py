# Read the number
n = int(input())

# Convert to binary and print
rem = []
while n > 0:
  rem.append(n % 2)
  n //= 2
print(*rem[::-1],sep="")
  
