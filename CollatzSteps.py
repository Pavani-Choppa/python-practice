# Read the number
n = int(input())

# Count steps to reach 1
count = 0
while n != 1:
  if n % 2 == 0:
    n //= 2
  else:
    n = 3 * n + 1
  count += 1
print("Steps: "+str(count))
